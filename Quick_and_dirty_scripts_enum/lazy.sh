#!/bin/bash
FNAME=$1

if [ -z "$FNAME" ]
then
  echo "$0 file_containing_list_of_hostnames"

else
  while read line; do
    # Remove https:// ; Only include domain names
    dname=$(echo $line | awk -F '//' '{print $2}')

    echo "++ Performing top ports scan on $dname ++"
    nmap -sC -sV -v $dname -oA "nmap-$dname"

    echo "++ Performing nikto scan on $dname ++"
    nikto -h $dname -port 443 -Tuning x6 | tee "nikto-$dname"

    echo "++ Performing dirb scan on $dname ++"
    dirb $line -o "dirb-$dname"
  done < $FNAME

fi
