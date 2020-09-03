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
        #self.default_encoding = 'utf-8'
        self.log_dir = getcwd() + "\\Logs\\"
        self.keywords_file = getcwd() + "\\keywords.txt"

        self.RED = Fore.RED
        self.GREEN = Fore.GREEN
        self.BLUE = Fore.BLUE
        self.CYAN = Fore.CYAN
        self.YELLOW = Fore.YELLOW
        self.MAGENTA = Fore.MAGENTA
        self.RESET = Fore.RESET

    def print_and_log(self, ip_src, url, method, user_agent, payload):
        data_for_print  = f"{self.CYAN}[{self.get_current_date} {self.get_current_time}] {self.MAGENTA}\"{ip_src}\" " 
        data_for_print += f"{self.GREEN}requested \"http://{url}\" with {method} method\n"
        data_for_print += f"{self.RED}User_Agent : {user_agent}\n"
        data_for_print += f"{self.YELLOW}Data : {payload}{self.RESET}\n"
                
        data_for_write  = f"[{self.get_current_date} {self.get_current_time}] \"{ip_src}\" " 
        data_for_write += f"requested \"http://{url}\" with {method} method\n"
        data_for_write += f"User_Agent : {user_agent}\n"
        data_for_write += f"Data : {payload}\n"

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
            #packet.show()

            # If packet is a http request, get the requested url
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()

            # Get the request method
            method = packet[HTTPRequest].Method.decode()

            # Get the user agent
            user_agent = packet[HTTPRequest].User_Agent.decode()

            # <IP  version=4 ihl=5 tos=0x0 len=719 id=1339 flags=DF frag=0 ttl=128 proto=tcp chksum=0x0 src=192.168.2.9 dst=176.28.50.165
            ip_src = packet[0].getlayer("IP").src

            if packet.haslayer(scapy.Raw):
                payload = packet[scapy.Raw].load.decode() 

                with open(self.keywords_file, "r") as kf:
                    keywords = kf.readlines()

                    for keyword in keywords:
                        if keyword.strip() in payload:
                            self.print_and_log(ip_src, url, method, user_agent, payload)
                            break

    def start(self):
        self.clear_screen()
        print(f"{self.RED}[+] Starting sniffer\n{self.RESET}")

        # iface: interface, store: tells scapy not to store packets in memory, prn: specify callback function
        scapy.sniff(iface=self.interface, store=False, prn=self.process_sniffed_packet)

if __name__ == "__main__":
    init()
    sniffer = Sniffer("Ethernet")   
    sniffer.start()