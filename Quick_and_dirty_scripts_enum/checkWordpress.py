#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import argparse
import concurrent.futures
import re

wordpress_sites = []

def banner():
    intro = '''
    ██     ██ ██████   ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
    ██     ██ ██   ██ ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
    ██  █  ██ ██████  ██      ███████ █████   ██      █████   █████   ██████  
    ██ ███ ██ ██      ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
     ███ ███  ██       ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
    '''
    print(intro)

def save_wordpress_sites(filename):
    wordpress_sites.sort() 

    with open(filename,'w') as f:
        for site in wordpress_sites:
            f.write(f"{site}\n")

    print(f"\n[+] Saved file to {filename}")

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def check_for_wordpress(url):
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        body = soup.find_all("body")
        search_str = r'wp-content'

        for string in body:
            matchObj = re.search(search_str, str(string))
            
            if matchObj:
                print(f"[+] Found {search_str} :: {url}")
                wordpress_sites.append(url)
                break

    except Exceptions as err:
        print(f"[!] Error :: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get wordpress sites from list of hostnames")
    parser.add_argument("file_to_read", help="File containing a list of hostnames")
    parser.add_argument("-o", "--outfile", help="File to write the results of all wordpress sites", required=True)

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]
    outfile = args.outfile

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor: 
        for host in stripped_hostnames:
            url = f"https://{host}"
            executor.submit(check_for_wordpress, url)

    save_wordpress_sites(outfile)
