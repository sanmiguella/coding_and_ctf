import socket
import threading
import sys, signal
import subprocess

from os import getcwd, system
from Security import Security
from base64 import b64encode, b64decode

class Server(Security):
    def __init__(self):
        super().__init__()
        self.bind_ip = "127.0.0.1"
        self.bind_port = 4444
        self.log_file = getcwd() + "\\Logs\\server_log.txt"
        self.buffer_size = 128

    def print_and_log(self, data):
        with open(self.log_file, "a+") as log_file:
            log_file.write(f"{data}\n")
            print(data)
    
    def clear_screen(self):
        system("cls")

    def handle_client(self, client_socket):
        data_list = list()
        count = 1
        received_data = ""

        try:
            print(f"\n[*] Send & Recv buffer - ({self.buffer_size} Bytes)")

            while True:
                data_block = client_socket.recv(self.buffer_size).decode(self.default_encoding)
                self.print_and_log(f"[~] Data Block {count} ({len(data_block)} Bytes) - {data_block}")

                if not data_block:
                    break

                client_socket.sendall(received_data.encode(self.default_encoding))
                data_list.append(data_block)
                count += 1

            for data in data_list:
                received_data += data

            self.print_and_log(f"\n[=] Data list - {data_list}")
            self.print_and_log(f"[=] Received data ({len(received_data)} Bytes)- {received_data}")

            decrypted_data = self.decrypt_received_data(received_data)

            if decrypted_data is None:
                self.print_and_log(f"\n[>] Detected corruption on decrypted data - {decrypted_data}")
                encrypted_reply = self.generate_encrypted_data("Corrupted")

            else:
                self.print_and_log(f"\n[>] Decrypted data ({len(decrypted_data)} Bytes) - {decrypted_data}")

                try:
                    command = decrypted_data
                    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
                    result = result.stdout

                except Exception as error:
                    result = f"{error}\n".encode(self.default_encoding)

            encrypted_reply = self.generate_encrypted_data(result.decode(self.default_encoding))
              
            client_socket.sendall(encrypted_reply.encode(self.default_encoding))
            self.print_and_log(f"\n[+] Sending back reply ({len(encrypted_reply)} Bytes) - {encrypted_reply}")

            client_socket.close()
            self.print_and_log(f"\n[#] Closed client connection.")

        except ConnectionResetError as error:
            self.print_and_log(f"\n[!] Connection Reset Error - {error}")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.clear_screen()
        self.print_and_log(f"[#] Server starting.")
        server.bind((self.bind_ip, self.bind_port))

        server.listen()
        self.print_and_log(f"[#] Listening on ({self.bind_ip} : {self.bind_port})")
        
        while True:
            try:
                client, addr = server.accept()
                client_ip, client_port = addr

                self.print_and_log(f"\n[+] Connection accepted - ({client_ip} : {client_port})")
                client_handler = threading.Thread(target=self.handle_client, args=(client,))
                client_handler.start()
            
            except KeyboardInterrupt:
                self.print_and_log(f"\n[!] CTRL+C pressed, goodbye!")
                break

            except socket.error as socket_error:
                self.print_and_log(f"\n[!] Socket Error - {socket_error}")
        
            except Exception as error:
                self.print_and_log(f"\n[!] Error - {error}")

server = Server()
server.start()