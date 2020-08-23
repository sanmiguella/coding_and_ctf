import socket
import os

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

        return b64encode(signature).decode('utf-8')
    
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

class Server:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip 
        self.server_port = server_port 
        self.buffer_size = 1024  
        self.log_base_directory = getcwd() + "\\Logs\\"
        self.upload_base_directory = getcwd() + "\\Uploads\\"
        self.uploaded_data = list()

    def clear_screen(self):
        system("cls")

    def get_current_date(self):
        today = date.today()
        todays_date = today.strftime("%d_%m_%Y")
        return todays_date

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def get_current_time_for_file(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        return current_time

    def print_and_log(self, data):
        log_filename = self.log_base_directory + self.get_current_date() + " - log.txt"

        with open(log_filename, "a+") as log_file:
            print(data)
            log_file.write(data + "\n")

    def server_start(self):
        self.clear_screen()
        print(f"[+] ({self.get_current_date()} {self.get_current_time()}) Starting server.")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_connection:
                server_connection.bind((self.server_ip, self.server_port))
                self.print_and_log(f"[+] ({self.get_current_date()} {self.get_current_time()}) Successfully created socket.")

                while True:
                    try:
                        server_connection.listen()
                        self.print_and_log(f"\n[+] ({self.get_current_date()} {self.get_current_time()}) Listening for incoming connection.")

                        connection, address = server_connection.accept()
                        client_ip, client_port = address

                        with connection:
                            self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) Connected by - Client IP : {client_ip} , Client PORT : {client_port}")

                            rsa_signed_b64encoded_iv_and_ciphertext = connection.recv(self.buffer_size).decode('utf-8')
                            rsa_signature_iv_and_ciphertext = rsa_signed_b64encoded_iv_and_ciphertext[0:344]
                            b64encoded_iv_and_ciphertext = rsa_signed_b64encoded_iv_and_ciphertext[344:]

                            self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) AES Encrypted data (iv & ciphertext) - {b64encoded_iv_and_ciphertext}")
                            connection.send(b"Encrypted data ok")

                            data_signature_and_b64encoded_rsa_encrypted_session_key = connection.recv(self.buffer_size).decode('utf-8')
                            data_signature = data_signature_and_b64encoded_rsa_encrypted_session_key[0:64]
                            b64encoded_rsa_encrypted_session_key = data_signature_and_b64encoded_rsa_encrypted_session_key[64:]

                            self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) HMAC signature - {data_signature}")

                            self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) RSA encrypted Session key - {b64encoded_rsa_encrypted_session_key}")
                            connection.send(b"Session key ok")

                            # Decrypt session key with server's private key
                            server_private_key = security.get_key_from_file(security.server_private_key)
                            rsa_decrypted_session_key_bytes = security.rsa_decrypt(b64decode(b64encoded_rsa_encrypted_session_key), server_private_key)
                            b64encoded_rsa_decrypted_session_key = b64encode(rsa_decrypted_session_key_bytes).decode('utf-8')
                            self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) RSA decrypted Session key - {b64encoded_rsa_decrypted_session_key}")

                            hmac_message_verified = security.verify_hmac(rsa_signed_b64encoded_iv_and_ciphertext.encode('utf-8'), b64decode(b64encoded_rsa_decrypted_session_key), data_signature)

                            # If message is hmac verified, proceed to do rsa verification.
                            if hmac_message_verified == True:
                                print(f"[X] ({self.get_current_date()} {self.get_current_time()}) Message HMAC verified.")
                                
                                client_public_key = security.get_key_from_file(security.client_public_key)
                                rsa_message_verified = security.rsa_verify(b64encoded_iv_and_ciphertext.encode('utf-8'), b64decode(rsa_signature_iv_and_ciphertext), client_public_key)

                                # If message is rsa verified, proceed to do aes decryption.
                                if rsa_message_verified:
                                    print(f"[X] ({self.get_current_date()} {self.get_current_time()}) Message RSA verified.")

                                    decrypted_message = security.aes_decrypt(b64encoded_rsa_decrypted_session_key, b64encoded_iv_and_ciphertext)
                                    self.print_and_log(f"[X] ({self.get_current_date()} {self.get_current_time()}) Plaintext:\n{decrypted_message}")

                                    self.uploaded_data.append(decrypted_message)

                                    if decrypted_message == 'exit' or decrypted_message == 'quit':
                                        self.print_and_log(f"\n[!] ({self.get_current_date()} {self.get_current_time()}) Terminating Server.")
                                        break

                                    if decrypted_message == 'upload_finished':
                                        self.uploaded_data.pop()
                                        upload_filename = self.upload_base_directory + self.get_current_date() + " - " + self.get_current_time_for_file() + " uploads.txt"

                                        with open(upload_filename, "w", newline = "\n") as upload_fname:
                                            for data in self.uploaded_data:
                                                upload_fname.write(data)

                                        print(f"[+] Saved uploaded data as \"{upload_filename}\"")
                                        self.uploaded_data.clear()

                                else:
                                    print(f"[!] ({self.get_current_date()} {self.get_current_time()}) RSA Signature verification failed.")

                            else:
                                print(f"[!] ({self.get_current_date()} {self.get_current_time()}) HMAC Message verification failed.")

                    except KeyboardInterrupt:
                        self.print_and_log(f"\n[!] ({self.get_current_date()} {self.get_current_time()}) CTRL + C pressed. Terminating Server.")
                        break

                    except Exception as error:
                        self.print_and_log(f"\n[!] ({self.get_current_date()} {self.get_current_time()}) Error:\n{error}")

security = Security()
server = Server("127.0.0.1", 4444)
server.server_start()