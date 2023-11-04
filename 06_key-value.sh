#!/bin/bash


# how to store the key value pairs
# associated array

declare -A myArray

myArray=([name]="Ranjit" [city]=pune [age]=13 [isEligibile]=true)

echo "my name is ${myArray[name]}" 
echo "my name is ${myArray[*]}" 
