#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def banner():
    intro = '''
    ██    ██  █████  ██      ██ ██████   █████  ████████  ██████  ██████  
    ██    ██ ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
    ██    ██ ███████ ██      ██ ██   ██ ███████    ██    ██    ██ ██████  
     ██  ██  ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
       ████   ██   ██ ███████ ██ ██████  ██   ██    ██     ██████  ██   ██ 
    '''
    print(intro)

def readFromFile():
    with open(hostListFile,'r') as f: return(f.readlines())

def saveValidHosts():
    valid.sort()

    with open(validfile, 'w') as vf:
        for valid_url in valid:
            vf.write(valid_url + "\n")

    print(f"[+] Written valid hosts to :: {validfile}")

def saveMaybeValidHosts():
    maybeValid.sort()

    with open(maybefile, 'w') as mf:
        for maybeValid_url in maybeValid:
            mf.write(maybeValid_url + "\n")

    print(f"[+] Written maybe valid hosts to :: {maybefile}")

def initiateRequest(url):
    try:
        response = requests.get(url, verify=False)
        responseCode = response.status_code
        print(f"{url} :: {responseCode}")

        if responseCode == 200:
            valid.append(url)
        else:
            maybeValid.append(url)

    except Exception as err:
        print(f"{url} :: {err}")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check list of hosts for HTTP 200 ok.')
    parser.add_argument("fileToRead", help="Enter file containing a list of hosts")
    parser.add_argument("-vf", "--validfile", help="File which contains a list of HTTP 200 ok hosts.", required=True)
    parser.add_argument("-mf", "--maybefile", help="File which contains a list of hosts where the response code isn't HTTP 200 ok.", required=True)

    valid = []
    maybeValid = []

    args = parser.parse_args()
    hostListFile = args.fileToRead
    urls = readFromFile()
    urlsStripped = [url.strip() for url in urls]
    validfile = args.validfile
    maybefile = args.maybefile

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for url in urlsStripped:
            url = f"https://{url}"
            executor.submit(initiateRequest, url)

    print()
    saveValidHosts()
    saveMaybeValidHosts()
