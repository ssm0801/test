#!/bin/bash

#getting values from a file names.txt 

FILE="$PWD/names.txt"

for name in $(cat $FILE)
do
	echo "$name"
	sleep 3
done


# mapfile -t names_array < names.txt

# len=${#names_array[*]}

# for((i=$len-1;i>=0;i--))
# do
# 	echo "${names_array[i]}"
# done