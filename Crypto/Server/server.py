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
        self.server_public_key = self.base_key_path + "server_public.pem"
        self.server_private_key = self.base_key_path + "server_private.pem"
        self.client_public_key = self.base_key_path + "client_public.pem"

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

    # key - b64 encoded.
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

class Server:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip 
        self.server_port = server_port 
        self.buffer_size = 1024  

    def clear_screen(self):
        system("cls")

    def server_start(self):
        self.clear_screen()
        print("[+] Starting server.")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_connection:
                server_connection.bind((self.server_ip, self.server_port))
                print("[+] Successfully created socket.")

                while True:
                    try:
                        server_connection.listen()
                        print("\n[+] Listening for incoming connection.")

                        connection, address = server_connection.accept()
                        client_ip, client_port = address

                        with connection:
                            print(f"[X] Connected by - Client IP : {client_ip} , Client PORT : {client_port}")

                            b64encoded_iv_and_ciphertext = connection.recv(self.buffer_size).decode('utf-8')
                            print(f"[X] AES Encrypted data (iv & ciphertext) - {b64encoded_iv_and_ciphertext}")
                            connection.send(b"Encrypted data ok")

                            b64encoded_rsa_encrypted_session_key = connection.recv(self.buffer_size).decode('utf-8')
                            print(f"[X] RSA encrypted Session key - {b64encoded_rsa_encrypted_session_key}")
                            connection.send(b"Session key ok")

                            # Decrypt session key with server's private key
                            server_private_key = security.get_key_from_file(security.server_private_key)
                            rsa_decrypted_session_key_bytes = security.rsa_decrypt(b64decode(b64encoded_rsa_encrypted_session_key), server_private_key)
                            b64encoded_rsa_decrypted_session_key = b64encode(rsa_decrypted_session_key_bytes).decode('utf-8')
                            print(f"[X] RSA decrypted Session key - {b64encoded_rsa_decrypted_session_key}")

                            decrypted_message = security.aes_decrypt(b64encoded_rsa_decrypted_session_key, b64encoded_iv_and_ciphertext)
                            print(f"[X] Plaintext - {decrypted_message}")

                    except Exception as error:
                        print(f"\n[!] Error:\n{error}")

                    except KeyboardInterrupt:
                        print("\n[!] Terminating Server.")
                        break
         
security = Security()
server = Server("127.0.0.1", 4444)
server.server_start()