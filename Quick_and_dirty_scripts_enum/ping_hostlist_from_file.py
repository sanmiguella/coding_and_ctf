#!/usr/bin/python3
import ipaddress
import argparse
import concurrent.futures
from ping3 import ping

def ping_host(host):
    try:
        response = ping(host, unit='ms')

        if (args.verbose):
            if response == False:
                print(f"[-] {host} :: Host unknown.")

            elif response == None:
                print(f"[-] {host} :: Timed out.")

            else:
                print(f"[*] Response from {host} :: {response} ms")
                responsive_hosts.append(host)

        else:
            if response != False and response != None:
                print(f"[*] Response from {host} :: {response} ms")
                responsive_hosts.append(host)

    except AttributeError:
        pass

    except Exception as err:
        print(f"[-] Response from {host} :: {err}")

def read_from_file(filename):
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data

def save_to_file(filename):
    with open(filename, 'w') as f:
        for host in responsive_hosts:
            f.write(host + '\n')

if __name__ == "__main__":
    responsive_hosts = []

    parser = argparse.ArgumentParser(description="Ping host list from file")
    parser.add_argument('-f', '--hostfile', help='Host file to read data from.', required=True)
    parser.add_argument('-o', '--outfile', help='Host file to write results to.', required=True)
    parser.add_argument('-v', '--verbose', help='Verbose output includes errors and timeouts.', action='store_true')

    args = parser.parse_args()

    hostList = read_from_file(args.hostfile)

    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        for host in hostList:
            executor.submit(ping_host, host)

    if len(responsive_hosts) > 0:
        print("\n[+] List of responsive hosts:")

        for host in responsive_hosts:
            print(host)

        print(f"\n[*] Saving results to {args.outfile}")
        save_to_file(args.outfile)
