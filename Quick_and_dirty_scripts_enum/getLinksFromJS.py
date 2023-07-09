#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests
import argparse
import re
import threading
import validators

def getJsFromURL(url):
    response = requests.get(url)
    tree = bs(response.text, 'html.parser') # Parse into tree

    scriptList = list()

    for script in tree.find_all('script'):
        src = script.get('src')

        if src is not None:
            if not src.startswith('http') and not src.startswith('https'):
                src = url + src 
            
            scriptList.append(src)

    scriptList.sort()
    return(scriptList)

def processURL(url):
    response = requests.get(url)
    jsCode = response.text
    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    extractedURLs = re.findall(regex, jsCode)

    validURLs = list()

    for extractedURL in extractedURLs:
        validated = validators.url(extractedURL)

        if validated:
            validURLs.append(extractedURL)

    urls.extend(validURLs)

def getURLs(urlList):
    threads = list()

    for url in urlList:
        t = threading.Thread(target=processURL, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI Tool that gets link from from javascript files on a target website.')
    parser.add_argument('-u', '--url', help='Target URL.')
    args = parser.parse_args()

    url = args.url

    if url is not None:
        scriptList = getJsFromURL(url)

        urls = list()
        getURLs(scriptList)

        uniqueURLs = list(set(urls))
        uniqueURLs.sort()

        for url in uniqueURLs:
            print(url)

    else:
        print('URL must not be empty and URL must start with http:// or https://')