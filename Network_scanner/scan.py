import scapy.all as scapy
import argparse
import sys

from scapy.layers.l2 import *
from os import system
from colorama import init, Fore   

class Scanner:
    def __init__(self):
        self.ip_addr = None
        self.arp_request = None
        self.broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
        self.timeout_duration = 5

        self.red = Fore.RED
        self.green = Fore.GREEN 
        self.blue = Fore.BLUE
        self.cyan = Fore.CYAN
        self.yellow = Fore.YELLOW
        self.magenta = Fore.MAGENTA
        self.reset = Fore.RESET

        init()
        self.get_arguments()

    def validate_ip(self, ip_addr):
        octets = ip_addr.split('.')

        for octet in octets:
            try:
                # https://www.w3schools.com/python/ref_func_all.asp
                # len(octets) == 4 -> Check if format is a.b.c.d
                # 0 < len(octet) < 4 -> Check if each octet length in the range of 1-3
                # 0 <= int(part) < 256 -> Check if each octet value is in the range of 0-255
                return len(octets) == 4 and all((0 < len(octet) < 4) and (0 <= int(octet) < 256) for octet in octets)

            except ValueError:
                return False
            
            except (AttributeError, TypeError):
                return False

    def validate_subnetMask(self, subnet_mask):
        try:
            if len(subnet_mask) > 0 and len(subnet_mask) <= 3:
                if int(subnet_mask) >= 0 and int(subnet_mask) <= 32:
                    return True
                else:
                    return False
            else:
                return False

        except ValueError:
            return False

        except (AttributeError, TypeError):
            return False

    def get_arguments(self):
        parser = argparse.ArgumentParser(description='Discover hosts on a network.')
        parser.add_argument('-i', '--ip', required=True, help="format: 192.168.2.0/24 , ip_addr/mask")
        
        args = parser.parse_args()
        ip_from_args = args.ip

        if ip_from_args is None:
            parser.print_help()
            sys.exit(1)

        else:            
            try:
                ip_addr, subnet_mask = ip_from_args.split("/")  

                ip_validated = self.validate_ip(ip_addr)
                subnetMask_validated = self.validate_subnetMask(subnet_mask)

                if ip_validated and subnetMask_validated:
                    self.ip_addr = ip_from_args
                    self.arp_request = ARP(pdst=self.ip_addr)
                    self.scan()
                    sys.exit(0)
                
                elif ip_validated == False:
                    parser.print_help()
                    print(f"\nError: Check format of IP Address.")
                    sys.exit(1)

                elif subnetMask_validated == False:
                    parser.print_help()
                    print(f"\nError: Check format of Subnet Mask.")
                    sys.exit(1)

            except Exception as error:
                parser.print_help()
                print(f"\nError: Check the format of IP Address & Subnet Mask.  ")
                sys.exit(1)

    @property
    def arp_fields(self):
        return(scapy.ls(ARP()))

    @property
    def ethernet_fields(self):
        return(scapy.ls(Ether()))
    
    @property
    def arp_summary(self):
        return(self.arp_request.summary())

    @property
    def broadcast_summary(self):
        return(self.broadcast.summary())

    def clear_screen(self):
        system('cls')

    def print_output(self, packet_reply_dict):
        print(f"{self.yellow}+" + "-" * 48 + f"+{self.reset}")
        print(f"{self.yellow}|{self.reset}" + f"{self.cyan}%-24s{self.reset}" %(" IP Address") + f"{self.yellow}|{self.reset}" + f"{self.green}%-23s{self.reset}" %(f" Mac Address") + f"{self.yellow}|{self.reset}")
        print(f"{self.yellow}+" + "-" * 48 + f"+{self.reset}")
        
        for ip in packet_reply_dict:
            mac = packet_reply_dict.get(ip)
            print(f"{self.yellow}|{self.reset} {self.cyan}%-22s{self.reset} {self.yellow}|{self.reset} {self.green}%-21s{self.reset} {self.yellow}|{self.reset}" %(ip, mac))

        print(f"{self.yellow}+" + "-" * 48 + f"+{self.reset}")

    def scan(self):
        self.clear_screen()
        
        packet_reply_dict = dict()

        arp_request_broadcast = self.broadcast / self.arp_request
        answered_list, unanswered_list = srp(arp_request_broadcast, timeout=self.timeout_duration)

        self.clear_screen()

        for packet in answered_list:
            src_mac = packet[1].hwsrc
            src_ip = packet[1].psrc
            packet_reply_dict[src_ip] = src_mac

        self.print_output(packet_reply_dict)           

if __name__ == '__main__':
    scanner = Scanner()