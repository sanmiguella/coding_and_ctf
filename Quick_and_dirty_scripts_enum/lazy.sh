#!/bin/bash
FNAME=$1
DIR=$2

if [ -z "$FNAME" ] || [ -z "$DIR" ]
then
  echo "Usage instructions:"
  echo "$0 hostnames.txt target_directory"
  echo -e "\nImportant:"
  echo "Hostnames must contain http:// or https://"
  exit 1

else
  mkdir -p $DIR

  while read line; do
    # Remove https:// ; Only include domain names
    dname=$(echo $line | awk -F '//' '{print $2}')

    echo -e "\n++ Performing top ports scan on $dname ++\n"
    nmap -sT -sC -sV --min-rate 50 -v $dname -oA "$DIR/nmap-$dname" 2> /dev/null

    echo -e "\n++ Performing nikto scan on $dname ++\n"
    nikto -h $dname -port 443 -Tuning x6 2> /dev/null | tee "$DIR/nikto-$dname"

    echo -e "\n++ Performing dirb scan on $dname ++\n"
    dirb $line -o "$DIR/dirb-$dname" 2> /dev/null
  done < $FNAME

fi

exit 0
