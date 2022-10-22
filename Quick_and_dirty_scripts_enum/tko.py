#!/usr/bin/python3
import dns.resolver
import requests
import concurrent.futures
import argparse
import sys

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def readFromFile(fileToRead):
    with open(fileToRead) as f: 
        return [line.strip() for line in f.readlines()]

def checkForSubTakeover(host):
    try:
        answers = dns.resolver.resolve(host, 'CNAME')
        cname = ''

        for rdata in answers: 
            cname += str(rdata)

        cnameResult = f'{answers.qname} - {cname} (CNAME)'
    except:
        cnameResult = f'{host} - NoCNAME'

    notFound = True
    try:
        res = requests.get(f'https://{host}',verify=False).text
        
        for fingerprint in fingerprintList:
            if fingerprint in res:
                msg = f'{host} | {cnameResult} | Fingerprint: "{fingerprint}"'
                takeover.append(msg)
                notFound = False
                break
        
        if notFound:
            msg = f'{host} | {cnameResult} | No fingerprint matched'
    except Exception as err:
        msg = f'Host: {host} | Error: {err}'
    finally:
        print(msg)

def saveToFile():
    if len(takeover) > 0:
        takeover.sort()

        with open(outfile,'w') as f:
            for result in takeover: 
                f.write(f'{result}\n')

        print(f'\n{len(takeover)} results saved...')
    else:
        print('\nNo results. Exiting program...')
        sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check list of hosts for subdomain takeover.')
    parser.add_argument('hostsFileToRead', help='File containing list of hosts.')
    parser.add_argument('-f', '--fingerprintFile', help='File containing fingerprints for subdomain takeover.', required=True)
    parser.add_argument('-t', '--threads', nargs='?', const=20, type=int, default=20,  help='Number of threads to use, default is 20.')
    parser.add_argument('-o', '--outfile', nargs='?', const='tko-results.txt', default='tko-results.txt',  help='File to write results to.')

    takeover = list()
    args = parser.parse_args()
    hostsList = readFromFile(args.hostsFileToRead)
    fingerprintList = readFromFile(args.fingerprintFile)
    outfile = args.outfile

    tr = args.threads

    print(f'Executing scan with {tr} threads.\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        for host in hostsList: 
            executor.submit(checkForSubTakeover, host)

    saveToFile()
