#!/bin/bash

read -p " enter your marks " marks

if [[ $marks -ge  80 ]]
then
	echo " you are A grade"
elif [[ $marks -ge 60 ]]
then	
	echo "2nd division"
elif [[ $marks -ge 40 ]]
then	
	echo "you are 3rd "
else
	echo "oops you are fail "
fi	

# if [ $a -lt $b ]; then
# 	echo "$a is less than $b"
# elif [ $b -lt $a ]; then
# 	echo "$b is less than $a"
# else
# 	echo "$a and $b are equal"
# fi