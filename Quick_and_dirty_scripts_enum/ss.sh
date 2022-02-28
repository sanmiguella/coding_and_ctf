#!/bin/bash
host_file=$1

while IFS="" read -r host || [ -n "$host" ]
do
        echo "[+] Screenshotting $host"
        gowitness single https://$host
done < $host_file


ss_dir='/tmp/screenshots'
if [ ! -d "$ss_dir" ]; then
        mkdir $ss_dir
fi

cp -v ./screenshots/* $ss_dir