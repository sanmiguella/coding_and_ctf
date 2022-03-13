#!/usr/bin/python3
import ipaddress
import argparse
import concurrent.futures
from ping3 import ping

responsive_hosts = []

def banner():
    intro = """
    ██████  ██ ███    ██  ██████      ███████ ██     ██ ███████ ███████ ██████  ███████ ██████  
    ██   ██ ██ ████   ██ ██           ██      ██     ██ ██      ██      ██   ██ ██      ██   ██ 
    ██████  ██ ██ ██  ██ ██   ███     ███████ ██  █  ██ █████   █████   ██████  █████   ██████  
    ██      ██ ██  ██ ██ ██    ██          ██ ██ ███ ██ ██      ██      ██      ██      ██   ██ 
    ██      ██ ██   ████  ██████      ███████  ███ ███  ███████ ███████ ██      ███████ ██   ██ 
    """
    print(intro)

def save_hosts_to_file(save_file):
    with open(save_file,'w') as sf:
        for host in responsive_hosts:
            sf.write(f"{host}\n")

    print(f"\n[+] Saved file to {save_file}")

def ping_host(host):
    try:
        response = ping(host, unit='ms')

        if response == False:
            print(f"{host} :: Host unknown.")
        elif response == None:
            print(f"{host} :: Timed out.")
        else:
            print(f"Response from {host} :: {response} ms")
            responsive_hosts.append(host)

    except AttributeError:
        pass

    except Exception as err:
        print(f"Response from {host} :: {err}")

if __name__ == "__main__":
    ipv4_subnet = []

    parser = argparse.ArgumentParser(description="Ping legacy ipv4 network")
    parser.add_argument("ipv4_subnet", help="Enter CIDR, ex 192.168.2.0/24")

    args = parser.parse_args()
    ipv4_subnet = args.ipv4_subnet
    ipv4_hosts = [str(ip).strip() for ip in ipaddress.IPv4Network(ipv4_subnet)]
  
    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for host in ipv4_hosts:
            executor.submit(ping_host, host)

    print("\n[+] List of responsive hosts:")
    for host in responsive_hosts:
        print(host)

    save_hosts_to_file(f"ipv4_hosts.txt")
