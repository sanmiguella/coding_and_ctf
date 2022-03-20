#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import argparse
import re

links = []

def banner():
    intro = '''
    ██╗     ██╗███╗   ██╗██╗  ██╗███████╗
    ██║     ██║████╗  ██║██║ ██╔╝██╔════╝
    ██║     ██║██╔██╗ ██║█████╔╝ ███████╗
    ██║     ██║██║╚██╗██║██╔═██╗ ╚════██║
    ███████╗██║██║ ╚████║██║  ██╗███████║
    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
    '''
    print(intro)

def save_links(filename):
    with open(filename,'w') as f:
        for site in links:
            f.write(f"{site}\n")

    print(f"\n[+] Saved file to {filename}")

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def check_for_links(url):
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")

        for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
            link_only = link['href']
            links.append(link_only)
            print(link_only) 

    except Exception as err:
        print(f"[!] Error :: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get Links from Url")
    parser.add_argument("-u", "--url", help="URL containing Links.", required=True)
    parser.add_argument("-o", "--outfile", help="File to write all links to.")

    args = parser.parse_args()
    outfile = args.outfile
    url = args.url
    url = url.strip()

    banner()
    check_for_links(url)

    if outfile:
        save_links(outfile)
