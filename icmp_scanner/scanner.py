import socket
import threading

from os import system, name
from time import sleep
from struct import pack
from netaddr import IPNetwork, IPAddress
from ctypes import *
from colorama import init, Fore

class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ushort),
        ("unused", c_ushort),
        ("next_hop_mtu", c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)
    
    def __init__(self, socket_buffer):
        pass

# IP header: 20 bytes
class IP(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        ("src", c_ulong),
        ("dst", c_ulong)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # Map protocol constants to their names. 
        self.protocol_map = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        # Human readable IP addresses.
        self.src_addr = socket.inet_ntoa(pack("<L", self.src))
        self.dst_addr = socket.inet_ntoa(pack("<L", self.dst))

        # Human readable protocol.
        try:
            self.protocol = self.protocol_map.get(self.protocol_num)
        except:
            self.protocol = str(self.protocol_num)

class Prettify:
    def __init__(self):
        self.red = Fore.RED
        self.green = Fore.GREEN 
        self.blue = Fore.BLUE
        self.cyan = Fore.CYAN
        self.yellow = Fore.YELLOW
        self.magenta = Fore.MAGENTA
        self.reset = Fore.RESET
        init()  

# ICMP Type 3: Destination unreachable
# ICMP Code 3: Port unreachable
class Scanner(Prettify):
    def __init__(self, subnet):
        super().__init__()
        self.subnet = subnet
        self.unreachable_port = 65212
        self.magic_message = b"MR ROBOT"
        self.sleep_time = 5

    def short_pause(self):
        sleep(self.sleep_time)

    def start_scanning(self):
        sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # SOCK_DGRAM: UDP
        for ip in IPNetwork(self.subnet):
            try:
                # https://netaddr.readthedocs.io/en/latest/tutorial_01.html
                ip = str(ip) 
                sender.sendto(self.magic_message, (ip, self.unreachable_port))
                #print(f"[#] Sending magic message to \"{ip}\"")
            
            except Exception as error:
                print(f"[!] Error - {error}")
        
class Sniffer(Scanner):
    def __init__(self, listen_addr, subnet):
        super().__init__(subnet)
        self.listen_addr = listen_addr
        self.socket_proto = ""
        self.buf_size = 65565

    def clear_screen(self):
        system("cls")

    def start_host_discovery(self):
        self.clear_screen()

        os_version = name

        if os_version == "nt": 
            self.socket_proto = socket.IPPROTO_IP
        else: 
            self.socket_proto = socket.IPPROTO_ICMP

        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, self.socket_proto)
        sniffer.bind((self.listen_addr, 0))

        # IP headers to be included in capture.
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # In windows, need to send an IOCTL to setup promiscuous mode.
        if os_version == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        t_network_scan = threading.Thread(target = self.start_scanning)
        t_network_scan.start()

        try:
            while True:
                # Read in a packet.
                raw_buf = sniffer.recvfrom(self.buf_size)[0]

                # IP header bit offset: 0-120 bits(20 bytes)
                # Create ip header from first 20 bytes of buffer.
                ip_header = IP(raw_buf[0:20])

                if ip_header.protocol == "ICMP":
                    # Calculate where ICMP packet starts.
                    offset = ip_header.ihl * 4

                    # ICMP size - 8 Bytes.
                    buf = raw_buf[offset : offset + sizeof(ICMP)]

                    # Create ICMP structure.
                    icmp_header = ICMP(buf)

                    # ICMP Type 3: Destination unreachable
                    # ICMP Code 3: Port unreachable
                    if icmp_header.type == 3 and icmp_header.code == 3:
                        # Make sure host is in target subnet.
                        if IPAddress(ip_header.src_addr) in IPNetwork(self.subnet):
                            # Data in the ICMP packet.
                            data = raw_buf[len(raw_buf) - len(self.magic_message) : ]

                            if data == self.magic_message:
                                # Make sure packet has our magic message.
                                print(f"{self.magenta}[>] {self.red}{ip_header.src_addr} {self.cyan} -> {self.green} {ip_header.dst_addr}{self.reset}")
                                print(f"{self.magenta}[+] {self.yellow}ICMP data: {self.cyan}{data.decode()}\n{self.reset}")

        except KeyboardInterrupt:
            # For windows, turn promiscuous mode off.
            if os_version == "nt":
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

sniffer = Sniffer("192.168.2.9", "192.168.2.0/24")
sniffer.start_host_discovery()