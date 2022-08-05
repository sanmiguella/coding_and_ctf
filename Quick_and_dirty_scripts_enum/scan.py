#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def banner():
    intro = '''
    ███████╗ ██████╗ █████╗ ███╗   ██╗
    ██╔════╝██╔════╝██╔══██╗████╗  ██║
    ███████╗██║     ███████║██╔██╗ ██║
    ╚════██║██║     ██╔══██║██║╚██╗██║
    ███████║╚██████╗██║  ██║██║ ╚████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
    '''
    print(intro)

def readFromFile():
    with open(hostListFile,'r') as f: return(f.readlines())

def saveValidHosts():
    validCode.sort()

    with open(validCodeFile,'w') as f:
        for result in validCode:
            f.write(f"{result}\n")

    print(f"Written hosts which responds with http 200 to {validCodeFile}")

def saveOtherCodeHosts():
    otherCode.sort()

    with open(otherCodeFile,'w') as f:
        for result in otherCode:
            f.write(f"{result}\n")

    print(f"Written hosts which responds with other codes to {otherCodeFile}")

def initRequest(url):
    try:
        response = requests.get(url,verify=False)
        responseCode = response.status_code

        strippedUrl = url.replace('https://','')
        print(f"{strippedUrl} : {responseCode}")

        if responseCode == 200:
            validCode.append(strippedUrl)
        else:
            otherCode.append(strippedUrl)

    except Exception as err:
        print(f"{strippedUrl} : {err}")

if __name__=="__main__":
    banner()
    parser = argparse.ArgumentParser(description='Check a list of hosts which responds with HTTP 200 code.')
    parser.add_argument("fileToRead", help="File containing a list of hosts.")
    parser.add_argument("-vf", "--validCodeFile", help="Writes to file a list of HTTP 200 ok hosts.", required=True)
    parser.add_argument("-of", "--otherCodeFile", help="Writes to file a list of hosts where response code isn't HTTP 200.", required=True)

    validCode = []
    otherCode = []

    args = parser.parse_args()
    hostListFile = args.fileToRead

    urls = readFromFile()
    urlsStripped = [url.strip() for url in urls]

    validCodeFile = args.validCodeFile
    otherCodeFile = args.otherCodeFile

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for url in urlsStripped:
            executor.submit(initRequest,f"https://{url}")

    saveValidHosts()
    saveOtherCodeHosts()
