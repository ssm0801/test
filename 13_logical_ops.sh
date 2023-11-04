#!/bin/bash

# AND Operator
read -p "what is your age " age
if [[ age -ge 18 && age -le 80 ]]
then
	echo "eligible for vote"
else
	echo "sorry not eligible"
fi
