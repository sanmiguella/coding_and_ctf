#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import argparse
import concurrent.futures
import re
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def save_wordpress_sites(filename):
    wordpress_sites.sort() 

    with open(filename,'w') as f:
        for site in wordpress_sites:
            f.write(f"{site}\n")

    print(f"\n[+] Saved file to {filename}")
    wordpress_sites.clear() 

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def check_for_wordpress(url):
    try:
        html_content = requests.get(url, verify=False).text
        soup = BeautifulSoup(html_content, "lxml")
        body = soup.find_all("body")
        search_str = r'wp-content|\/wp-content\/|\/wp-includes\/'

        for string in body:
            matchObj = re.search(search_str, str(string))
            
            if matchObj:
                print(f"[+] Found - {url}")
                wordpress_sites.append(url)
                break

    except Exception as err:
        print(f"[!] Error - {err}")

if __name__ == "__main__":
    wordpress_sites = []

    parser = argparse.ArgumentParser(description="Get wordpress sites from list of hostnames")
    parser.add_argument("file_to_read", help="File containing a list of hostnames")
    parser.add_argument("-o", "--outfile", help="File to write the results of all wordpress sites", required=True)
    parser.add_argument("-t", "--threads", nargs="?", const=20, type=int, default=20, help="Number of threads, default is 20.")

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]
    outfile = args.outfile

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor: 
        print(f"[+] Scanning with {args.threads} threads.\n")

        for host in stripped_hostnames:
            url = f"https://{host}"
            executor.submit(check_for_wordpress, url)

    if not wordpress_sites:
        print(f"\n[X] No wordpress sites found.")
    else:
        save_wordpress_sites(outfile)
