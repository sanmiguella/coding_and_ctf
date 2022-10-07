#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import argparse
import re
import numpy as np
import concurrent.futures
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def save_links(filename, links):
    with open(filename,'w') as f:
        for link in links:
            f.write(f"{link}\n")

    print(f"\n[+] Saved file to {filename}")

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        urls = [url.strip() for url in f.readlines()]

    return(urls)

def check_webpage_for_links(url):
    try:
        html_content = requests.get(url, verify=False).text
        soup = BeautifulSoup(html_content, "lxml")

        for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
            link_only = urljoin(url, link['href'])
            links.append(link_only)
            print(link_only) 

    except Exception as err:
        print(f"[!] {err}")

def read_from_file(file_to_read):
    with open(file_to_read, 'r') as f:
        urls = [url.strip() for url in f.readlines()]

    return urls

if __name__ == "__main__":
    links = list()

    parser = argparse.ArgumentParser(description="Get Links from Url")
    parser.add_argument("-f", "--file", help="File containing list of hosts that starts with https://", required=True)
    parser.add_argument("-o", "--outfile", help="File to write all links to.")
    parser.add_argument("-t", "--threads", nargs="?", const=20, type=int, default=20, help="Number of threads, default is 20.")

    args = parser.parse_args()
    outfile = args.outfile
    urls = read_from_file(args.file)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        print(f"[+] Scanning with {args.threads} threads.\n")

        for url in urls:
            executor.submit(check_webpage_for_links, url)

    links = np.unique(links).tolist()
    links.sort()

    if outfile:
        save_links(outfile, links)
