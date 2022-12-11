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
    parser.add_argument('-s', '--subnet', help='Subnet to scan.')
    parser.add_argument('-d', '--dir', help='Directory to save results to.')
    parser.add_argument('-t', '--threads', help='Number of threads.')
    
    args = parser.parse_args()
    subnet = args.subnet
    saveDir = args.dir
    numOfThreads = args.threads

    # https://stackoverflow.com/questions/1942160/python-3-create-a-list-of-possible-ip-addresses-from-a-cidr-notation
    ipList = ipaddress.ip_network(subnet)

    datetimeFormat = "%d/%m/%Y %H:%M:%S"

    if subnet and saveDir and numOfThreads:
        try:
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

        except KeyboardInterrupt:
            print('\n[!] Exiting now.')

        except Exception as err:
            print(f'\n[!] {err}')
    else:
        parser.print_help()
