import sys
from os import path, system, getcwd
from datetime import date, datetime
from scapy.layers.inet import IP, ICMP, sr1
from subprocess import Popen

class Utility:
    data_file = getcwd() + "\\servers.txt"
    log_file = getcwd() + "\\Logs\\log.txt"

    # Clear screen.
    @classmethod
    def clear_screen(cls):
        system('cls')

    # Prints data to screen and logs data at the same time.
    @classmethod
    def print_and_log(cls, data):
        with open(cls.log_file, "a+") as log_file:
            print(data)
            log_file.write(data + "\n")

    @classmethod
    def get_current_date(cls):
        today = date.today()
        todays_date = today.strftime("%d/%m/%Y")
        return todays_date

    @classmethod
    def get_current_time(cls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @classmethod
    def load_file(cls, filename):
        # Check if file exist and file is indeed a file.
        # If condition fails, exit program.
        if path.exists(filename) and path.isfile(filename):
            ip_list = open(filename, "r").readlines()
            ip_list = [ip.strip() for ip in ip_list]
            
            return ip_list

        else:
            print(f"[!] Unable to read {filename}")
            sys.exit(1)

    # Meat of the program. Only pings a single host. Output is logged and printed onto the screen.
    @classmethod
    def ping_ip(cls, ip):   
        # https://dev.to/ankitdobhal/let-s-ping-the-network-with-python-scapy-5g18 
        icmp = IP(dst = ip)/ICMP()

        cls.print_and_log("-" * 64)
        cls.print_and_log(f"{cls.get_current_date()} {cls.get_current_time()} - Testing connectivity on {ip}")
        
        response = sr1(icmp, timeout = 10)

        cls.print_and_log(f"\n{icmp.summary()}")

        if response == None:
            cls.print_and_log(f"\n[-] No response from {ip}.")

        else:
            cls.print_and_log(response.summary())
            cls.print_and_log(f"\n[+] {ip} is up.")

        cls.print_and_log("-" * 64 + "\n")

    @classmethod
    def ping(cls):
        cls.clear_screen()
        
        ip_list = cls.load_file(cls.data_file)

        [cls.ping_ip(ip) for ip in ip_list]

        # Opens results in notepad, proces.wait() ensures that notepad doesn't close right away.
        process = Popen(["notepad.exe", cls.log_file])
        process.wait()

if __name__ == "__main__":
    Utility.ping()