#!/usr/bin/python3
import requests 
import argparse

valid = []
maybe_valid = []

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        urls = f.readlines()
    return(urls)

def save_valid_hosts():
    # Save valid and maybe_valid to file
    with open("./valid.txt",'w') as valid_file:
        for valid_url in valid:
            valid_file.write(valid_url + "\n")

def save_maybe_valid_hosts():
    with open("./maybe_valid.txt",'w') as maybe_valid_file:
        for maybe_valid_url in maybe_valid:
            maybe_valid_file.write(maybe_valid_url + "\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Check host(s) for code 200.')
    parser.add_argument("file_to_read", help="Enter file containing a list of hosts")

    args = parser.parse_args()
    urls = read_from_file(args.file_to_read.strip())

    # Check URL 1 by 1
    for index, url in enumerate(urls):
        url = f"https://{url.strip()}"

        try:
            print(f"{index} ---> Trying {url} <---")
            res = requests.get(url)
            res_code = res.status_code
            print(f"\nResponse code: {res_code}\n")

            if res_code == 200:
                valid.append(url)
            else:
                maybe_valid.append(url)

        except Exception as err:
            print(f"\nErr -> {err}\n")