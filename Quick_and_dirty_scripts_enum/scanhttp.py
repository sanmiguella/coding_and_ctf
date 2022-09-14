#!/usr/bin/python3
import requests
import argparse
import concurrent.futures
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class HttpScan:
    def __init__(self, file, validOutputFile, otherOutputFile, threads):
        self.file = file
        self.validOutputFile = validOutputFile
        self.otherOutputFile = otherOutputFile 
        self.threads = threads
        self.validResults = list()
        self.otherResults = list()

    def readFromFile(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()

        data = [line.strip() for line in lines]
        return(data)
            
    def saveValidResults(self):
        self.validResults.sort()

        with open(self.validOutputFile, 'w') as f:
            f.writelines("%s\n" % result for result in self.validResults)

        print(f"\n[>] Written hosts that responded with http 200 to {self.validOutputFile}.")
        self.validResults.clear()

    def saveOtherResults(self):
        self.otherResults.sort()

        with open(self.otherOutputFile, 'w') as f:
            f.writelines("%s\n" % result for result in self.otherResults)

        print(f"[>] Written hosts that responded with other codes to {self.otherOutputFile}.")
        self.otherResults.clear()

    def checkResponse(self, url):
        domainName = urlparse(url).netloc

        try:
            res = requests.get(url, verify=False)

        except Exception as err:
            msg = f"{domainName} : {err}"

        else:
            resCode = res.status_code

            if resCode == 200:
                self.validResults.append(domainName)

            else:
                self.otherResults.append(f"{domainName} : {resCode}")

        finally:
            output = f"{domainName} : {resCode}"
            print(output)
    
    def scan(self):
        urls = self.readFromFile()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            print(f'[+] Executing scan with {self.threads} threads.\n')

            for url in urls:
                url = f"https://{url}"
                executor.submit(self.checkResponse, url)

        self.saveValidResults()
        self.saveOtherResults()
 
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check hosts that responds with HTTP 200 ok.')
    parser.add_argument("-f", "--file", help="Host file.", required=True)
    parser.add_argument("-vf", "--validOutputFile", nargs="?", const="vf.txt", default="vf.txt", help="Writes to file a list of HTTP 200 ok hosts. Default file is vf.txt.")
    parser.add_argument("-of", "--otherOutputFile", nargs="?", const="of.txt", default="of.txt", help="Writes to file a list of hosts where response code isn't HTTP 200. Default file is of.txt.")
    parser.add_argument("-t", "--threads", nargs="?", const=20, type=int, default=20,  help="Threads. Default is 20.")
    args = parser.parse_args()

    scanner = HttpScan(args.file, args.validOutputFile, args.otherOutputFile, args.threads)
    scanner.scan()
