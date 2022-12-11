#!/usr/bin/env python3
import ipaddress
import argparse
import socket
import concurrent.futures
import os
from datetime import datetime

def saveOpenPorts(ip, saveDir):
    if saveDir != '':
        filename = f'{saveDir}/portscan-{ip}.txt'
    else:
        filename = f'portscan-{ip}.txt'

    openPorts.sort()

    with open(filename, 'w') as f:
        f.write(f'{ip}\n\n')

        for port in openPorts:
            f.write(f'{port} / tcp\n')

    print(f'Saved results to :: {filename}')

def scanPort(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f'[+] {port} is open.')
        openPorts.append(port)

    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP port scanner.')
    parser.add_argument('-d', '--dir', help='Directory to save results to.', required=True)
    parser.add_argument('-t', '--threads', help='Number of threads.', required=True)

    parseOpt = parser.add_mutually_exclusive_group(required=True)
    parseOpt.add_argument('-s', '--subnet', help='Subnet to scan.')
    parseOpt.add_argument('-f', '--filelist', help='File containing list of host(s)')
    
    args = parser.parse_args()
    saveDir = args.dir
    numOfThreads = args.threads

    datetimeFormat = "%d/%m/%Y %H:%M:%S"

    try:
        if args.subnet:
            # https://stackoverflow.com/questions/1942160/python-3-create-a-list-of-possible-ip-addresses-from-a-cidr-notation
            subnet = args.subnet
            ipList = ipaddress.ip_network(subnet)

            for ip in ipList.hosts():
                openPorts = list()

                print(f'\nTarget :: {ip}')
                print(f'Started scan at :: {str(datetime.now().strftime(datetimeFormat))}\n')

                with concurrent.futures.ThreadPoolExecutor(max_workers=int(numOfThreads)) as executor:
                    for port in range(1, 65535):
                        executor.submit(scanPort, str(ip), port)

                print(f'\nScan completed for {ip} at :: {str(datetime.now().strftime(datetimeFormat))}')

                if saveDir:
                    os.makedirs(saveDir, exist_ok=True)
                    saveOpenPorts(ip, saveDir)
                else:
                    saveOpenPorts(ip, '')

                openPorts.clear()

        elif args.filelist:
            fileList = args.filelist

            with open(fileList, 'r') as f:
                hostList = list(host.strip() for host in f.readlines())

            for ip in hostList:
                openPorts = list()

                print(f'\nTarget :: {ip}')
                print(f'Started scan at :: {str(datetime.now().strftime(datetimeFormat))}\n')

                with concurrent.futures.ThreadPoolExecutor(max_workers=int(numOfThreads)) as executor:
                    for port in range(1, 65535):
                        executor.submit(scanPort, ip, port)

                print(f'\nScan completed for {ip} at :: {str(datetime.now().strftime(datetimeFormat))}')

                if saveDir:
                    os.makedirs(saveDir, exist_ok=True)
                    saveOpenPorts(ip, saveDir)
                else:
                    saveOpenPorts(ip, '')

                openPorts.clear()

    except KeyboardInterrupt:
        print('\n[!] Exiting now.')

    except Exception as err:
        print(f'\n[!] {err}')
