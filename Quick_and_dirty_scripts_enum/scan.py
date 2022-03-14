#!/usr/bin/python3
import requests
import argparse
import concurrent.futures
import uuid

valid = []
maybe_valid = []

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def banner():
    intro = '''
    ██    ██  █████  ██      ██ ██████   █████  ████████  ██████  ██████  
    ██    ██ ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
    ██    ██ ███████ ██      ██ ██   ██ ███████    ██    ██    ██ ██████  
     ██  ██  ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
       ████   ██   ██ ███████ ██ ██████  ██   ██    ██     ██████  ██   ██ 
    '''
    print(intro)

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        urls = f.readlines()

    return(urls)

def save_valid_hosts():
    prepend_filename = uuid.uuid4().hex
    vf = f"{prepend_filename}-valid.txt"
    valid.sort()

    with open(vf, 'w') as valid_file:
        for valid_url in valid:
            valid_file.write(valid_url + "\n")

    print(f"[+] Written valid hosts to :: {vf}")

def save_maybe_valid_hosts():
    prepend_filename = uuid.uuid4().hex
    mvf = f"{prepend_filename}-maybe_valid.txt"
    maybe_valid.sort()

    with open(mvf, 'w') as maybe_valid_file:
        for maybe_valid_url in maybe_valid:
            maybe_valid_file.write(maybe_valid_url + "\n")

    print(f"[+] Written maybe valid hosts to :: {mvf}")

def initiate_request(url):
    try:
        response = requests.get(url, verify=False)
        response_code = response.status_code
        print(f"{url} :: {response_code}")

        if response_code == 200:
            valid.append(url)
        else:
            maybe_valid.append(url)

    except Exception as err:
        print(f"{url} :: {err}")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check host(s) for code 200.')
    parser.add_argument("file_to_read", help="Enter file containing a list of hosts")

    args = parser.parse_args()
    urls = read_from_file(args.file_to_read)
    urls_stripped = [url.strip() for url in urls]

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for url in urls_stripped:
            url = f"https://{url}"
            executor.submit(initiate_request, url)

    print()
    save_valid_hosts()
    save_maybe_valid_hosts()
