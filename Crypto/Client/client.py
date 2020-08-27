import socket
import os
import sys

from time import sleep

from os import system, getcwd
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Hash import HMAC, SHA256
from Crypto.Signature import pss

from datetime import date, datetime

class Security: # Superclass.
    def __init__(self):
        # Location of various key files.
        self.base_key_path = getcwd() + "\\KeyFile\\"
        self.client_public_key = self.base_key_path + "client_public.pem"
        self.client_private_key = self.base_key_path + "client_private.pem"
        self.server_public_key = self.base_key_path + "server_public.pem"
        self.default_encoding = 'utf-8'
        
    # Get key from file and return it in binary format.
    def get_key_from_file(self, key_file):
        key = RSA.import_key(open(key_file, "rb").read())
        return key

    # Plaintext has to be encoded first.
    # Public key in binary format.
    def rsa_encrypt(self, plaintext, public_key):
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    # Ciphertext has to be encoded first.
    # Private key in binary format.
    def rsa_decrypt(self, ciphertext, private_key):
        cipher = PKCS1_OAEP.new(private_key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

    # Plaintext have to be encoded first.
    def aes_encrypt(self, plaintext):
        session_key = get_random_bytes(32)
        cipher = AES.new(session_key, AES.MODE_CBC)
        
        padded_data = pad(plaintext, AES.block_size)
        ciphertext_bytes = cipher.encrypt(padded_data)

        iv = cipher.iv
        
        # After b64 encoding iv, iv will be constant length of 24 bytes.
        b64encoded_iv = b64encode(iv).decode(self.default_encoding)

        b64encoded_ciphertext = b64encode(ciphertext_bytes).decode(self.default_encoding)

        # Combine both iv and ciphertext to become one string.
        b64encoded_iv_and_ciphertext = b64encoded_iv + b64encoded_ciphertext

        return b64encode(session_key).decode(self.default_encoding), b64encoded_iv_and_ciphertext

    # iv - b64 encoded. 
    # iv_and_ciphertext - b64 encoded.
    def aes_decrypt(self, key, iv_and_ciphertext):
        # First 24 bytes will be iv.
        iv = b64decode(iv_and_ciphertext[0:24])

        # After the initial 24 bytes, it will be the ciphertext.
        ciphertext = b64decode(iv_and_ciphertext[24:])

        key = b64decode(key)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size)

        return plaintext.decode(self.default_encoding)

    # message - has to be encoded first.
    # secret_key - binary format.
    def get_hmac(self, message, secret_key):
        new_hmac = HMAC.new(secret_key, digestmod=SHA256)
        new_hmac.update(message)

        # Returns hex representation instead of bytes.
        return new_hmac.hexdigest()

    # message - has to be encoded first.
    # secret_key - binary format.
    # mac - hex representation or hexdigest.
    def verify_hmac(self, message, secret_key, mac):
        new_hmac = HMAC.new(secret_key, digestmod=SHA256)
        new_hmac.update(message)

        try:
            new_hmac.hexverify(mac)
            return True

        except ValueError:
            return False

    # message - has to be encoded first.
    # private_key - binary format.
    # returns b64 encoded signature.
    def rsa_sign(self, message, private_key):
        digest = SHA256.new(message)
        signature = pss.new(private_key).sign(digest)

        return b64encode(signature).decode(self.default_encoding)
    
    # message - has to be encoded first.
    # signature - binary format.
    # public_key - binary format
    def rsa_verify(self, message, signature, public_key):
        digest = SHA256.new(message)
        verifier = pss.new(public_key)

        try:
            verifier.verify(digest, signature)
            return True
        
        except (ValueError, TypeError):
            return False

    # Data must be in binary format.
    def get_file_hash(self, data):
        hash_sha256 = SHA256.new()
        hash_sha256.update(data)

        return hash_sha256.hexdigest()
        
