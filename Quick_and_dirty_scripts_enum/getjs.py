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

def readFromFile(filename):
    with open(filename, "r") as f:
        urls = [line.strip() for line in f.readlines()]
    
    return(urls)

def getHostname(url):
    return(urlparse(url).netloc)

def formDirPath(url):
    hostname = getHostname(url)
    return(f"{os.getcwd()}/{hostname}")

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
        #print(f"[!] Get JS links error - {err}")
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
                    jsLinks.append(jsUrl)
                    print(f"[+] Found {jsUrl}")

            if len(jsLinks) > 0:
                hostname = getHostname(url)
                jsLinksFile = f"jsLinks-{hostname}.txt"

                with open(jsLinksFile, 'w') as f:
                    f.writelines("%s\n" % link.strip() for link in jsLinks)

                print(f"[o] Saved results to {jsLinksFile}")

                if download:
                    downloadJSlinks(url, jsLinks)

def downloadWrapper(link, fullPath, localFilename):
    save_file(url=link, file_path=fullPath, file_name=localFilename)

def downloadJSlinks(url, jsLinks):
    checkIfDirExists(url)
    fullPath = formDirPath(url)

    threads_downloadJSlinks = list()

    print(f"[o] Initiating download on {url}")

    for jsLink in jsLinks:
        localFilename = jsLink.split('/')[-1]

        try:
            tr = Thread(target=downloadWrapper, args=(jsLink, fullPath, localFilename))
            threads_downloadJSlinks.append(tr)
            tr.start()

        except Exception as err:
            #print(f"[!] Download erro - {jsLink} - {err}")
            pass

    for thread in threads_downloadJSlinks:
        thread.join()

def massGet(urls, download):
    threads_MassGet = list()

    for url in urls:
        tr = Thread(target=getJSlinks, args=(url, download))
        threads_MassGet.append(tr)
        tr.start()

    for thread in thread_MassGet:
        thread.join()

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
        massGet(readFromFile(args.file), args.download)

    else:
        parser.print_usage()
