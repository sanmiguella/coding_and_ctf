#!/usr/bin/env python3
import requests
import argparse
import sys
import concurrent.futures
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Scanner:
    def __init__(self, domainName, wordlist, threadsNum, outfile=None):
        self.domainName = domainName
        self.wordlist = wordlist
        self.threadsNum = threadsNum
        self.outfile = outfile
        self.validSubdomains = []

    # private method
    def __readFile(self):
        try:
            with open(self.wordlist, 'r') as f:
                data = [line.strip() for line in f.readlines()]
                return(data)
        except Exception as err:
            print(f"\n[!] {err}")
            sys.exit()

    def __writeFile(self):
        try:
            with open(self.outfile, 'w') as of:
                for sub in self.validSubdomains:
                    of.write(f"{sub}\n")
        except Exception as err:
            print(f"\n{err}")
        else:
            print(f"\n[+] Written file to {self.outfile}")

    def __checkIfSubDomainExists(self, sub):
        subDomain = f"https://{sub}.{self.domainName}"

        try:
            requests.get(subDomain, verify=False)
        except requests.ConnectionError:
            pass
        except Exception as err:
            print(f"[!] {err}")
        else:
            # When there are no errors
            print(f"Valid: {subDomain}")
            self.validSubdomains.append(f"{sub}.{self.domainName}")

    # public method
    def scan(self):
        subDomainsList = self.__readFile()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threadsNum) as executor:
            print(f"[+] Scanning {self.domainName} with {self.threadsNum} threads.")
            print(f"[+] Wordlists contains {len(subDomainsList)} entries.\n")

            for sub in subDomainsList:
                executor.submit(self.__checkIfSubDomainExists, sub)

        # Writes result only after scanning is done. However, it depends if the outfile argument is set
        if self.outfile is not None:
            self.__writeFile()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get valid subdomain(s) from a given domain name.")
    parser.add_argument("-d", "--domain", help="Domain name of target, for example, test.com", required=True)
    parser.add_argument("-w", "--wordlist", help="File containing list of words.", required=True)
    parser.add_argument("-o", "--outfile", help="File to save results to.")

    # https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    # nargs='?' -> 0 or 1 arguments
    # const=10 -> sets the default when there are 0 arguments
    # type=int -> converts the argument to int
    # default=10 -> sets threads to 10 even if no --threads is specified
    parser.add_argument("-t", "--threads", help="Number of threads to use, default is 10.", nargs='?', const=10, type=int, default=10)

    args = parser.parse_args()

    # https://stackoverflow.com/questions/30487767/check-if-argparse-optional-argument-is-set-or-not
    scan = Scanner(args.domain, args.wordlist, args.threads, args.outfile)
    scan.scan()
