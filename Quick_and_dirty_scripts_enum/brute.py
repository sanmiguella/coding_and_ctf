#!/usr/bin/python3
import requests
import argparse
import sys
import concurrent.futures
import dns.resolver

from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Scanner:
    def __init__(self, domainName, wordlist, threadsNum, outfile):
        self.domainName = domainName
        self.wordlist = wordlist
        self.threadsNum = threadsNum
        self.outfile = outfile
        self.timeout = 60
        self.found = []
        self.blacklistCode = [404,403]

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
            print(f"\n[>] Wrote results to {self.outfile}\n")

        finally:
            self.found.clear()

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

            if responseCode in self.blacklistCode:
                pass
            else:
                print(f"{url} -> {responseCode}")
                self.found.append(f"{url} {responseCode}")

    def scan(self):
        wordlist = self.readFile()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
            print()
            print(f"[+] Scanning {self.domainName} with {self.threadsNum} threads...")
            print(f"[+] Wordlists contains {len(wordlist)} entries.")
            print(f"[+] Output file - {self.outfile}")

            if command != "sub":
                print(f"[+] Blacklisted response code - {self.blacklistCode}\n")
            else:
                print()

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
            print(f"{subDomain}")
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

            print()
            print(f"[+] Scanning {host} with {self.threadsNum} threads...")
            print(f"[+] Wordlists contains {len(wordlist)} entries.")
            print(f"[+] Output file - {self.outfile}")
            print(f"[+] Blacklisted response code - {self.blacklistCode}\n")

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
                for fuzz in wordlist:
                    executor.submit(self.checkResponse, fuzz)

            self.writeFile()

class DnsScan(SubDomainScanner):
    def __init__(self, domainName, wordlist, threadsNum, outfile):
        super().__init__(domainName, wordlist, threadsNum, outfile)
        self.recordType_A = 'A'
        self.recordType_AAAA = 'AAAA'

    def checkResponse(self, fuzz):
        resolver = dns.resolver.Resolver() 
        subDomain = f"{fuzz}.{self.domainName}"

        resolvedToIPv4 = None
        resolvedToIPv6 = None

        try:
            resolvedToIPv4 = resolver.resolve(subDomain, self.recordType_A)[0]

        except:
            pass

        try:
            resolvedToIPv6 = resolver.resolve(subDomain, self.recordType_AAAA)[0]

        except:
            pass

        finally:
            if (resolvedToIPv4 is not None) or (resolvedToIPv6 is not None):
                print(f"{subDomain}")
                self.found.append(subDomain)

    def scan(self):
        wordlist = self.readFile()

        print()
        print(f"[+] Performing DNS enumeration with {self.threadsNum} threads...")
        print(f"[+] Wordlists contains {len(wordlist)} entries.")
        print(f"[+] Output file - {self.outfile}\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
            for fuzz in wordlist:
                executor.submit(self.checkResponse, fuzz)

        if self.outfile is not None:
            self.writeFile()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bruteforce file|dir|subdomain(s).")
    subParser = parser.add_subparsers(dest="command")

    dirScanParser = subParser.add_parser("dir", help="File|Dir bruteforcing.")
    dirScanParser.add_argument("-b", "--blacklist", help="Response code to blacklist. -b 200,302,etc")
    dirScanParser.add_argument("-w", "--wordlist", help="Wordlist.", required=True)
    dirScanParser.add_argument("-o", "--outfile", help="Writes results to file.")
    dirScanParser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Threads. Default is 10.")

    singleOrMassScanParser = dirScanParser.add_mutually_exclusive_group() 
    singleOrMassScanParser.add_argument("-f", "--hostfile", help="Host file format: https://test.com")
    singleOrMassScanParser.add_argument("-d", "--domain", help="Domain format: https://test.com")

    subScanParser = subParser.add_parser("sub", help="Subdomain bruteforcing.")
    subScanParser.add_argument("-d", "--domain", help="Domain format: test.com", required=True)
    subScanParser.add_argument("-w", "--wordlist", help="Wordlist.", required=True)
    subScanParser.add_argument("-o", "--outfile", help="Writes results to file.")
    subScanParser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Threads. Default is 10.")

    dnsScanParser = subParser.add_parser("dns", help="Dns bruteforcing.")
    dnsScanParser.add_argument("-d", "--domain", help="Domain forma: test.com", required=True)
    dnsScanParser.add_argument("-w", "--wordlist", help="Wordlist.", required=True)
    dnsScanParser.add_argument("-o", "--outfile", help="Writes results to file.")
    dnsScanParser.add_argument("-t", "--threads", nargs="?", const=10, type=int, default=10, help="Threads. Default is 10.")
    
    args = parser.parse_args()
    command = args.command

    if command == "dir" and (args.hostfile is not None):
        massBrute = MassDirBruteScan(args.domain, args.wordlist, args.threads, args.outfile, args.hostfile)

        if args.blacklist is not None:
            blacklistCodes = [int(code.strip()) for code in args.blacklist.split(",")]

            for code in blacklistCodes:
                massBrute.blacklistCode.append(code)

        massBrute.scan()

    elif command == "dir":
        dirBrute = Scanner(args.domain, args.wordlist, args.threads, args.outfile)

        if args.blacklist is not None:
            blacklistCodes = [int(code.strip()) for code in args.blacklist.split(",")]

            for code in blacklistCodes:
                dirBrute.blacklistCode.append(code)

        dirBrute.scan()

    elif command == "sub":
        subBrute = SubDomainScanner(args.domain, args.wordlist, args.threads, args.outfile)
        subBrute.scan()

    elif command == "dns":
       dnsBrute = DnsScan(args.domain, args.wordlist, args.threads, args.outfile) 
       dnsBrute.scan()

    else:
        parser.print_usage()
