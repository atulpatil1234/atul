#!/bin/bash

# Check if two arguments are passed
if [ "$#" -ne 2 ]; then
  echo "Usage: ./gencsv.sh <start_index> <end_index>"
  exit 1
fi

# Get the start and end indices from the command line arguments
start_index=$1
end_index=$2

# Generate the file 'inputFile'
output_file="inputFile"
> "$output_file" # Empty the file if it already exists

# Generate the entries
for (( i=start_index; i<=end_index; i++ ))
do
  random_number=$(( RANDOM % 1000 ))
  echo "$i, $random_number" >> "$output_file"
done

echo "File '$output_file' has been generated."

