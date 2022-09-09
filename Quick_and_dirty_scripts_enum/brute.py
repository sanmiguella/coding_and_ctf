#!/usr/bin/python3
import requests
import argparse
import sys
import concurrent.futures
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Scanner:
    def __init__(self, domainName, wordlist, threadsNum, outfile):
        self.domainName = domainName
        self.wordlist = wordlist
        self.threadsNum = threadsNum
        self.outfile = outfile
        self.found = []
        self.showBanner()

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
            r = requests.get(url, verify=False)
        except requests.ConnectionError:
            pass
        except Exception as err:
            print(f"[!] {err}")
        else:
            if r.status_code == 404:
                pass
            else:
                print(f"{url} -> {r.status_code}")
                self.found.append(f"{url}")

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
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enumerate files/folders from a given domain name.")
    parser.add_argument("--dir", help="File/Directory BruteForcing.", action="store_true")
    parser.add_argument("--sub", help="SubDomain BruteForcing.", action="store_true")
    parser.add_argument("-d", "--domain", help="Domain name of target: 'https://test.com' for file/directory bruteforcing. 'test.com' for subdomain bruteforcing.", required=True)
    parser.add_argument("-w", "--wordlist", help="Wordlist containing file(s)/folder(s).", required=True)
    parser.add_argument("-o", "--outfile", help="File to save results to.")
    parser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Number of threads to use, default is 10.")
    
    args = parser.parse_args()

    dirScan = args.dir
    subScan = args.sub

    if dirScan and subScan:
        print("\n[!] Choose either File/Directory or SubDomain bruteforcing.")
    elif dirScan:
        dirBrute = Scanner(args.domain, args.wordlist, args.threads, args.outfile)
        dirBrute.scan()
    elif subScan:
        subBrute = SubDomainScanner(args.domain, args.wordlist, args.threads, args.outfile)
        subBrute.scan()
    else:
        parser.print_usage()
