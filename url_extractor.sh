#!/bin/bash

echo "Enter the file for URL extraction: "
read file

#check if the file exists and is readable
if [[ ! -f "$file" || ! -r "$file" ]]; then
    echo "File does not exist or is not readable."
    exit 1
fi

#extract URLs and save to urls.txt
grep -oP '(https?://[^\s"]+)' "$file" > urls.txt

#Confirm completion
echo "URLs have been extracted to urls.txt"

