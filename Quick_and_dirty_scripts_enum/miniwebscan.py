#!/usr/bin/python3
from argparse import ArgumentParser
import nmap

def scan():
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sT -p80,443,8080,8443')

    for host in nm.all_hosts():
        linesep = '-' * 60

        print(linesep)
        print(f'Host: {host}')
        print(f'Hostname: {nm[host].hostname()}')
        print(f'State: {nm[host].state()}')
        print(linesep)

        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            print(linesep)

            lport = nm[host][proto].keys()

            for port in lport:
                print(f'port: {port}\tstate: {nm[host][proto][port]["state"]}')

if __name__ == "__main__":
    parser = ArgumentParser(description='Scan web servers using python3 nmap library.')
    parser.add_argument("-t", "--target", help="Target to scan.")
    args = parser.parse_args()

    target = args.target

    if target:
        scan()
    else:
        print("[!] No target provided.")
