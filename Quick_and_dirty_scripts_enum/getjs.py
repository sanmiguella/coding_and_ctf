#!/usr/bin/env python3
import requests
import argparse
import sys
import os
import shutil

from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from url_downloader import save_file
from threading import Thread

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def formDirPath(url):
    cwd = os.getcwd()
    hostname = urlparse(url).netloc
    return(f"{cwd}/{hostname}")

def checkIfDirExists(url):
    fullPath = formDirPath(url)

    if os.path.exists(fullPath):
        shutil.rmtree(fullPath, ignore_errors=True)    

    os.mkdir(fullPath)

def getJSlinks(url, download):
    jsLinks = list()

    try:
        res = requests.get(url, verify=False)

    except Exception as err:
        print(f"[!] Error (getJSlinks) - {err}")
        pass

    else:
        soup = BeautifulSoup(res.text, 'html.parser')
        scriptTags = soup.find_all('script')

        if len(scriptTags) > 0:
            print()

            for tag in scriptTags:
                src = tag.get('src')
                
                if src is not None:
                    jsUrl = urljoin(url, src)
                    
                    print(f"[+] Found {jsUrl}")
                    jsLinks.append(jsUrl)

            if len(jsLinks) > 0:
                hostname = urlparse(url).netloc
                jsLinksFile = f"jsLinks-{hostname}.txt"

                with open(jsLinksFile, 'w') as f:
                    for link in jsLinks:
                        f.write(f"{link.strip()}\n")        

                print(f"[o] Saved results to {jsLinksFile}")

                if download:
                    downloadJSlinks(url, jsLinks)

def downloadWrapper(link, fullPath, localFilename):
    save_file(url=link, file_path=fullPath, file_name=localFilename)

def downloadJSlinks(url, jsLinks):
    checkIfDirExists(url)
    fullPath = formDirPath(url)

    threads = list()

    print(f"[o] Initiating download on {url}")

    for link in jsLinks:
        localFilename = link.split('/')[-1]

        try:
            t = Thread(target=downloadWrapper, args=(link, fullPath, localFilename))
            threads.append(t)
            t.start()

        except Exception as dlErr:
            print(f"[!] Download Error - {link} - {dlErr}")
            pass

    for thread in threads:
        thread.join()

    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get JS file(s) from website(s).")
    subParser = parser.add_subparsers(dest="command") 

    singleSiteParser = subParser.add_parser("single", help="Get JS file(s) from a single website.")
    singleSiteParser.add_argument("-u", "--url", help="Url to download JS file(s) from. Format: https://example.com", required=True)
    singleSiteParser.add_argument("-d", "--download", help="Download JS file(s).", action='store_true')

    multipleSiteParser = subParser.add_parser("multiple", help="Get a list of JS file(s) from multiple websites.")
    multipleSiteParser.add_argument("-f", "--file", help="File containing multiple Url(s).", required=True)
    multipleSiteParser.add_argument("-d", "--download", help="Download JS file(s).", action='store_true')

    args = parser.parse_args()
    command = args.command

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
