#!/usr/bin/python3
import urllib.parse
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encode URL payload.')
    parser.add_argument("payload", help="Input payload in between quotes \"\"")

    args = parser.parse_args()
    encodedPayload = urllib.parse.quote(args.payload.strip())

    print(f"\n[+] Encoded payload:\n{encodedPayload}")

