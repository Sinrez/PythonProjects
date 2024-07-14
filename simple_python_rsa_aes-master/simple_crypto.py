from simple_crypto_utils import keysgen, encrypt, decrypt
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', help="Action keys/encrypt/decrypt")
parser.add_argument('-n', '--name', help="Project name")
parser.add_argument('-p', '--path', help="Path to file for encryption/decryption")
parser.add_argument('-pk', '--public_key', help="Path to received public key")
parser.add_argument('-prk', '--private_key', help="Path to your private key")
args = parser.parse_args()

if args.action == 'keys':
    if args.name:
        keysgen(args.name)
        print('Keys generated!')
    else:
        prj_name = input('Input project name: ')
        keysgen(prj_name)
        print('Keys generated!')

elif args.action == 'encrypt':
    if args.path:
        path = args.path
    else:
        path = input('Input path to file for encryption')
    if args.public_key:
        pub_key = args.public_key
    else:
        pub_key = input('Input path to public key file')
    encrypt(path, pub_key)

elif args.action == 'decrypt':
    if args.path:
        path = args.path
    else:
        path = input('Input path to file for decryption')
    if args.private_key:
        sec_key = args.private_key
    else:
        sec_key = input('Input path to private key file')
    decrypt(path, sec_key)
else:
    input('Unknown command! Press any key to continue.')
    os.system("python simple_crypto.py -h")


