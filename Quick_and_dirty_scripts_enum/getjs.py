#!/usr/bin/env python3
import requests
import argparse
import sys
import concurrent.futures
import os
import shutil

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from url_downloader import save_file

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def getJSlinks(url, download):
    try:
        print()
        res = requests.get(url, verify=False)

    except Exception as err:
        print(f"[!] Error : {err}")
        pass

    else:
        soup = BeautifulSoup(res.text, 'html.parser')
        scriptTags = soup.find_all('script')

        if len(scriptTags) > 0:
            for tag in scriptTags:
                src = tag.get('src')
                
                if src is not None:
                    print(f"[+] Found {src}")
                    jsLinks.append(src)

            if len(jsLinks) > 0:
                hostname = urlparse(url).netloc
                linksFilename = f"{hostname}-js-files.txt"

                with open(linksFilename, 'w') as f:
                    for link in jsLinks:
                        f.write(f"{link.strip()}\n")        

                if download:
                    downloadJSlinks(url)

                jsLinks.clear()

        else:
            print(f"[>] No JS file(s) found on {url}")

def downloadJSlinks(url):
    if len(jsLinks) > 0:
        try: 
            currentDir = os.getcwd()
            hostname = urlparse(url).netloc
            fullPath = f"{currentDir}/{hostname}"

            if os.path.exists(fullPath):
                shutil.rmtree(fullPath, ignore_errors=True)    

            os.mkdir(fullPath)

        except Exception as err:
            print(f"[!] Error : {err}")
            pass

        else:
            for link in jsLinks:
                localFilename = link.split('/')[-1]

                try:
                    print(f"[o] Downloading {link}")
                    save_file(url=link, file_path=fullPath, file_name=localFilename)

                except Exception as downloadErr:
                    print(f"[!] {link} : {downloadErr}")
                    pass

        finally:
            jsLinks.clear()
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get JS file(s) from website(s).")
    subParser = parser.add_subparsers(dest="command") 

    singleSiteParser = subParser.add_parser("single", help="Get a list of JS file(s) from a single website.")
    singleSiteParser.add_argument("-u", "--url", help="Url to download JS file(s) from. Format: https://example.com", required=True)
    singleSiteParser.add_argument("-d", "--download", help="Download the scraped JS file(s).", action='store_true')

    multipleSiteParser = subParser.add_parser("multiple", help="Get a list of JS file(s) from multiple websites.")
    multipleSiteParser.add_argument("-f", "--file", help="File containing list of urls.", required=True)
    multipleSiteParser.add_argument("-d", "--download", help="Download the scraped JS file(s).", action='store_true')

    args =parser.parse_args()
    command = args.command
    jsLinks = []

    if command == "single":
        getJSlinks(args.url, args.download)

    elif command == "multiple":
        with open(args.file, "r") as f:
            lines = f.readlines()

        urls = [line.strip() for line in lines]

        for url in urls:
            getJSlinks(url, args.download)

    else:
        parser.print_usage()
