#!/bin/bash

NUMBER_OF_PRACTICE=$1
STUDENT=$2

echo "Starting practice ${NUMBER_OF_PRACTICE} of student ${STUDENT}"

while true; do
    read -p "Continue? yes/no: " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please, answer yes or no.";;
    esac
done

# Source the environment setup script
source ./setenv.sh

# Run the main Python script
python "./practice_${NUMBER_OF_PRACTICE}/${STUDENT}.py"

# Deactivation is not strictly necessary for a script, as the environment changes
# do not persist when the script finishes
echo "Script execution finished."
