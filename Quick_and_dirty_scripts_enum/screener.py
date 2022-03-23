#!/usr/bin/python3
from selenium import webdriver
from argparse import ArgumentParser
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def read_from_file(filename):
    with open(filename, 'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def delay():
    delay_in_seconds = 3
    sleep(delay_in_seconds)

def take_screenshot(target, outdir):
    try:
        url = f"https://{target}"
        outfile = os.path.join(outdir, f"{target}.png")

        print(f"\n[+] Screenshotting {url}")

        driver.get(url)
        delay()
        driver.get_screenshot_as_file(outfile)

        print(f"Saved {target} to {outfile}")

    except Exception as err:
        print(f"[!] take_screenshot() : {err}")

if __name__ == "__main__":
    # Some parts borrowed from:
    # https://arminreiter.com/2021/08/take-and-compare-website-screenshots-with-python/
    parser = ArgumentParser(description='Screenhost target website.')
    parser.add_argument('-t', '--target', help='www.target.com')
    parser.add_argument('-i', '--infile', help='File containing list of hostnames, without https://')
    parser.add_argument('-d', '--dir', help='Output directory.')

    args = parser.parse_args()

    target = args.target
    filename = args.infile
    outdir = args.dir

    options = Options()
    options.add_argument("--headless")

    width = 1024
    height = 768

    driver = webdriver.Firefox(options=options)
    driver.set_window_size(width, height)

    try:

        if target and outdir:
            os.makedirs(outdir, exist_ok=True)
            take_screenshot(target, outdir) 

        elif filename and outdir:
            hostnames = read_from_file(filename)
            hostnames_stripped = [hostname.strip() for hostname in hostnames]

            os.makedirs(outdir, exist_ok=True)

            for hostname in hostnames_stripped:
                take_screenshot(hostname, outdir)

        else:
            parser.print_help()

    except Exception as err:
        print(f"[!] main() : {err}")

    finally:
        driver.quit()
