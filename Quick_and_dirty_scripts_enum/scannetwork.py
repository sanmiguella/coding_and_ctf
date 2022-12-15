#!/usr/bin/env python3
import ipaddress
import argparse
import socket
import concurrent.futures
import os
import sys
from datetime import datetime

def saveOpenPorts(ip, saveDir):
    if saveDir != '':
        filename = f'{saveDir}/portscan-{ip}.txt'
    else:
        filename = f'portscan-{ip}.txt'

    ports = ', '.join(str(port) for port in openPorts)

    with open(filename, 'w') as f:
        f.write(f'host : {ip}\n')
        f.write(f'open : {ports}')

    print(f'Saved results to :: {filename}')

def scanPort(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f'[+] {port} is open.')
        openPorts.append(port)

    sock.close()

def startScan(ipList):
    for ip in ipList:
        print(f'\nTarget :: {ip}')
        print(f'Started scan at :: {str(datetime.now().strftime(datetimeFormat))}\n')

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            for port in range(1, 65535):
                executor.submit(scanPort, ip, port)

        print(f'\nScan completed for {ip} at :: {str(datetime.now().strftime(datetimeFormat))}')
        openPorts.sort()

        if saveDir:
            os.makedirs(saveDir, exist_ok=True)
            saveOpenPorts(ip, saveDir)
        else:
            saveOpenPorts(ip, '')

        openPorts.clear()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP port scanner.')
    parser.add_argument('-d', '--dir', help='Directory to save results to.', required=True)
    parser.add_argument('-t', '--threads', nargs='?', const=50, type=int, default=50, help='Number of threads. Default is 50.')

    parseOpt = parser.add_mutually_exclusive_group(required=True)
    parseOpt.add_argument('-s', '--subnet', help='Subnet to scan.')
    parseOpt.add_argument('-f', '--filelist', help='File containing list of host(s)')
    parseOpt.add_argument('-i', '--ip', nargs='+', help='Target IP(s) separated by spaces.')
    
    args = parser.parse_args()
    saveDir = args.dir
    numOfThreads = args.threads

    datetimeFormat = '%d/%m/%Y %H:%M:%S'
    openPorts = list()

    try:
        if args.subnet:
            # https://stackoverflow.com/questions/1942160/python-3-create-a-list-of-possible-ip-addresses-from-a-cidr-notation
            try:
                hostList = ipaddress.ip_network(args.subnet)
                ipList = list(str(ip) for ip in hostList.hosts())

            except Exception as err:
                print(f'[!] {err}')

            else:
                startScan(ipList)

        elif args.filelist:
            try:
                with open(args.filelist, 'r') as f:
                    ipList = list(host.strip() for host in f.readlines())

            except Exception as err:
                print(f'[!] {err}')

            else:
                try:
                    [ipaddress.ip_address(ip) for ip in ipList]
                
                except Exception as err:
                    print(f'[!] {err}')

                else:
                    startScan(ipList)

        elif args.ip:
            ipList = args.ip

            try:
                [ipaddress.ip_address(ip) for ip in ipList]

            except Exception as err:
                print(f'[!] {err}')

            else:
                startScan(ipList)

    except KeyboardInterrupt:
        print('\n[!] Exiting now.')
        sys.exit(1)
