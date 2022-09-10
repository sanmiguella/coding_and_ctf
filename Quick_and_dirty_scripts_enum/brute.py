#!/usr/bin/python3
import requests
import argparse
import sys
import concurrent.futures
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Scanner:
    def __init__(self, domainName, wordlist, threadsNum, outfile):
        self.domainName = domainName
        self.wordlist = wordlist
        self.threadsNum = threadsNum
        self.outfile = outfile
        self.found = []
        self.showBanner()
        self.timeout = 60

    def showBanner(self):
        msg = '''
██████  ██████  ██    ██ ████████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██      
██████  ██████  ██    ██    ██    █████   
██   ██ ██   ██ ██    ██    ██    ██      
██████  ██   ██  ██████     ██    ███████
'''
        print(msg)

    def readFile(self):
        try:
            with open(self.wordlist, 'r') as f:
                data = [line.strip() for line in f.readlines()]
        except Exception as err:
            print(f"\n[!] {err}")
            sys.exit()
        else:
            return(data)

    def writeFile(self):
        try:
            with open(self.outfile, 'w') as of:
                for found in self.found:
                    of.write(f"{found}\n")
        except Exception as err:
            print(f"\n[!] {err}")
        else:
            print(f"\n[+] Written file to {self.outfile}")

    def checkResponse(self, fuzz):
        try:
            url = f"{self.domainName}/{fuzz}"
            r = requests.get(url, timeout=self.timeout, verify=False)
        except requests.ConnectionError:
            pass
        except Exception as err:
            print(f"[!] {err}")
        else:
            responseCode = r.status_code

            if responseCode == 404 or responseCode == 403:
                pass
            else:
                print(f"{url} -> {responseCode}")
                self.found.append(f"{url} {responseCode}")

    def scan(self):
        wordlist = self.readFile()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
            print(f"[+] Scanning {self.domainName} with {self.threadsNum} threads...")
            print(f"[+] Wordlists contains {len(wordlist)} entries.")
            print(f"[+] Save results - {self.outfile}\n")

            for fuzz in wordlist:
                executor.submit(self.checkResponse, fuzz)

        if self.outfile is not None:
            self.writeFile()

        self.found.clear()

class SubDomainScanner(Scanner):
    def __init__(self, domainName, wordlist, threadsNum, outfile):
        super().__init__(domainName, wordlist, threadsNum, outfile)

    def checkResponse(self, fuzz):
        try:
            subDomain = f"https://{fuzz}.{self.domainName}"
            requests.get(subDomain, verify=False)
        except requests.ConnectionError:
            pass
        except Exception as err:
            print(f"[!] {err}")
        else:
            print(f"Valid: {subDomain}")
            self.found.append(f"{fuzz}.{self.domainName}")

class MassDirBruteScan(Scanner):
    def __init__(self, domainName, wordlist, threadsNum, outfile, hostfile):
        super().__init__(domainName, wordlist, threadsNum, outfile)
        self.hostfile = hostfile
        self.domainName = None

    def readFile(self, fileToRead):
        try:
            with open(fileToRead, 'r') as f:
                data = [line.strip() for line in f.readlines()]
        except Exception as err:
            print(f"\n[!] {err}")
            sys.exit()
        else:
            return(data)

    def scan(self):
        wordlist = self.readFile(self.wordlist)
        hostfile = self.readFile(self.hostfile)

        for host in hostfile:
            self.domainName = host
            self.outfile = f"{urlparse(host).netloc}.txt"

            print(f"[+] Scanning {host} with {self.threadsNum} threads...")
            print(f"[+] Wordlists contains {len(wordlist)} entries.")
            print(f"[+] Save results - {self.outfile}\n")

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
                for fuzz in wordlist:
                    executor.submit(self.checkResponse, fuzz)

            self.writeFile()
            self.found.clear()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enumerate files/folders from a given domain name.")
    parser.add_argument("--dir", help="File/Directory BruteForcing.", action="store_true")
    parser.add_argument("--hostfile", help="List of hosts to perform File/Directory BruteForcing on.")
    parser.add_argument("--sub", help="SubDomain BruteForcing.", action="store_true")
    parser.add_argument("-d", "--domain", help="Domain name of target: 'https://test.com' for file/directory bruteforcing. 'test.com' for subdomain bruteforcing.")
    parser.add_argument("-w", "--wordlist", help="Wordlist containing file(s)/folder(s).", required=True)
    parser.add_argument("-o", "--outfile", help="File to save results to.")
    parser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Number of threads to use, default is 10.")
    
    args = parser.parse_args()

    dirScan = args.dir
    subScan = args.sub

    if dirScan and subScan:
        print("\n[!] Choose either File/Directory or SubDomain bruteforcing.")
    elif dirScan and (args.hostfile is not None):
        massBrute = MassDirBruteScan(args.domain, args.wordlist, args.threads, args.outfile, args.hostfile)
        massBrute.scan()
    elif dirScan:
        dirBrute = Scanner(args.domain, args.wordlist, args.threads, args.outfile)
        dirBrute.scan()
    elif subScan:
        subBrute = SubDomainScanner(args.domain, args.wordlist, args.threads, args.outfile)
        subBrute.scan()
    else:
        parser.print_usage()
