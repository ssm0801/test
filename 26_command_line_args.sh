#!/bin/bash
# to access the argument
set -x
if [[ $# -eq 0 ]]
then
	exit 1
fi
echo "First argument is $1"
echo "Second argument is $2"

echo "all the args are -$@"
echo "Number of args are $# "

# for loop to access value from argument
for filename in $@
do
	echo "copying file $filename"
done