class Client(Security): # Subclass.
    def __init__(self, server_ip, server_port):
        super().__init__() # Allows calling of methods of superclass in subclass.
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = 1024
        self.log_base_directory = getcwd() + "\\Logs\\"
        self.menu_base_directory = getcwd() + "\\Menu\\"
        self.data_file = self.menu_base_directory + "menu.txt"
        self.data_block_size = 256
        self.short_sleep_time = 1.2
        self.long_sleep_time = 2
        self.default_encoding = 'utf-8'

    def clear_screen(self):
        system("cls")
    
    @property
    def get_current_date(self):
        today = date.today()
        todays_date = today.strftime("%d_%m_%Y")
        return todays_date

    @property
    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @property
    def get_current_time_for_file(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        return current_time

    def test_connection_to_server(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect_to_server:
                connect_to_server.connect((self.server_ip, self.server_port))
                connect_to_server.close()

                return True
        
        except ConnectionError:
            return False

    def print_and_log(self, data):
        log_filename = self.log_base_directory + self.get_current_date + " - log.txt"

        with open(log_filename, "a+") as log_file:
            print(data)
            log_file.write(data + "\n")

    def pause(self):
        system("pause")
    
    def short_pause(self):
        sleep(self.short_sleep_time)

    def long_pause(self):
        sleep(self.long_sleep_time)

    def upload_data(self, data_to_send):
        b64encoded_session_key, b64encoded_iv_and_ciphertext = self.aes_encrypt(data_to_send)

        self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) Unencrypted Session key - {b64encoded_session_key}")
        self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) AES encrypted data(iv & ciphertext) ({len(b64encoded_iv_and_ciphertext)} bytes) - {b64encoded_iv_and_ciphertext}")

        # 344 Bytes on RSA signature
        # RSA signature on iv and ciphertext
        client_private_key = self.get_key_from_file(self.client_private_key)
        rsa_signature_iv_and_ciphertext = self.rsa_sign(b64encoded_iv_and_ciphertext.encode(self.default_encoding), client_private_key)
        self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) RSA signature on iv and ciphertext ({len(rsa_signature_iv_and_ciphertext)} bytes) - {rsa_signature_iv_and_ciphertext}")    

        rsa_signed_b64encoded_iv_and_ciphertext = rsa_signature_iv_and_ciphertext + b64encoded_iv_and_ciphertext 

        # HMAC signature -> [RSA signature] + [b64 encoded iv and ciphertext].
        hmac_signature = self.get_hmac(rsa_signed_b64encoded_iv_and_ciphertext.encode(self.default_encoding), b64decode(b64encoded_session_key))
        self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) HMAC signature ({len(hmac_signature)} bytes)- {hmac_signature}")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect_to_server:
                connect_to_server.connect((self.server_ip, self.server_port))

                connect_to_server.send(rsa_signed_b64encoded_iv_and_ciphertext.encode(self.default_encoding))
                data_from_server = connect_to_server.recv(self.buffer_size)

                if data_from_server == b"Encrypted data ok":
                    # Encrypt session key with server's public key.
                    server_public_key = self.get_key_from_file(self.server_public_key)
                    rsa_encrypted_session_key_bytes = self.rsa_encrypt(b64decode(b64encoded_session_key), server_public_key)
                    b64encoded_rsa_encrypted_session_key = b64encode(rsa_encrypted_session_key_bytes)

                    self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) RSA encrypted session key ({len(b64encoded_rsa_encrypted_session_key.decode(self.default_encoding))} bytes) - {b64encoded_rsa_encrypted_session_key.decode(self.default_encoding)}")

                    # First 64 bytes - signature , After 64 bytes - b64 encoded rsa encrypted session key   
                    hmac_signature_and_b64encoded_rsa_encrypted_session_key = hmac_signature + b64encoded_rsa_encrypted_session_key.decode(self.default_encoding)

                    connect_to_server.send(hmac_signature_and_b64encoded_rsa_encrypted_session_key.encode(self.default_encoding))
                    data_from_server = connect_to_server.recv(self.buffer_size)

                    if data_from_server == b"Session key ok":
                        connect_to_server.close()
                        self.print_and_log(f"[!] ({self.get_current_date} {self.get_current_time}) Closed connection to Server - IP: {self.server_ip} , PORT: {self.server_port}")
                        print()

        except ConnectionError as error:
            self.print_and_log(f"\n[!] ({self.get_current_date} {self.get_current_time}) Connection error:\n{error}")
            return "break"

    def upload_file(self):
        while True:
            with open(self.data_file, "rb") as df:
                self.clear_screen()
                plaintext_block = df.read(self.data_block_size)

                while plaintext_block != b"":
                    return_code = self.upload_data(plaintext_block)

                    if return_code == "break":
                        sys.exit(1)
                    
                    else:
                        plaintext_block = df.read(self.data_block_size)

            with open(self.data_file, "rb") as df:
                data = df.read()
                file_hash = self.get_file_hash(data)
                data_to_send = f"upload_finished|{file_hash}"

            self.upload_data(data_to_send.encode(self.default_encoding))
            break

    def menu(self):
        while True:
            self.clear_screen()

            print("1. Upload Food Menu.")
            print("2. Exit.")

            try:
                option = int(input("\nOption - "))

                if option == 1:
                    self.clear_screen()
                    self.upload_file()
                    self.pause()

                elif option == 2:
                    self.clear_screen()
                    self.upload_data(b"exit")
                    break

            except ValueError:
                print("\nOnly numbers are accepted.")
                self.short_pause()

    def client_start(self):
        # Test connection to server before displaying menu.
        connection_ok = self.test_connection_to_server()

        if connection_ok:
            self.menu()
        
        else:
            self.print_and_log(f"\n[!] Unable to connect to server, SERVER IP - {self.server_ip} , SERVER PORT - {self.server_port}\n")

client = Client("127.0.0.1", 4444)
client.client_start()