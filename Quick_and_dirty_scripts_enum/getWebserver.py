#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

def getWebserver(hostname):
    try:
        r = requests.get(f"https://{hostname}")
        webServer = r.headers['Server']
        data = f"{hostname} : {webServer}"
        print(data)
        data += "\n"

    except Exception as err :
        if verbose:
            data = f"{hostname} - {err}"
            print(data)
            data += "\n"

    finally:
       resultsList.append(data) 

def readFromFile():
    with open(hostListFile,'r') as f: return(f.readlines())

def saveToFile():
    with open(outfile,'w') as f: 
        for result in resultsList:
            f.write(result)

def showBanner():
    banner = '''
     ██████  ███████ ████████ ██     ██ ███████ ██████  ███████ ███████ ██████  ██    ██ ███████ ██████  
     ██       ██         ██    ██     ██ ██      ██   ██ ██      ██      ██   ██ ██    ██ ██      ██   ██ 
     ██   ███ █████      ██    ██  █  ██ █████   ██████  ███████ █████   ██████  ██    ██ █████   ██████  
     ██    ██ ██         ██    ██ ███ ██ ██      ██   ██      ██ ██      ██   ██  ██  ██  ██      ██   ██ 
      ██████  ███████    ██     ███ ███  ███████ ██████  ███████ ███████ ██   ██   ████   ███████ ██   ██ 
    '''
    print(banner)

if __name__ == "__main__":
    showBanner()
    parser = argparse.ArgumentParser(description="Get webserver name/version from list of hostnames.")
    parser.add_argument("hostListFile", help="File containing a list of hostnames.")
    parser.add_argument("-o", "--outfile", help="File to write results to.")
    parser.add_argument("-v", "--verbose", help="Show errors.", action='store_true')

    args = parser.parse_args()
    outfile = args.outfile
    verbose = args.verbose

    hostListFile = args.hostListFile
    hosts = readFromFile()
    hostList = [host.strip() for host in hosts]
    resultsList = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for host in hostList:
            executor.submit(getWebserver, host)

    saveToFile()
