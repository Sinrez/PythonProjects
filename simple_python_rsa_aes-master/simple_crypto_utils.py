from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from base64 import encodebytes, b64decode
from pathlib import Path

#читаем секрет
with open('secret.txt', 'r') as sec:
    secret = sec.read().encode()

def keysgen(prj_name):
    """Генерация начальной ключевой пары для ассиметричного шифрования по алгоритму RSA"""
    keys_path = Path(Path.cwd(), 'keys')
    keys_path.mkdir(parents=True, exist_ok=True)  # создание каталога, если он не существует
    # Создание закрытого (секретного) ключа
    privatekey = RSA.generate(2048)
    # Запись закрытого (секретного) ключа в файл
    sec_path = Path(keys_path, prj_name + '.seprk')
    with open(sec_path, 'wb') as f:
        f.write(bytes(privatekey.exportKey('PEM')))
    # Создание открытого (публичного) ключа
    publickey = privatekey.publickey()
    # Запись открытого (публичного) ключа в файл
    pub_path = Path(keys_path, prj_name + '.sepbk')
    with open(pub_path, 'wb') as f:
        f.write(bytes(publickey.exportKey('PEM')))


def encrypt(plain_path, pub_key):
    """Шифрование файла"""
    # Генерация сессионного ключа симметричного шифрования для алгоритма AES
    sessionkey = Random.new().read(32)  # 256 бит
    # Загрузка в память архива для зашифрования в двоичном виде
    f = open(plain_path, 'rb')
    plaintext = f.read()
    f.close()
    # Шифрование архива 'plaintext.rar' по алгоритму AES
    iv = Random.new().read(16)  # 128 bit
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    ciphertext = iv + obj.encrypt(plaintext)
    ciphertext = bytes(ciphertext)
    # Шифрование сессионного симметричного ключа открытым ассимметричным ключом получателя
    publickey = RSA.importKey(open(pub_key, 'rb').read())  # 'public_key.txt'
    cipherrsa = PKCS1_OAEP.new(publickey)
    sessionkey = cipherrsa.encrypt(sessionkey)
    # Запись зашифрованного сессионного ключа в файл
    f = open(plain_path + '.seef', 'wb')
    f.write(bytes(sessionkey) + encodebytes(secret) + bytes(ciphertext))
    f.close()


def decrypt(enc_path, sec_key):
    """Расшифровка файла"""
    # Расшифровка сессионного ключа закрытым (секретным) ключом по алгоритму RSA
    privatekey = RSA.importKey(open(sec_key, 'rb').read())
    cipherrsa = PKCS1_OAEP.new(privatekey)
    f = open(enc_path, 'rb')
    encrypted = f.read().split(encodebytes(secret))
    sessionkey = encrypted[0]
    sessionkey = cipherrsa.decrypt(sessionkey)
    # Расшифровка архива сессионным ключом, полученном на предыдущем шаге
    ciphertext = encrypted[1]
    f.close()
    iv = ciphertext[:16]
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    plaintext = obj.decrypt(ciphertext)
    plaintext = plaintext[16:]
    # Запись расшифрованного архива в файл 'decrypted.rar'
    f = open(enc_path[:-5] + '.decrypted', 'wb')
    f.write(bytes(plaintext))
    f.close()
