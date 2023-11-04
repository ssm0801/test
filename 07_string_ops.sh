#!/bin/bash

myVar="hey buddy how are you Buddy ?"

echo "Length of my var is ${#myVar}"

echo "upper case is ${myVar^^}"
echo "lower case ${myVar,,}"


# to replace the string 

newVar=${myVar/Buddy/Paul}

echo "New Var is ------- $newVar"

# to slice a string 

echo "after slice ${myVar:4:5}"

