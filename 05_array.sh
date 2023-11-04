#!/bin/bash

# Array
# declare myArray
myArray=(1 true 3.14 hello "ranjit")
echo "${myArray[4]}"
# blank
echo "${myArray[5]}"

echo "display all value * : ${myArray[*]}"
echo "display all value @ : ${myArray[@]}"

# how to find the length of an array 

echo "Length of an array #* : ${#myArray[*]}"
echo "Length of an array #@ : ${#myArray[@]}"

# ${array[*]:start:count}
echo " value from index 2-3 : ${myArray[*]:2:2} "

# updating array with new value
myArray+=(New false 5 "TWS")

echo "my new array : ${myArray[*]}"
