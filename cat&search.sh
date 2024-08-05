# script to cat out all files and searches for a specific string
#!/bin/bash

# Set the directory where the .txt files are located
dir=/home # update to the folder containing the files

# Set password to search for
password="password" # Update to the string you're searching for

# Loop through each .txt file in the dir
for file in "$dir"/*.txt
do
  # Search for the password in the file
  if grep -q "$password" "$file"; then
    echo "Password found in file: $file"
  else
    echo "Password not found in file: $file"
  fi
done
