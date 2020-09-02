import scapy.all as scapy

#from scapy.layers import http
#from scapy.layers.inet import IP, UDP, TCP, ICMP
from scapy.layers.http import HTTPRequest

from os import getcwd, system
from datetime import date, datetime
from colorama import init, Fore

class Sniffer:
    def __init__(self, interface):
        self.interface = interface
        self.default_encoding = 'utf-8'
        self.log_dir = getcwd() + "\\Logs\\"

        self.CYAN = Fore.CYAN
        self.GREEN = Fore.GREEN
        self.RED = Fore.RED
        self.BLUE = Fore.BLUE
        self.YELLOW = Fore.YELLOW
        self.RESET = Fore.RESET

    def print_and_log(self, url, method, packet):
        data_for_print = f"{self.CYAN}{self.get_current_date} {self.get_current_time} {self.GREEN}Requested {url} with {method}, {self.YELLOW}Data - {packet[scapy.Raw]}{self.RESET}"
        data_for_write = f"{self.get_current_date} {self.get_current_time} Requested {url} with {method}, Data - {packet[scapy.Raw].load}"

        log_file = self.log_dir + f"{self.get_current_date}.txt"
        with open(log_file, "a+", newline = "\n") as lf:
            lf.write(f"{data_for_write}\n")

        print(data_for_print)

    def clear_screen(self):
        system("cls")

    @property
    def get_current_date(self):
        today = date.today()
        today_date = today.strftime("%d-%m-%Y")
        return(today_date)      

    @property
    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return(current_time)  

    def process_sniffed_packet(self, packet):
        if packet.haslayer(HTTPRequest):
            # If packet is a http request, get the requested url
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()

            # Get the request method
            method = packet[HTTPRequest].Method.decode()

            if packet.haslayer(scapy.Raw):
                self.print_and_log(url, method, packet)

    def start(self):
        self.clear_screen()
        print(f"{self.RED}[+] Starting sniffer\n{self.RESET}")

        # iface: interface, store: tells scapy not to store packets in memory, prn: specify callback function
        scapy.sniff(iface=self.interface, store=False, prn=self.process_sniffed_packet, filter="port 80")

if __name__ == "__main__":
    init()
    sniffer = Sniffer("Ethernet")   
    sniffer.start()