#!/usr/bin/python3
import argparse
import sys
from ipwhois import IPWhois
#from pprint import pprint

def readFromFile(file_to_read):
    with open(file_to_read, 'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def performWhois(ip):
    # https://stackoverflow.com/questions/24580373/how-to-get-whois-info-by-ip-in-python-3
    obj = IPWhois(ip)
    res = obj.lookup_whois()
    #pprint(res)

    if simpleView:
        # Query | Cidr | Description | Asn
        data = f"{res['query']} | {res['nets'][0]['cidr']} | {res['nets'][0]['description']} | {res['asn']}\r\n"
    elif neatView:
        data  = f"Query: {res['query']}\r\n"
        data += f"Cidr: {res['nets'][0]['cidr']}\r\n"
        data += f"Description: {res['nets'][0]['description']}\r\n"
        data += f"Asn: {res['asn']}\r\n"

    print(data)
    return(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get whois data from IP address")
    parser.add_argument("file_to_read", help="File containing a list of IP addresses")
    parser.add_argument("-o", "--outfile", help="Output file to write results to", required=True)
    parser.add_argument("-s", "--simple", help="Simple view", action='store_true')
    parser.add_argument("-n", "--neat", help="Neat view", action='store_true')

    args = parser.parse_args()
    ipAddresses = readFromFile(args.file_to_read)
    ipList = [ipAddress.strip() for ipAddress in ipAddresses]
    outfile = args.outfile
    simpleView = args.simple
    neatView = args.neat

    if simpleView and neatView:
        print("\nEither -s or -n can be set, not both.\n")
        sys.exit()
    elif not simpleView and not neatView:
        print("\nPlease set either -s or -n.\n")
        sys.exit()

    with open(outfile, 'w') as f:
        for ip in ipList:
            try:
                dataToWrite = performWhois(ip)
                f.write(dataToWrite + "\r\n")

            except KeyboardInterrupt:
                print('\nExiting...\n')
                sys.exit()

            except Exception as err:
                print(f'\n{err}\n')
