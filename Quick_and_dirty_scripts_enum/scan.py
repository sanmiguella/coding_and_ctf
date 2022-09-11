#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def readFromFile():
    with open(hostListFile,'r') as f: return(f.readlines())

def saveValidHosts():
    validCode.sort()

    with open(validCodeFile,'w') as f:
        for result in validCode: f.write(f"{result}\n")

    print(f"Written hosts which responds with http 200 to {validCodeFile}")
    validCode.clear()

def saveOtherCodeHosts():
    otherCode.sort()

    with open(otherCodeFile,'w') as f:
        for result in otherCode: f.write(f"{result}\n")

    print(f"Written hosts which responds with other codes to {otherCodeFile}")
    otherCode.clear()

def initRequest(url):
    strippedUrl = url.replace('https://','')

    try:
        response = requests.get(url, verify=False)
        responseCode = response.status_code

        if responseCode == 200: 
            validCode.append(strippedUrl)
        else: 
            msg = f"{strippedUrl} : {responseCode}"
            otherCode.append(msg)
    except Exception as err:
        msg = f"{strippedUrl} : {err}"
    finally:
        print(msg)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check a list of hosts which responds with HTTP 200 code.')
    parser.add_argument("fileToRead", help="File containing a list of hosts.")
    parser.add_argument("-vf", "--validCodeFile", help="Writes to file a list of HTTP 200 ok hosts.", required=True)
    parser.add_argument("-of", "--otherCodeFile", help="Writes to file a list of hosts where response code isn't HTTP 200.", required=True)
    parser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Number of threads, default is 10.")

    validCode = []
    otherCode = []

    args = parser.parse_args()
    hostListFile = args.fileToRead

    urls = readFromFile()
    urlsStripped = [url.strip() for url in urls]

    validCodeFile = args.validCodeFile
    otherCodeFile = args.otherCodeFile

    tr = args.threads

    with concurrent.futures.ThreadPoolExecutor(max_workers=tr) as executor:
        print(f'Executing scan with {tr} threads.\n')
        for url in urlsStripped: executor.submit(initRequest,f"https://{url}")

    print()
    saveValidHosts()
    saveOtherCodeHosts()
