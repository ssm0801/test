#!/bin/bash

count=0
num=10
while [[ $count -le $num ]]
do
	echo "number are $count"
	let count++
done

# while true
# do
# echo "$count"
# let count++
# done

# myArray=(1 2 3 hi hello "boss")
# length=${#myArray[*]}

# i=0
# while [[ $i -lt $length ]]
# do
# 	echo "value of array is ${myArray[i]}"
# 	let i++
# done