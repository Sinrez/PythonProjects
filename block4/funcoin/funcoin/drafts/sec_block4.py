import json
import sqlite3
from datetime import datetime, timezone
from pprint import pprint
from hashlib import sha256
import random
import easygui

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []  # список незавершенных транзакций

        # Инициализация базы данных
        self.conn = sqlite3.connect('blockchain.db')
        # self.create_table()

        # Делаем нулевой блок генезиса - начальный блок
        print("Creating genesis block")
        self.new_block()

    # def create_table(self):
    #     with self.conn:
    #         self.conn.execute('''CREATE TABLE IF NOT EXISTS blocks
    #                             (index INTEGER PRIMARY KEY,
    #                             timestamp TEXT,
    #                             transactions TEXT,
    #                             previous_hash TEXT,
    #                             nonce TEXT,
    #                             hash TEXT)''')

    # def save_block(self, block):
    #     with self.conn:
    #         self.conn.execute('''INSERT INTO blocks (index, timestamp, transactions, previous_hash, nonce, hash)
    #                             VALUES (?, ?, ?, ?, ?, ?)''', (block['index'], block['timestamp'], json.dumps(block['transactions']),
    #                                                             block['previous_hash'], block['nonce'], block['hash']))

    def last_block(self):
        # Получает последний блок в цепочке
        return self.chain[-1] if self.chain else None

    def new_block(self, previous_hash=None):
        # Генерирует новый блок и добавляет его в цепь
        block = {
            'index': len(self.chain),
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'nonce': format(random.getrandbits(64), "x")
        }

        # Возвращает хэш этого нового блока и добавляет его в блок
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # Сбрасывает список незавершенных транзакций
        self.pending_transactions = []
        self.chain.append(block)
        # self.save_block(block)
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

    def proof_of_work(self):
        # подтверждение выполненной работы через подбор блока
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

        print("Found a new block: ")
        pprint(new_block)

    def add_transaction(self):
        transaction = easygui.enterbox("Enter transaction data (e.g., 'sender:receiver:amount'):")
        if transaction:
            self.pending_transactions.append(transaction)

if __name__ == '__main__':
    bc = Blockchain()
    while True:
        choice = easygui.buttonbox("Select an option:", choices=["Add Transaction", "Mine Block", "Exit"])
        if choice == "Add Transaction":
            bc.add_transaction()
        elif choice == "Mine Block":
            bc.proof_of_work()
        elif choice == "Exit":
            break
