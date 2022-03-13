#!/usr/bin/python3
import argparse
import socket
import concurrent.futures
import sys
from datetime import datetime

open_ports = []

def save_open_ports(target):
    filename = f"portscan-ipv6-{target}.txt"
    open_ports.sort()

    with open(filename,'w') as f:
        for port in open_ports:
           f.write(f"{port}\n")

    print(f"[+] Saved results to {filename}")

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open.")
        open_ports.append(port)

    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Host to perform port scan on.')
    parser.add_argument("target", help="IPv4 address of target")

    args = parser.parse_args()

    target = args.target
    target = target.strip()
    target = socket.getaddrinfo(target, None, socket.AF_INET6)[0][4][0]

    try:
        dt_format = "%d/%m/%Y %H:%M:%S"

        print(f"[+] Target :: {target}")
        print(f"[+] Started scan at :: {str(datetime.now().strftime(dt_format))}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for port in range(1, 65535):
                executor.submit(scan_port, target, port)

        print(f"[+] Scan completed at :: {str(datetime.now().strftime(dt_format))}")
        save_open_ports(target)

    except KeyboardInterrupt:
        print("[!] Exiting now.")
        sys.exit()

    except socket.gaierror as err:
        print(f"[!] Error :: {err}")
        sys.exit()

    except socket.error as err:
        print(f"[!] Error :: {err}")
        sys.exit()
