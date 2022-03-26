#!/usr/bin/python3
import argparse
import socket
import concurrent.futures
import sys
import os
from datetime import datetime

def banner():
    intro = """
    ██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """
    print(intro)

def save_open_ports(target, odir):
    if odir != "":
        filename = f"{odir}/portscan-ipv4-{target}.txt"
    else:
        filename = f"portscan-ipv4-{target}.txt"

    open_ports.sort()

    with open(filename,'w') as f:
        f.write(f"{target}\n\n")

        for port in open_ports:
           f.write(f"{port} / tcp\n")

    print(f"Saved results to :: {filename}")

def scan_port(target, port, v6):
    if v6:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] {port} is open.")
        open_ports.append(port)

    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TCP port scanner.')
    parser.add_argument("-t", "--target", help="IP address of target.")
    parser.add_argument("-d", "--odir", help="Directory to save scans to.")
    parser.add_argument("-6", "--v6", help="IPv6 scan.", action="store_true")

    args = parser.parse_args()
    target = args.target
    odir = args.odir
    v6 = args.v6

    open_ports = []

    try:
        if target:
            target = target.strip()
        
            if v6:
                target = socket.getaddrinfo(target, None, socket.AF_INET6)[0][4][0]
            else:
                target = socket.gethostbyname(target)

            banner()
            dt_format = "%d/%m/%Y %H:%M:%S"

            print(f"Target :: {target}")
            print(f"Started scan at :: {str(datetime.now().strftime(dt_format))}\n")

            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                for port in range(1, 65535):
                    executor.submit(scan_port, target, port, v6)

            print(f"\nScan completed at :: {str(datetime.now().strftime(dt_format))}")

            if odir:    
                os.makedirs(odir, exist_ok=True)
                save_open_ports(target, odir)
            else:
                save_open_ports(target, "")

        else:
            parser.print_help()

    except KeyboardInterrupt:
        print("\n[!] Exiting now.")

    except Exception as err:
        print(f"\n[!] {err}")

    finally:
        sys.exit()
