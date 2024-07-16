import json
from datetime import datetime, timezone
from pprint import pprint
from hashlib import sha256
import random
import easygui


class ImmutableList(object):
    #класс-обёрткf, управляет доступом к списку для эмуляции "неизменности" блокчейна
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

        # Делаем нулевой блок генезиса - начальный блок
        print("Creating genesis block")
        self.new_block()

    def last_block(self):
        # Получает последний блок в цепочке
        return self.__chain[-1] if len(self.__chain) > 0 else None

    def new_block(self, previous_hash=None, content_transactions=None):
        # Генерирует новый блок и добавляет его в цепь
        block = {
            'index': len(self.__chain),
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'content_transactions': content_transactions,
            'previous_hash': previous_hash,
            'nonce': format(random.getrandbits(64), "x")
        }

        # Возвращает хэш этого нового блока и добавляет его в блок
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # Сбрасывает список незавершенных транзакций
        self.__pending_transactions = []
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
        msg = f"Found a new block:\n{json.dumps(new_block, indent=4)}"
        easygui.msgbox(msg, title="New Block Found")

        # консоль для отладки оставим
        print("Found a new block:")
        pprint(new_block)

    def return_all_blocks(self):
        return list(self.__chain)


if __name__ == "__main__":
    bc = Blockchain()

    while True:
        title = "Data input to blockchain"
        choice = easygui.buttonbox("Select an option:", title=title, choices=["Add to Blockchain", "Show full blockchain", "Exit"])

        if choice == "Add to Blockchain":
            data = easygui.enterbox("Enter data:", title=title)
            if data:
                bc.proof_of_work(data)
            else:
                bc.proof_of_work()
        elif choice == "Show full blockchain":
            blocks = bc.return_all_blocks()
            if blocks:
                msg = "Blockchain:\n\n"
                for block in blocks:
                    msg += json.dumps(block, indent=4) + "\n\n"
                easygui.msgbox(msg, title="Full Blockchain")
            else:
                easygui.msgbox("Blockchain is empty.", title="Full Blockchain")
        elif choice == "Exit":
            break
