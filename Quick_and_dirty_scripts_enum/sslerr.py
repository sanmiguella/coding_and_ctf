#!/usr/bin/python3
import requests
import argparse
import concurrent.futures

ssl_err_list = []

def banner():
    intro = '''
    ██ ███    ██ ██    ██  █████  ██      ██ ██████   █████  ████████  ██████  ██████  
    ██ ████   ██ ██    ██ ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
    ██ ██ ██  ██ ██    ██ ███████ ██      ██ ██   ██ ███████    ██    ██    ██ ██████  
    ██ ██  ██ ██  ██  ██  ██   ██ ██      ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ 
    ██ ██   ████   ████   ██   ██ ███████ ██ ██████  ██   ██    ██     ██████  ██   ██ 
    '''
    print(intro)

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        urls = f.readlines()

    return(urls)

def save_sslerror_hosts(ssl_err_file):
    ssl_err_list.sort()

    with open(ssl_err_file, 'w') as sef:
        for host in ssl_err_list:
            sef.write(f"{host}\n")

    print(f"\n[+] Written hosts with ssl error to :: {ssl_err_file}")

def initiate_request(url):
    try:
        response = requests.get(url, allow_redirects=False, verify=True)
        response_code = response.status_code

    except requests.exceptions.SSLError as ssl_err:
        output = f"{url} :: {ssl_err}"
        print(output)
        ssl_err_list.append(output)

    except Exception as err:
        print(f"{url} :: {err}")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check host(s) for code SSL errors.')
    parser.add_argument("file_to_read", help="File containing a list of hosts")
    parser.add_argument("-o", "--outfile", help="File to write results of a list of hosts with SSL errors", required=True)

    args = parser.parse_args()
    urls = read_from_file(args.file_to_read)
    urls_stripped = [url.strip() for url in urls]
    outfile = args.outfile

    banner()
  
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for url in urls_stripped:
            url = f"https://{url}"
            executor.submit(initiate_request, url)
    
    save_sslerror_hosts(outfile)
