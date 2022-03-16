#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

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

def save_valid_hosts(validfile):
    valid.sort()

    with open(validfile, 'w') as vf:
        for valid_url in valid:
            vf.write(valid_url + "\n")

    print(f"[+] Written valid hosts to :: {validfile}")

def save_maybe_valid_hosts(maybefile):
    maybe_valid.sort()

    with open(maybefile, 'w') as mf:
        for maybe_valid_url in maybe_valid:
            mf.write(maybe_valid_url + "\n")

    print(f"[+] Written maybe valid hosts to :: {maybefile}")

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
    parser.add_argument("-vf", "--validfile", help="File which contains a list of HTTP 200 ok hosts.", required=True)
    parser.add_argument("-mf", "--maybefile", help="File which contains a list of hosts whose response code isn't HTTP 200 ok.", required=True)

    args = parser.parse_args()
    urls = read_from_file(args.file_to_read)
    urls_stripped = [url.strip() for url in urls]
    validfile = args.validfile
    maybefile = args.maybefile

    banner()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for url in urls_stripped:
            url = f"https://{url}"
            executor.submit(initiate_request, url)

    print()
    save_valid_hosts(validfile)
    save_maybe_valid_hosts(maybefile)
