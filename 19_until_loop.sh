#!/bin/bash

a=10

until [[ $a -eq 1 ]]
do
	echo "Value of a is $a "
	let a--
done

# until true
# do
# echo "$a"
# let a--
# done