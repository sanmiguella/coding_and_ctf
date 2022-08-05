#!/usr/bin/python3
import argparse
import socket
import concurrent.futures
import requests

def banner():
    intro = '''
     ██████  ███████ ████████ ██ ██████  
     ██       ██         ██    ██ ██   ██ 
     ██   ███ █████      ██    ██ ██████  
     ██    ██ ██         ██    ██ ██      
      ██████  ███████    ██    ██ ██      
    '''
    print(intro)

def readFromFile():
    with open(hostnameFileList,'r') as f: return(f.readlines())

def resolveHostname(hostname):
    try:
        ipv4 = socket.gethostbyname(hostname)
    except:
        ipv4 = 'NoIPv4'

    try:
        ipv6 = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
    except:
        ipv6 = 'NoIPv6'

    data = f"{hostname} | {ipv4} | {ipv6}"
    ipList.append(data)
    print(data)

def saveIP():
    ipList.sort()

    with open(outfile,'w') as ipFile:
        for result in ipList:
            ipFile.write(f"{result}\n")

    print(f"\nSaved results to {outfile}")

if __name__=="__main__":
    ipList = []

    parser = argparse.ArgumentParser(description="Get IPv4/IPv6 from file containing list of hostnames.")
    parser.add_argument("fileToRead", help="File containing a list of hostnames")
    parser.add_argument("-o", "--outfile", help="File to write results to", required=True)

    args = parser.parse_args()
    outfile = args.outfile
    hostnameFileList = args.fileToRead
    hostnames = readFromFile()
    strippedHostnames = [hostname.strip() for hostname in hostnames]

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for hostname in strippedHostnames:
            executor.submit(resolveHostname, hostname)

    saveIP()
