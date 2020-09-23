import base64
import os
import sys

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path

class Encryption:
    SALT = b"My$@lT"
    BLOCK_SIZE = 128

    @classmethod
    def get_key(cls, password):
        kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256,
            length = 32,
            salt = cls.SALT,
            iterations = 100000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    @classmethod
    def encrypt_file(cls, password, src_filename, dest_filename):
        key = cls.get_key(password)

        crypto = Fernet(key)
 
        index = 0

        try:
            with open(src_filename, "rb") as sf:
                with open(dest_filename, "w") as df:
                    plainText_block = sf.read(cls.BLOCK_SIZE)

                    while plainText_block != b"":
                        cipherText_block = crypto.encrypt(plainText_block)
                        
                        if index == 0:
                            df.write(f"{cipherText_block.decode()}")
                        else:
                            df.write(f"\n{cipherText_block.decode()}")
                        
                        plainText_block = sf.read(cls.BLOCK_SIZE)
                        index += 1
    
        except AssertionError:
            sys.exit(1)

    @classmethod
    def decrypt_file(cls, password, src_filename, dest_filename):
        key = cls.get_key(password)

        crypto = Fernet(key)
        index = 0

        cipherText_list = open(src_filename).read().splitlines()

        try:
            with open(dest_filename, "w", newline = "\n") as df:
                for cipherText in cipherText_list:
                    plainText = crypto.decrypt(cipherText.encode()).decode()

                    df.write(plainText)
                    index += 1

        except AssertionError:
            sys.exit(1)

def show_help():
    programName = sys.argv[0].split('\\')
    programName = programName[len(programName) -1]

    print("To run this program: ")
    print(f" {programName} [encrypt] plainTextFile.txt cipherTextFile.txt")
    print(f" {programName} [decrypt] cipherTextFile.txt plainTextFile.txt")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        show_help()
    
    else:
        command = sys.argv[1].lower().strip()

        if command != "encrypt" and command != "decrypt":
            show_help()

        else:
            password = sys.argv[2].strip()
            src_file = sys.argv[3].strip() 
            dest_file = sys.argv[4].strip()

            if path.isfile(src_file):
                if command == "encrypt":
                    result = Encryption.encrypt_file(password, src_file, dest_file)

                    print("\nEncryption Done!")

                elif command == "decrypt":
                    result = Encryption.decrypt_file(password, src_file, dest_file)

                    print("\nDecryption Done!")

            else:
                show_help()
                print(f"\nError - {src_file} does not exists.")