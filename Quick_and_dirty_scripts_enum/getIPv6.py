#!/usr/bin/python3
import argparse
import socket
import concurrent.futures
import uuid

ipv6_list = []

def banner():
    intro = '''
    ██ ██████  ██    ██  ██████      ██████  ███████ ███████  ██████  ██      ██    ██ ███████ ██████  
    ██ ██   ██ ██    ██ ██           ██   ██ ██      ██      ██    ██ ██      ██    ██ ██      ██   ██ 
    ██ ██████  ██    ██ ███████      ██████  █████   ███████ ██    ██ ██      ██    ██ █████   ██████  
    ██ ██       ██  ██  ██    ██     ██   ██ ██           ██ ██    ██ ██       ██  ██  ██      ██   ██ 
    ██ ██        ████    ██████      ██   ██ ███████ ███████  ██████  ███████   ████   ███████ ██   ██ 
    '''
    print(intro)

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def save_ipv6_list(filename):
    # Sort and save ipv6s in the list to a file
    ipv6_list.sort()

    with open(filename,'w') as ipv6_file:
        for ipv6 in ipv6_list:
            ipv6_file.write(f"{ipv6}\n")

    print(f"[+] Written file to {filename}")

def resolve_hostname(hostname):
    try:
        result = socket.getaddrinfo(hostname, 443, socket.AF_INET6)
        ipv6 = result[0][4][0]
        ipv6_list.append(f"{hostname} {ipv6}")
        print(f"{hostname} :: {ipv6}")

    except Exception as err:
        #print(f"{hostname} :: {err}")
        pass

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get IPv6 from hostname")
    parser.add_argument("file_to_read", help="Enter file containing a list of hostnames")

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor: 
        for hostname in stripped_hostnames:
            executor.submit(resolve_hostname, hostname)

    print(f"\n[+] IPv6 address count: {len(ipv6_list)}")
    prepend_filename = uuid.uuid4().hex
    filename = f"{prepend_filename}-ipv6_list.txt"
    save_ipv6_list(filename)
