#!/bin/bash

while read item
do
	echo "value from file is $item"
done < names.txt

# while read item || [ -n "$item" ]; do
#     echo "value from file is $item"
# done < names.txt
