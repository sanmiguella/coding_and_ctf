import socket
import os
import sys

from time import sleep

from os import system, getcwd
from base64 import b64encode, b64decode
from datetime import date, datetime

from Security import Security
        
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