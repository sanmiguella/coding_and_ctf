import socket
import os

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

class Security:
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
        
class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = 1024
        self.data_file = getcwd() + "\\logs\\" + "log.txt"
        self.data_block_size = 256
        self.short_sleep_time = 1.2
        self.default_encoding = 'utf-8'

    def clear_screen(self):
        system("cls")

    def pause(self):
        system("pause")
    
    def short_pause(self):
        sleep(self.short_sleep_time)

    def upload_data(self, data_to_send):
        b64encoded_session_key, b64encoded_iv_and_ciphertext = security.aes_encrypt(data_to_send)

        print(f"\n[X] Unencrypted Session key - {b64encoded_session_key}")
        print(f"[X] AES encrypted data(iv & ciphertext) ({len(b64encoded_iv_and_ciphertext)} bytes) - {b64encoded_iv_and_ciphertext}")

        # 344 Bytes on RSA signature
        # RSA signature on iv and ciphertext
        client_private_key = security.get_key_from_file(security.client_private_key)
        rsa_signature_iv_and_ciphertext = security.rsa_sign(b64encoded_iv_and_ciphertext.encode(self.default_encoding), client_private_key)
        print(f"[X] RSA signature on iv and ciphertext ({len(rsa_signature_iv_and_ciphertext)} bytes) - {rsa_signature_iv_and_ciphertext}")    

        rsa_signed_b64encoded_iv_and_ciphertext = rsa_signature_iv_and_ciphertext + b64encoded_iv_and_ciphertext 

        # HMAC signature -> [RSA signature] + [b64 encoded iv and ciphertext].
        hmac_signature = security.get_hmac(rsa_signed_b64encoded_iv_and_ciphertext.encode(self.default_encoding), b64decode(b64encoded_session_key))
        print(f"[X] HMAC signature ({len(hmac_signature)} bytes)- {hmac_signature}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect_to_server:
            connect_to_server.connect((self.server_ip, self.server_port))

            connect_to_server.send(rsa_signed_b64encoded_iv_and_ciphertext.encode(self.default_encoding))
            data_from_server = connect_to_server.recv(self.buffer_size)

            if data_from_server == b"Encrypted data ok":
                # Encrypt session key with server's public key.
                server_public_key = security.get_key_from_file(security.server_public_key)
                rsa_encrypted_session_key_bytes = security.rsa_encrypt(b64decode(b64encoded_session_key), server_public_key)
                b64encoded_rsa_encrypted_session_key = b64encode(rsa_encrypted_session_key_bytes)

                print(f"[X] RSA encrypted session key ({len(b64encoded_rsa_encrypted_session_key.decode(self.default_encoding))} bytes) - {b64encoded_rsa_encrypted_session_key.decode(self.default_encoding)}")

                # First 64 bytes - signature , After 64 bytes - b64 encoded rsa encrypted session key   
                hmac_signature_and_b64encoded_rsa_encrypted_session_key = hmac_signature + b64encoded_rsa_encrypted_session_key.decode(self.default_encoding)

                connect_to_server.send(hmac_signature_and_b64encoded_rsa_encrypted_session_key.encode(self.default_encoding))
                data_from_server = connect_to_server.recv(self.buffer_size)

                if data_from_server == b"Session key ok":
                    pass

    def client_start(self):
        while True:
            with open(self.data_file, "rb") as df:
                self.clear_screen()
                plaintext_block = df.read(self.data_block_size)

                while plaintext_block != b"":
                    self.upload_data(plaintext_block)
                    plaintext_block = df.read(self.data_block_size)

            self.upload_data(b"upload_finished")
            break

security = Security()
client = Client("127.0.0.1", 4444)
client.client_start()