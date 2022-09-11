#!/usr/bin/python3
import requests
import argparse
import concurrent.futures
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def readFromFile():
    with open(args.file,'r') as f:
        return(f.readlines())

def saveValidHosts():
    validCode.sort()

    with open(validOutputFile, 'w') as f:
        for result in validCode:
            f.write(f"{result}\n")

    print(f"\n[>] Written hosts that responded with http 200 to {validOutputFile}.")
    validCode.clear()

def saveOtherCodeHosts():
    otherCode.sort()

    with open(otherOutputFile, 'w') as f:
        for result in otherCode:
            f.write(f"{result}\n")

    print(f"[>] Written hosts that responded with other codes to {otherOutputFile}.")
    otherCode.clear()

def initRequest(url):
    domainName = urlparse(url).netloc

    try:
        response = requests.get(url, verify=False)
    except Exception as err:
        msg = f"{domainName} : {err}"
    else:
        resCode = response.status_code

        if resCode == 200:
            validCode.append(domainName)
        else:
            otherCode.append(f"{domainName} : {resCode}")
    finally:
        msg = f"{domainName} : {resCode}"
        print(msg)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check hosts that responds with HTTP 200 ok.')
    parser.add_argument("-f", "--file", help="Host file.", required=True)
    parser.add_argument("-vf", "--validOutputFile", nargs="?", const="vf.txt", default="vf.txt", help="Writes to file a list of HTTP 200 ok hosts. Default file is vf.txt.")
    parser.add_argument("-of", "--otherOutputFile", nargs="?", const="of.txt", default="of.txt", help="Writes to file a list of hosts where response code isn't HTTP 200. Default file is of.txt.")
    parser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10,  help="Threads. Default is 10.")

    validCode = []
    otherCode = []

    args = parser.parse_args()

    lines = readFromFile()
    urls = [line.strip() for line in lines]

    validOutputFile = args.validOutputFile
    otherOutputFile = args.otherOutputFile

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        print(f'[+] Executing scan with {args.threads} threads.\n')

        for url in urls:
            executor.submit(initRequest, f"https://{url}")

    saveValidHosts()
    saveOtherCodeHosts()
