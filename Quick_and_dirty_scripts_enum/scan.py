#!/usr/bin/python3
import requests 

valid = []
maybe_valid = []

if __name__=="__main__":
    f = open("./pub.out",'r')
    urls = f.readlines()
    f.close()

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

    # Save valid and maybe_valid to file
    with open("./valid.txt",'w') as valid_file:
        for valid_url in valid:
            valid_file.write(valid_url + "\n")

    with open("./maybe_valid.txt",'w') as maybe_valid_file:
        for maybe_valid_url in maybe_valid:
            maybe_valid_file.write(maybe_valid_url + "\n")
    
