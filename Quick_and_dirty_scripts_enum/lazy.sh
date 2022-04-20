#!/bin/bash
FNAME=$1

if [ -z "$FNAME" ]
then
  echo "Usage instructions:"
  echo "$0 hostnames.txt"
  echo -e "\nImportant:"
  echo "Hostnames must contain http:// or https://"
  exit 1

else
  while read line; do
    # Remove https:// ; Only include domain names
    dname=$(echo $line | awk -F '//' '{print $2}')

    echo -e "++ Performing top ports scan on $dname ++\n"
    nmap -sT -sC -sV --min-rate 50 -v $dname -oA "nmap-$dname" 2> /dev/null

    echo -e "++ Performing nikto scan on $dname ++\n"
    nikto -h $dname -port 443 -Tuning x6 2> /dev/null | tee "nikto-$dname"

    echo -e "++ Performing dirb scan on $dname ++\n"
    dirb $line -o "dirb-$dname" 2> /dev/null
  done < $FNAME

fi

exit 0
