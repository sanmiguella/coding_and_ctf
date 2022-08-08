#!/usr/bin/python3
import dns.resolver
import requests
import concurrent.futures
import argparse
import sys

def readFromFile(fileToRead):
    with open(fileToRead) as f: return([line.strip() for line in f.readlines()])

def checkForSubTakeover(host):
    try:
        answers = dns.resolver.resolve(host,'CNAME')
        cname = ''
        for rdata in answers: cname += str(rdata)
        cnameResult = f'{answers.qname} - {cname} (CNAME)'
    except:
        cnameResult = f'{host} - NoCNAME'

    notFound = True
    try:
        res = requests.get(f'https://{host}',verify=False).text
        
        for fingerprint in fingerprintList:
            if fingerprint in res:
                msg = f'Host: {host} | {cnameResult} | Fingerprint: "{fingerprint}"'
                takeover.append(msg)
                notFound = False
                break
        
        if notFound:
            msg = f'Host: {host} | {cnameResult} | No fingerprint matched'
   
        print(msg)
    except:
        pass

def saveToFile():
    if len(takeover) > 0:
        takeover.sort()

        with open(outfile,'w') as f:
            for result in takeover: f.write(f'{result}\n')

        print(f'\n{len(takeover)} results saved...')
    else:
        print('\nNo results. Exiting program...')
        sys.exit()

def showBanner():
    banner = '''
    ███████ ██    ██ ██████  ████████ ██   ██  ██████  
    ██      ██    ██ ██   ██    ██    ██  ██  ██    ██ 
    ███████ ██    ██ ██████     ██    █████   ██    ██ 
         ██ ██    ██ ██   ██    ██    ██  ██  ██    ██ 
    ███████  ██████  ██████     ██    ██   ██  ██████  
    '''
    print(banner)

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    showBanner()
    parser = argparse.ArgumentParser(description='Check list of hosts for subdomain takeover.')
    parser.add_argument('hostsFileToRead', help='File containing list of hosts.')
    parser.add_argument('-f', '--fingerprintFile', help='File containing fingerprints for subdomain takeover.',required=True)
    parser.add_argument('-t', '--threads', help='Number of threads to use, default is 10.')
    parser.add_argument('-o', '--outfile', help='File to write results to.',required=True)

    takeover = []
    args = parser.parse_args()
    hostsList = readFromFile(args.hostsFileToRead)
    fingerprintList = readFromFile(args.fingerprintFile)
    outfile = args.outfile

    tr = args.threads
    if tr is None: tr = 10
    else: tr = int(args.threads)

    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        print(f'Executing scan with {tr} threads.\n')
        for host in hostsList: executor.submit(checkForSubTakeover,host)

    saveToFile()
