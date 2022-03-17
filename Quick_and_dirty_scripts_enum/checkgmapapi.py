#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import argparse
import concurrent.futures
import re

notFound = True

def banner():
    intro = '''
     ██████  ███    ███  █████  ██████   █████  ██████  ██     ███████ ██ ███    ██ ██████  ███████ ██████  
     ██       ████  ████ ██   ██ ██   ██ ██   ██ ██   ██ ██     ██      ██ ████   ██ ██   ██ ██      ██   ██ 
     ██   ███ ██ ████ ██ ███████ ██████  ███████ ██████  ██     █████   ██ ██ ██  ██ ██   ██ █████   ██████  
     ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ ██      ██     ██      ██ ██  ██ ██ ██   ██ ██      ██   ██ 
      ██████  ██      ██ ██   ██ ██      ██   ██ ██      ██     ██      ██ ██   ████ ██████  ███████ ██   ██ 
                                                                                                              
    '''
    print(intro)

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def check_for_gmapapi(url):
    global notFound

    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        body = soup.find_all("body")
        gmapapi_regex = re.compile(r'AIza\w+')

        for data in body:
            results = re.findall(gmapapi_regex, str(data))
            
            if results:
                notFound = False
                print(f"[+] Found on {url}:")
                
                for result in results:
                    print(f"- {result}")

    except Exceptions as err:
        print(f"[!] Error :: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check gmapapi from list of hostnames")
    parser.add_argument("file_to_read", help="File containing a list of hostnames")

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read)
    stripped_hostnames = [hostname.strip() for hostname in hostnames]

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor: 
        for host in stripped_hostnames:
            url = f"https://{host}"
            executor.submit(check_for_gmapapi, url)

    if notFound:
        print("[!] No gmap api keys found.")
