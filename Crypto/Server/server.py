import socket
import os
import sys, signal

from os import system, getcwd
from base64 import b64encode, b64decode
from datetime import date, datetime

from Security import Security

class Server(Security): # Subclass.
    def __init__(self, server_ip, server_port):
        super().__init__()
        self.server_ip = server_ip 
        self.server_port = server_port 
        self.buffer_size = 1024  
        self.log_base_directory = getcwd() + "\\Logs\\"
        self.upload_base_directory = getcwd() + "\\Uploads\\"
        self.menu_base_directory = getcwd() + "\\Menu\\"
        self.uploaded_data = list()
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

    def signal_handler(self, signal, frame):
        self.print_and_log(f"\n[!] ({self.get_current_date} {self.get_current_time}) Server terminated by CTRL+C , Goodbye!")
        sys.exit(0) # Graceful exit.

    def print_and_log(self, data):
        log_filename = self.log_base_directory + self.get_current_date + " - log.txt"

        with open(log_filename, "a+") as log_file:
            print(data)
            log_file.write(data + "\n")

    def receive_and_decrypt(self, connection, client_ip, client_port):
        with connection:
            self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) Connected by - Client IP : {client_ip} , Client PORT : {client_port}")

            # Receiving of data from Client.
            rsa_signed_b64encoded_iv_and_ciphertext = connection.recv(self.buffer_size).decode(self.default_encoding)

            rsa_signature_iv_and_ciphertext = rsa_signed_b64encoded_iv_and_ciphertext[0:344]
            b64encoded_iv_and_ciphertext = rsa_signed_b64encoded_iv_and_ciphertext[344:]

            self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) AES Encrypted data (iv & ciphertext) - {b64encoded_iv_and_ciphertext}")
            connection.send(b"Encrypted data ok")

            data_signature_and_b64encoded_rsa_encrypted_session_key = connection.recv(self.buffer_size).decode(self.default_encoding)
            data_signature = data_signature_and_b64encoded_rsa_encrypted_session_key[0:64]
            b64encoded_rsa_encrypted_session_key = data_signature_and_b64encoded_rsa_encrypted_session_key[64:]

            self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) HMAC signature - {data_signature}")

            self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) RSA encrypted Session key - {b64encoded_rsa_encrypted_session_key}")
            connection.send(b"Session key ok")

            # Decrypt session key with server's private key
            server_private_key = self.get_key_from_file(self.server_private_key)
            rsa_decrypted_session_key_bytes = self.rsa_decrypt(b64decode(b64encoded_rsa_encrypted_session_key), server_private_key)
            b64encoded_rsa_decrypted_session_key = b64encode(rsa_decrypted_session_key_bytes).decode(self.default_encoding)
            self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) RSA decrypted Session key - {b64encoded_rsa_decrypted_session_key}")

            hmac_message_verified = self.verify_hmac(rsa_signed_b64encoded_iv_and_ciphertext.encode(self.default_encoding), b64decode(b64encoded_rsa_decrypted_session_key), data_signature)

            # If message is hmac verified, proceed to do rsa verification.
            if hmac_message_verified == True:
                self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) Message HMAC verified.")
                
                client_public_key = self.get_key_from_file(self.client_public_key)
                rsa_message_verified = self.rsa_verify(b64encoded_iv_and_ciphertext.encode(self.default_encoding), b64decode(rsa_signature_iv_and_ciphertext), client_public_key)

                # If message is rsa verified, proceed to do aes decryption.
                if rsa_message_verified:
                    self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) Message RSA verified.")

                    decrypted_message = self.aes_decrypt(b64encoded_rsa_decrypted_session_key, b64encoded_iv_and_ciphertext)
                    self.print_and_log(f"[X] ({self.get_current_date} {self.get_current_time}) Plaintext:\n{decrypted_message}")

                    return decrypted_message

                else:
                    self.print_and_log(f"[!] ({self.get_current_date} {self.get_current_time}) RSA Signature verification failed.")
                    return "error"

            else:
                self.print_and_log(f"[!] ({self.get_current_date} {self.get_current_time}) HMAC Message verification failed.")
                return "error"

    def server_start(self):
        signal.signal(signal.SIGINT, server.signal_handler)

        self.clear_screen()
        self.print_and_log(f"[+] ({self.get_current_date} {self.get_current_time}) Starting server.")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_connection:
                server_connection.bind((self.server_ip, self.server_port))
                self.print_and_log(f"[+] ({self.get_current_date} {self.get_current_time}) Successfully created socket.")

                while True:
                    try:
                        server_connection.listen()
                        self.print_and_log(f"\n[+] ({self.get_current_date} {self.get_current_time}) Listening for incoming connection.")

                        connection, address = server_connection.accept()
                        client_ip, client_port = address

                        decrypted_message = self.receive_and_decrypt(connection, client_ip, client_port)

                        if decrypted_message == 'exit' or decrypted_message == 'quit':
                            self.print_and_log(f"\n[!] ({self.get_current_date} {self.get_current_time}) Terminating Server.")
                            break

                        elif decrypted_message == 'test connection':
                            self.print_and_log(f"\n[#] Received test connection from client - test ok.")

                        elif 'upload_finished|' in decrypted_message:
                            # Command|hash
                            hash_from_client = decrypted_message.split("|")[1]

                            upload_filename = self.upload_base_directory + self.get_current_date + " - " + self.get_current_time_for_file + " uploads.txt"

                            with open(upload_filename, "w", newline = "\n") as upload_fname:
                                for data in self.uploaded_data:
                                    upload_fname.write(data)

                            self.print_and_log(f"[+] Saved uploaded data as \"{upload_filename}\"")
                            self.uploaded_data.clear()

                            with open(upload_filename, "rb") as upload_fname:
                                data = upload_fname.read()
                                uploaded_filename_hash = self.get_file_hash(data)
                            
                            self.print_and_log(f"[+] Computed Hash - {uploaded_filename_hash}")
                            self.print_and_log(f"[+] Hash from Client - {hash_from_client}")

                            if uploaded_filename_hash == hash_from_client:
                                self.print_and_log("[+] Uploaded file hash fully verified, no tampering detected.")
                            else:
                                self.print_and_log("[!] Uploaded file failed hash verification, file may be tampered.")
                            
                        elif decrypted_message == "error":
                            pass

                        else:
                            self.uploaded_data.append(decrypted_message)

                    except ConnectionError as error:
                        self.print_and_log(f"\n[!] ({self.get_current_date} {self.get_current_time}) Connection error:\n{error}")

                    except Exception as error:
                        self.print_and_log(f"\n[!] ({self.get_current_date} {self.get_current_time}) Error:\n{error}")

server = Server("127.0.0.1", 4444)
server.server_start()