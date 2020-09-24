import base64
import os
import sys

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from os import path

class Encryption:
    SALT = b"My$@lT"
    DATA_BLOCK_SIZE = 256

    @classmethod
    # https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
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
            with open(src_filename, "rb") as src_file:
                with open(dest_filename, "w") as dest_file:
                    plainText_block = src_file.read(cls.DATA_BLOCK_SIZE)

                    while plainText_block != b"":
                        cipherText_block = crypto.encrypt(plainText_block)
                        
                        # To remove newlines at the end of the file.
                        if index == 0:
                            dest_file.write(f"{cipherText_block.decode()}")
                        else:
                            dest_file.write(f"\n{cipherText_block.decode()}")
                        
                        plainText_block = src_file.read(cls.DATA_BLOCK_SIZE)
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

class Program:
    @classmethod
    def show_help(cls):
        # Only get program name, not interested in full path.
        programName = sys.argv[0].split('\\')
        programName = programName[len(programName) -1]

        headerName = "Program Usage"

        print("-" * 64)
        print(f"{headerName:>35}")
        print("-" * 64)
        print(" Command - encrypt or decrypt\n")
        print(f" {programName} command plainTextFile.txt cipherTextFile.txt")
        print(f" {programName} command cipherTextFile.txt plainTextFile.txt")

    @classmethod
    def show_args(cls):
        # List all arguments including program name.
        for index in range(len(sys.argv)):
            fmt_index = f"[{index}]"
            print(f"Arg {fmt_index:<4} - {sys.argv[index]}")
    
    @classmethod
    def execute(cls):
        # sys.argv[0] - program name
        # sys.argv[1] - commands or actions

        if len(sys.argv) < 5:
            Program.show_help()
        
        else:
            command = sys.argv[1].lower().strip()

            if command != "encrypt" and command != "decrypt":
                Program.show_help()

            else:
                password = sys.argv[2].strip()
                src_file = sys.argv[3].strip() 
                dest_file = sys.argv[4].strip()

                if path.isfile(src_file):
                    if command == "encrypt":
                        Encryption.encrypt_file(password, src_file, dest_file)
                        print("\nEncryption Done!")

                    elif command == "decrypt":
                        Encryption.decrypt_file(password, src_file, dest_file)
                        print("\nDecryption Done!")

                else:
                    Program.show_help()
                    print(f"\nError - {src_file} does not exists.")

if __name__ == "__main__":
    Program.execute()