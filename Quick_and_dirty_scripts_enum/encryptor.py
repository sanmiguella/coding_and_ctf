#!/usr/bin/python3
from argparse import ArgumentParser
from pyAesCrypt import encryptFile, decryptFile
import os 
import sys

def encrypt_file(fnIn, fnOut, password):
    try:
        if os.path.exists(fnIn):
            encryptFile(fnIn, fnOut, password)
            print(f"[+] Encryted {fnIn} to {fnOut}")
            
            os.remove(fnIn)
            print(f"[+] Removed {fnIn}")
    
        else:
            print(f"[!] {fnIn} not found.")

    except Exception as err:
        print(f"[!] {err}")
        sys.exit()

def decrypt_file(fnIn, fnOut, password):
    try:
        if os.path.exists(fnIn):
            decryptFile(fnIn, fnOut, password)
            print(f"[+] Decrypted {fnIn} to {fnOut}")
            
            os.remove(fnIn)
            print(f"[+] Removed {fnIn}")

        else:
            print(f"[!] {fnIn} not found.")

    except Exception as err:
        print(f"[!] {err}")
        sys.exit()

if __name__ == "__main__":
    parser = ArgumentParser(description="Encrypt or Decrypt File.")
    parser.add_argument("-i", "--inputfile", help="Input File.")
    parser.add_argument("-o", "--outputfile", help="Output File.")
    parser.add_argument("-e", "--encrypt", help="To encrypt", action="store_true")
    parser.add_argument("-d", "--decrypt", help="To decrypt", action="store_true")
    parser.add_argument("-p", "--password", help="Password")

    args = parser.parse_args()
    inputFile = args.inputfile
    outputFile = args.outputfile
    password = args.password
    act_encrypt = args.encrypt
    act_decrypt = args.decrypt

    if act_encrypt and inputFile and outputFile and password:
        encrypt_file(inputFile, outputFile, password)
    elif act_decrypt and inputFile and outputFile and password:
        decrypt_file(inputFile, outputFile, password)
    else:
        parser.print_help()
