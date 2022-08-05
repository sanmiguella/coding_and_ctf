#!/usr/bin/python3
import argparse
import sys
import re
import socket
import concurrent.futures
from ipwhois import IPWhois
#from pprint import pprint

def readFromFile():
    with open(hostListFile,'r') as f: return(f.readlines())

def performWhois(ip):
    # https://stackoverflow.com/questions/24580373/how-to-get-whois-info-by-ip-in-python-3
    obj = IPWhois(ip)
    res = obj.lookup_whois()
    #pprint(res)

    # https://stackoverflow.com/questions/275018/how-do-i-remove-a-trailing-newline#:~:text=You%20may%20use%20line%20%3D%20line,the%20string%2C%20not%20just%20one.
    regUnwanted = re.compile("[\r\n]")
    desc = res['nets'][0]['description']
    desc = regUnwanted.sub(" ", desc)

    if simpleView:
        # Query | Cidr | Description | Asn
        data = f"{res['query']} | {res['nets'][0]['cidr']} | {desc} | {res['asn']}"
    elif neatView:
        data  = f"Query: {res['query']}\n"
        data += f"Cidr: {res['nets'][0]['cidr']}\n"
        data += f"Description: {desc}\n"
        data += f"Asn: {res['asn']}\n"

    print(data)
    data += "\n"
    resultList.append(data)

def resolveIPv4(hostname):
    try:
        ipv4Addr = socket.gethostbyname(hostname)
        ipList.append(ipv4Addr)
    except:
        pass

def resolveIPv6(hostname):
    try:
        # https://stackoverflow.com/questions/15373288/python-resolve-a-host-name-with-ipv6-address
        ipv6Addr = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
        ipList.append(ipv6Addr)
    except:
        # Invalid hostnames will not appear in the ip list
        pass

def saveToFile():
    resultList.sort()
    with open(outfile,'w') as f:
        for result in resultList: f.write(result)

def showBanner():
    banner = '''
    ██╗      █████╗ ███████╗██╗   ██╗██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
    ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██║    ██║██║  ██║██╔═══██╗██║██╔════╝
    ██║     ███████║  ███╔╝  ╚████╔╝ ██║ █╗ ██║███████║██║   ██║██║███████╗
    ██║     ██╔══██║ ███╔╝    ╚██╔╝  ██║███╗██║██╔══██║██║   ██║██║╚════██║
    ███████╗██║  ██║███████╗   ██║   ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
    '''
    print(banner)

if __name__ == "__main__":
    showBanner()
    parser = argparse.ArgumentParser(description="Get whois data from a list of hostnames.")
    parser.add_argument("hostListFile", help="File containing a list of hostnames.")
    parser.add_argument("-o", "--outfile", help="Output file to write results to", required=True)
    parser.add_argument("-s", "--simple", help="Simple view", action='store_true')
    parser.add_argument("-n", "--neat", help="Neat view", action='store_true')
    parser.add_argument("-t", "--threads", help="Number of threads to use, default is 10.")

    args = parser.parse_args()
    hostListFile = args.hostListFile
    outfile = args.outfile
    simpleView = args.simple
    neatView = args.neat

    if simpleView and neatView:
        print("\nEither -s or -n can be set, not both.\n")
        sys.exit()
    elif not simpleView and not neatView:
        print("\nPlease set either -s or -n.\n")
        sys.exit()

    tr = args.threads
    if tr is None: tr = 10
    else: tr = int(tr)

    resultList = []
    ipList= []
    hosts = readFromFile()
    hostList = [host.strip() for host in hosts]

    print(f'Executing operations with {tr} threads.')

    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        print('Resolving hostnames to IPv4..')
        for host in hostList:
            executor.submit(resolveIPv4,host)

    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        print('Resolving hostnames to IPv6..\n')
        for host in hostList:
            executor.submit(resolveIPv6,host)

    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        for ip in ipList:
            executor.submit(performWhois,ip)

    print(f'\nSaving results to {outfile}.')
    saveToFile()
