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
    # For use in decrypting filename.
    # Plaintext - must be in binary format.
    # get_key() will automatically encode password.
    def decrypt(cls, password, cipherText):
        key = cls.get_key(password)
        crypto = Fernet(key)

        plainText = crypto.decrypt(cipherText)
        return plainText

    @classmethod
    # For use in encrypting filename.
    # Plaintext - must be in binary format.
    # get_key() will automatically encode password.
    def encrypt(cls, password, plainText):
        key = cls.get_key(password)
        crypto = Fernet(key)

        cipherText = crypto.encrypt(plainText)
        return cipherText

    @classmethod
    def encrypt_file(cls, password, src_filename):
        key = cls.get_key(password)
        crypto = Fernet(key)
        
        # destination filename must be in string format.
        dest_filename = Encryption.encrypt(password, src_filename.encode()).decode()

        try:
            with open(src_filename, "rb") as src_file:
                with open(dest_filename, "w") as dest_file:
                    plainText_block = src_file.read(cls.DATA_BLOCK_SIZE)

                    index = 0
                    while plainText_block != b"":
                        cipherText_block = crypto.encrypt(plainText_block)
                        
                        # To remove newlines at the end of the file.
                        if index == 0:
                            dest_file.write(f"{cipherText_block.decode()}")
                            index += 1

                        else:
                            dest_file.write(f"\n{cipherText_block.decode()}")
                        
                        plainText_block = src_file.read(cls.DATA_BLOCK_SIZE)
    
        except AssertionError:
            sys.exit(1)

    @classmethod
    def decrypt_file(cls, password, src_filename):
        key = cls.get_key(password)
        crypto = Fernet(key)

        # destination filename must be in string format.
        dest_filename = Encryption.decrypt(password, src_filename.encode()).decode()

        # Split using newlines as delimeter.
        cipherText_list = open(src_filename).read().splitlines()
        
        try:
            with open(dest_filename, "w", newline = "\n") as df:
                for cipherText in cipherText_list:
                    plainText = crypto.decrypt(cipherText.encode()).decode()
                    df.write(plainText)

        except AssertionError:
            sys.exit(1)

class Program:
    @classmethod
    def show_help(cls):
        programName = Program.get_name()
        headerName = "Program Usage"

        print("-" * 64)
        print(f"{headerName:>35}")
        print("-" * 64)

        print()
        print(f" {programName} encrypt plainTextFile.txt")
        print(f" {programName} decrypt cipherTextFile.txt")

    @classmethod
    def get_name(cls):
        # Only get program name, not interested in full path.
        programName = sys.argv[0].split('\\')
        programName = programName[len(programName) -1]

        return programName

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

        if len(sys.argv) < 4:
            Program.show_help()
        
        else:
            command = sys.argv[1].lower().strip()

            if command != "encrypt" and command != "decrypt":
                Program.show_help()

            else:
                password = sys.argv[2].strip()
                src_file = sys.argv[3].strip() 

                if path.isfile(src_file):
                    if command == "encrypt":
                        Encryption.encrypt_file(password, src_file)
                        print("\nEncryption Done!")

                    elif command == "decrypt":
                        Encryption.decrypt_file(password, src_file)
                        print("\nDecryption Done!")

                else:
                    Program.show_help()
                    print(f"\nError - {src_file} does not exists.")

if __name__ == "__main__":
    Program.execute()