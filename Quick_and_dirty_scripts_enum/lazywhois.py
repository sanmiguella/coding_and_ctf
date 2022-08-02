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

    data  = f"Description: {res['nets'][0]['description']} - {res['query']}\r\n"
    data += f"Asn: {res['asn']}\r\n"
    data += f"Cidr: {res['nets'][0]['cidr']}\r\n"

    print(data)
    return(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get whois data from IP address")
    parser.add_argument("file_to_read", help="File containing a list of IP addresses")
    parser.add_argument("-o", "--outfile", help="Output file to write results to", required=True)

    args = parser.parse_args()
    ipAddresses = readFromFile(args.file_to_read)
    ipList = [ipAddress.strip() for ipAddress in ipAddresses]
    outfile = args.outfile

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
