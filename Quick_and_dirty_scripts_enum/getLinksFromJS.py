#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests
import argparse
import re
import threading
import validators

def getJsFileFromTargetURL():
    response = requests.get(targetUrl)
    tree = bs(response.text, 'html.parser') # Parse into tree

    scriptList = list()

    for script in tree.find_all('script'):
        jsSrc = script.get('src')

        if jsSrc is not None:
            if not jsSrc.startswith('http') and not jsSrc.startswith('https'):
                jsSrc = targetUrl + jsSrc 
            
            scriptList.append(jsSrc)

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

def getURLsFromJsSrc(jsURLs):
    threads = list()

    for jsURL in jsURLs:
        t = threading.Thread(target=processURL, args=(jsURL,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Comand-line tool that retrieves hyperlinks from JavaScript files on a specified website.')
    parser.add_argument('-u', '--url', help='Target URL.')
    args = parser.parse_args()

    targetUrl = args.url

    if targetUrl is not None:
        validated = validators.url(targetUrl)

        if validated:
            scriptList = getJsFileFromTargetURL()

            urls = list()
            getURLsFromJsSrc(scriptList)

            uniqueURLs = list(set(urls))
            uniqueURLs.sort()

            if len(uniqueURLs) > 0:
                for index, url in enumerate(uniqueURLs, start=1):
                    print(f'{index}. {url}')
            else:
                print('No results.')

        else:
            print('URL must not be empty and URL must start with http:// or https://')