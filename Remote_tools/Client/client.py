import socket

from os import system, getcwd
from Security import Security
from base64 import b64encode, b64decode
 
class Client(Security):
    def __init__(self):
        super().__init__()
        self.target = "127.0.0.1"
        self.port = 4444
        self.log_file = getcwd() + "\\Logs\\client_log.txt"
        self.buffer_size = 128

    def clear_screen(self):
        system("cls")

    def pause(self):
        system("pause")

    def print_and_log(self, data):
        with open(self.log_file, "a+", newline="\n") as log_file:
            log_file.write(f"{data}\n")
            print(data)

    def client_sender(self):
        try:
            while True:
                self.clear_screen()
            
                data_list = list() 
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                
                command = input("[#] Command > ")
                self.print_and_log(f"[#] Encrypting command - {command}")

                encrypted_data = self.generate_encrypted_data(command)
                self.print_and_log(f"\n[!] Encrypted data ({len(encrypted_data)} Bytes) - {encrypted_data}")
                
                # 344 bytes - RSA encrypted session key, After 344 bytes - iv & ciphertext
                client_socket.connect((self.target, self.port))
                client_socket.sendall(encrypted_data.encode(self.default_encoding))                
                client_socket.shutdown(socket.SHUT_WR)

                count = 1
                self.print_and_log(f"\n[*] Send & Receive buffer - ({self.buffer_size} Bytes)")
    
                while True:
                    data_block = client_socket.recv(self.buffer_size).decode(self.default_encoding)
                    self.print_and_log(f"[~] Data Block {count} ({len(data_block)} Bytes) - {data_block}")

                    if not data_block:
                        break

                    data_list.append(data_block)
                    count += 1

                received_data = ""

                for data in data_list:
                    received_data += data

                #self.print_and_log(f"\n[=] Data list - {data_list}")
                self.print_and_log(f"\n[=] Received data ({len(received_data)} Bytes) - {received_data}")

                decrypted_data = self.decrypt_received_data(received_data)

                if decrypted_data is None:
                    self.print_and_log(f"\n[>] Detected corruption on decrypted data - {decrypted_data}")

                else:
                    self.print_and_log(f"\n[>] Decrypted data ({len(decrypted_data)} Bytes):\n{decrypted_data}")

                self.pause()

        except KeyboardInterrupt:
            self.print_and_log(f"\n\n[!] Ctrl+C detected, exiting client.")

        except socket.error as socket_error:
            self.print_and_log(f"\n[!] Socket Error - {socket_error}")

        except Exception as error:
            self.print_and_log(f"\n[!] Error - {error}")

        finally:
            client_socket.close()

    def start(self):
        self.client_sender()
               
client = Client()
client.start()