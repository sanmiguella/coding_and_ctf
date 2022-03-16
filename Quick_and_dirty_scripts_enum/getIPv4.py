#!/usr/bin/python3
import argparse
import socket
import concurrent.futures

ipv4_list = []

def banner():
    intro = '''
    ██ ██████  ██    ██ ██   ██     ██████  ███████ ███████  ██████  ██      ██    ██ ███████ ██████  
    ██ ██   ██ ██    ██ ██   ██     ██   ██ ██      ██      ██    ██ ██      ██    ██ ██      ██   ██ 
    ██ ██████  ██    ██ ███████     ██████  █████   ███████ ██    ██ ██      ██    ██ █████   ██████  
    ██ ██       ██  ██       ██     ██   ██ ██           ██ ██    ██ ██       ██  ██  ██      ██   ██ 
    ██ ██        ████        ██     ██   ██ ███████ ███████  ██████  ███████   ████   ███████ ██   ██
    '''
    print(intro)

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def resolve_hostname(hostname):
    try:
        ipv4 = socket.gethostbyname(hostname)
        ipv4_list.append(f"{hostname} {ipv4}")
        print(f"{hostname} :: {ipv4}")

    except Exception as err:
        #print(f"{hostname} :: {err}")
        pass

def save_ipv4_list(filename):
    # Sort and save ipv4s in the list to a file
    ipv4_list.sort()

    with open(filename,'w') as ipv4_file:
        for host in ipv4_list:
            ipv4_file.write(f"{host}\n")

    print(f"\n[+] Saved file to {filename}")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get IPv4 from hostname")
    parser.add_argument("file_to_read", help="File containing a list of hostnames")
    parser.add_argument("-o", "--outfile", help="Output file to write results to", required=True)

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]
    outfile = args.outfile

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for hostname in stripped_hostnames:
            executor.submit(resolve_hostname, hostname)

    print(f"\n[+] IPv4 address count: {len(ipv4_list)}")
    save_ipv4_list(outfile)
