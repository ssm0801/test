#!/bin/bash
# IFS - internal field separator
# read a csv file

cat test.csv | awk 'NR!=1{print}' | while IFS="," read id name age
do
	echo "the id $id the name $name the age $age"
done
