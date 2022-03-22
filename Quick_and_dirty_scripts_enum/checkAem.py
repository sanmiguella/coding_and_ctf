#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import argparse
import concurrent.futures
import re

aem_sites = []

def banner():
    intro = '''
     █████  ███████ ███    ███ 
     ██   ██ ██      ████  ████ 
     ███████ █████   ██ ████ ██ 
     ██   ██ ██      ██  ██  ██ 
     ██   ██ ███████ ██      ██ 
    '''
    print(intro)

def save_aem_sites(filename):
    aem_sites.sort() 

    with open(filename,'w') as f:
        for site in aem_sites:
            f.write(f"{site}\n")

    print(f"\n[+] Saved file to {filename}")

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def check_for_aem(url):
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        img = soup.find_all("img")
        aem_str_regex = r'\/clientlibs\/|\/etc\/|\/granite\/|\/cq\/'

        for data in img:
            matchObj = re.search(aem_str_regex, str(data))
            
            if matchObj:
                matched_string = matchObj[0]
                print(f"[+] Found \"{matched_string}\" on {url}")
                aem_sites.append(url)
                break

    except Exception as err:
        print(f"[!] Error :: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get aem sites from list of hostnames")
    parser.add_argument("file_to_read", help="File containing a list of hostnames")
    parser.add_argument("-o", "--outfile", help="File to write the results of all aem sites", required=True)

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]
    outfile = args.outfile

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor: 
        for host in stripped_hostnames:
            url = f"https://{host}"
            executor.submit(check_for_aem, url)

    if not aem_sites:
        print("\n[!] No AEM sites found.")
    else:
        save_aem_sites(outfile)