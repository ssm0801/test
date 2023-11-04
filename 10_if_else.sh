#!/bin/bash
read -p "Enter Your Marks : " marks

if [[ $marks -gt 40 && $marks -lt 90 ]];
then 
	echo "you are superb"
else
	echo "you loose"
fi

# age=14
# if [ $age -ge 18 ]; then
# 	echo "Able to vote"
# else
# 	echo "Not eligible"
# fi

# if [ $age -ge 18 ]
# then
# 	echo "Able to vote"
# else
# 	echo "Not eligible"
# fi