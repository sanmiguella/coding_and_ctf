import socket
import threading
import sys, signal
import subprocess
import traceback

import concurrent.futures

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
        with open(self.log_file, "a+", newline="\n") as log_file:
            log_file.write(f"{data}\n")
            print(data)
    
    def clear_screen(self):
        system("cls")

    def receive_and_decrypt(self, client_socket):
        print(f"\n[*] Send & Recv buffer - ({self.buffer_size} Bytes)")

        data_list = list()
        count = 1
        received_data = ""
        
        while True:
            data_block = client_socket.recv(self.buffer_size).decode(self.default_encoding)
            self.print_and_log(f"[~] Data Block {count} ({len(data_block)} Bytes) - {data_block}")

            if not data_block:
                break

            data_list.append(data_block)
            count += 1

        for data in data_list:
            received_data += data

        self.print_and_log(f"\n[=] Received data ({len(received_data)} Bytes)- {received_data}")

        decrypted_data = self.decrypt_received_data(received_data)
        return decrypted_data

    def handle_remote_command(self, client_socket):
        try:
            decrypted_data = self.receive_and_decrypt(client_socket)

            if decrypted_data is None:
                self.print_and_log(f"\n[>] Detected corruption on decrypted data - {decrypted_data}")
                encrypted_reply = self.generate_encrypted_data("Corrupted")

            else:
                self.print_and_log(f"\n[>] Decrypted data ({len(decrypted_data)} Bytes) - {decrypted_data}")

                # https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
                command = decrypted_data
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.print_and_log(f"\n[X] Executing command - {command}")
                
                # If stdout is empty, it means that there's errors running the program.
                if result.stdout == b'':
                    result = result.stderr

                else: 
                    result = result.stdout

                encrypted_reply = self.generate_encrypted_data(result.decode(self.default_encoding))
                    
                client_socket.sendall(encrypted_reply.encode(self.default_encoding))
                self.print_and_log(f"\n[+] Sending back reply ({len(encrypted_reply)} Bytes) - {encrypted_reply}")

        except ConnectionResetError as connection_error:
            self.print_and_log(f"\n[!] Socket Error - {connection_error}")
        
        finally:
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()
            self.print_and_log(f"\n[#] Closed client connection.\n")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.clear_screen()
        self.print_and_log(f"[#] Server starting.")
        server.bind((self.bind_ip, self.bind_port))

        server.listen()
        self.print_and_log(f"[#] Listening on ({self.bind_ip} : {self.bind_port})")
        
        while True:
            try:
                client_socket, addr = server.accept()
                client_ip, client_port = addr

                self.print_and_log(f"\n[+] Connection accepted - ({client_ip} : {client_port})")
                
                '''
                thread_client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                thread_client_handler.start()
                '''

                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                    executor.submit(self.handle_remote_command, client_socket)

            except KeyboardInterrupt:
                self.print_and_log(f"\n[!] CTRL+C pressed, goodbye!")
                break

            except socket.error as socket_error:
                self.print_and_log(f"\n[!] Socket Error - {socket_error}")
        
            except Exception as error:
                self.print_and_log(f"\n[!] Error - {error}")

server = Server()
server.start()