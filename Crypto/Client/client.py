import socket
import os

from os import system, getcwd
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Security:
    def __init__(self):
        # Location of various key files.
        self.base_key_path = getcwd() + "\\KeyFile\\"
        self.client_public_key = self.base_key_path + "client_public.pem"
        self.client_private_key = self.base_key_path + "client_private.pem"
        self.server_public_key = self.base_key_path + "server_public.pem"

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
        b64encoded_iv = b64encode(iv).decode('utf-8')

        b64encoded_ciphertext = b64encode(ciphertext_bytes).decode('utf-8')

        # Combine both iv and ciphertext to become one string.
        b64encoded_iv_and_ciphertext = b64encoded_iv + b64encoded_ciphertext

        return b64encode(session_key).decode('utf-8'), b64encoded_iv_and_ciphertext

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

        return plaintext.decode('utf-8')

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = 1024

    def clear_screen(self):
        system("cls")

    def pause(self):
        system("pause")

    def client_start(self):
        while True:
            self.clear_screen()

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect_to_server:
                connect_to_server.connect((self.server_ip, self.server_port))
                
                plaintext = input("[+] Input text to send - ").encode('utf-8')
                b64encoded_session_key, b64encoded_iv_and_ciphertext = security.aes_encrypt(plaintext)

                print(f"\n[X] Unencrypted Session key - {b64encoded_session_key}")
                print(f"[X] AES encrypted data(iv & ciphertext) - {b64encoded_iv_and_ciphertext}")

                connect_to_server.send(b64encoded_iv_and_ciphertext.encode('utf-8'))
                data_from_server = connect_to_server.recv(self.buffer_size)

                if data_from_server == b"Encrypted data ok":
                    # Encrypt session key with server's public key.
                    server_public_key = security.get_key_from_file(security.server_public_key)
                    rsa_encrypted_session_key_bytes = security.rsa_encrypt(b64decode(b64encoded_session_key), server_public_key)
                    b64encoded_rsa_encrypted_session_key = b64encode(rsa_encrypted_session_key_bytes)

                    print(f"[X] RSA encrypted session key - {b64encoded_rsa_encrypted_session_key.decode('utf-8')}")

                    connect_to_server.send(b64encoded_rsa_encrypted_session_key)
                    data_from_server = connect_to_server.recv(self.buffer_size)

                    if data_from_server == b"Session key ok":
                        print()
                        self.pause()

security = Security()
client = Client("127.0.0.1", 4444)
client.client_start()