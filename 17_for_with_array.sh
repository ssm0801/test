#!/bin/bash

myArray=(1 2 3 hi hello "boss")

length=${#myArray[*]}

for item in ${myArray[*]}
do
echo "$item"
done

for((i=0;i<$length;i++))
do
	echo "value of array is ${myArray[i]}"
done
