import json
from datetime import datetime, timezone
from pprint import pprint
from hashlib import sha256
import random
import easygui
from pprint import pprint
import sqlite3


class ImmutableList:
    def __init__(self):
        self._list = []
        
    def append(self, item):
        self._list.append(item)

    def __getitem__(self, index):
        return self._list[index]

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return repr(self._list)


class Blockchain(object):
    def __init__(self):
        self.__chain = ImmutableList()
        self.init_db()

        # Делаем нулевой блок генезиса - начальный блок
        print("Creating genesis block")
        self.new_block()

    def init_db(self):
        self.conn = sqlite3.connect('blockchain.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                hash TEXT,
                previous_hash TEXT,
                json_data TEXT
            )
        ''')
        self.conn.commit()

    def save_block_to_db(self, block):
        self.cur.execute('''
            INSERT INTO blocks (timestamp, hash, previous_hash, json_data)
            VALUES (?, ?, ?, ?)
        ''', (block['timestamp'], block['hash'], block['previous_hash'], json.dumps(block)))
        self.conn.commit()

    def load_blocks_from_db(self):
        self.cur.execute('SELECT json_data FROM blocks ORDER BY id')
        rows = self.cur.fetchall()
        for row in rows:
            block = json.loads(row[0])
            self.__chain.append(block)


    def last_block(self):
        # Получает последний блок в цепочке
        return self.__chain.__getitem__(-1) if len(self.__chain) > 0 else None

    def new_block(self, previous_hash=None, content_transactions=None):
        """Генерирует новый блок и добавляет его в цепь"""
        block = {
            'index': self.__chain.__len__(),
            # 'timestamp': datetime.now(timezone.utc).isoformat(),
            'timestamp': datetime.now(timezone.utc).strftime('%d:%m:%Y %H:%M:%S.%f'),
            'content_transactions': content_transactions,
            'previous_hash': previous_hash,
            'nonce': format(random.getrandbits(64), "x")
        }

        # Возвращает хэш этого нового блока и добавляет его в блок
        block_hash = self.hash(block)
        block["hash"] = block_hash
        return block

    @staticmethod
    def hash(block):
        # вычисление хэша блока
        # Гарантирует, что словарь отсортирован, иначе у нас будут несогласованные хэши
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @staticmethod
    def valid_block(block):
        # Проверяем, что хэш блока начинается с 4 нулей 0000
        return block["hash"].startswith("0000")

    def proof_of_work(self, content_transactions=None):
        # подтверждение выполненной работы через подбор блока
        while True:
            prev_hash = self.last_block()["hash"] if self.last_block() else None
            new_block = self.new_block(prev_hash, content_transactions)
            if self.valid_block(new_block):
                break

        self.__chain.append(new_block)
        print("Found a new block:")
        pprint(new_block)

    def return_all_blocks(self):
        return list(self.__chain)

if __name__ == "__main__":
    bc = Blockchain()

    while True:
        title = "Ввод данных в блокчейн"
        choice = easygui.buttonbox("Выберите опцию:", title=title, choices=["Добавить в блокчейн", "Показать весь блокчейн", "Сохранить блокчейн в БД", "Выход"])
        
        if choice == "Добавить в блокчейн":
            content = easygui.enterbox("Введите данные для добавления в блокчейн:")
            bc.proof_of_work(content)
        elif choice == "Показать весь блокчейн":
            blocks = bc.return_all_blocks()
            if blocks:
                msg = "Blockchain:\n\n"
                for block in blocks:
                    msg += json.dumps(block, indent=4, ensure_ascii=False) + "\n\n"
                easygui.msgbox(msg, title="Полный блокчейн")
        elif choice == "Сохранить блокчейн в БД":
            for block in bc.return_all_blocks():
                bc.save_block_to_db(block)
            easygui.msgbox("Блокчейн сохранен в БД.", title="Сохранение")
        elif choice == "Выход":
            break