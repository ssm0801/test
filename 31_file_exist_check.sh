#!/bin/bash

FILEPATH="/home/ubuntu/scripts/test.csv"

# -d for directory
# -f for file
if [[ -f $FILEPATH ]]
then
	echo "file exist"
else
	echo "not exist"
	exit 1
fi

