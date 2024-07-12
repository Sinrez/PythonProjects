import json
from datetime import datetime, timezone
from pprint import pprint
from hashlib import sha256
import random

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = [] #  список незавершенных транзакций

        # Делаем нулевой блок генезиса- начальный блок
        print("Creating genesis block")
        self.new_block()

    def last_block(self):
        # # Получает последний блок в проходе цепочки
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
        # Добавляет блок в цепочку
        self.chain.append(block)
        print(f"Created block {block['index']}")
        print()
        pprint(block)
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
        #подтверждение выполненной работы через подбор блока
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

        self.chain.append(new_block)
        print("Found a new block: ", new_block)

if __name__ == '__main__':
    bc = Blockchain()
    print()
    bc.new_block(previous_hash=bc.chain[0]['hash'])
