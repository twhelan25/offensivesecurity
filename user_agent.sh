bash
#!/bin/bash

# Function to get MD5 hash of curl response
get_response_hash() {
        curl -s -A "$1" $ip -L | md5sum | awk '{print $1}'
}

# Loop through capital letters A to Z
for letter in {A..Z}; do
        current_response=$(get_response_hash "$letter")

        if [ "$first_run" = true ] || [ "$current_response" != "$previous_response" ]; then
                echo "User-Agent: $letter"
                echo "Response hash: $current_response"
                curl -A "$letter" $ip -L
                echo -e "\n----------\n"


                previous_response=$current_response
                first_run=false
        fi
done
