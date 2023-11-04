#!/bin/bash --

# this is a comment

# Run in new shell
# ./<script>

# Run in same shell
# source <script>
# . <script>
# bash <script>

# Debug script
# bash -x <script>

# name="XYZ"
# age=55

# echo "File name $0"
# echo "First argument $1"
# echo "Second argument ${2}"
# echo "Tenth argument ${10}"
# echo "Total arguments $#"
# echo "All arguments * $*"
# echo "All arguments @ $@"
# echo "PID of script $$"
# echo "Status of last command $?"

# shift will remove first argument, can be updated while looping it
# while (( $# ))
# do
# 	echo $*
# 	shift
# done

# take input from user
# read name
# echo $name

# IMP ONE
# getopts options

# read -p "Enter age = " age
# if [ $age -ge 18 ]; then
# 	echo "Able to vote"
# else
# 	echo "Not eligible"
# fi

# read -p "Enter age = " age
# if [ $age -ge 18 ]
# then
# 	echo "Able to vote"
# else
# 	echo "Not eligible"
# fi

# read -p "Enter first number = " a
# read -p "Enter second number = " b
# if [ $a -lt $b ]; then
# 	echo "$a is less than $b"
# elif [ $b -lt $a ]; then
# 	echo "$b is less than $a"
# else
# 	echo "$a and $b are equal"
# fi

# For loop
# (( initialization, condition, updation ))
# for (( i=1; i<=10; i++)); do
# 	echo $i
# done

# Infinite for loop
# for ((;;)); do
# 	echo "Infinite"
# done

# For in loop
# {start..end..increment}
# echo "Table for 5"
# for x in {5..50..5}; do
# 	echo "$x"
# done

# While loop
# start=$1
# end=$2
# while [ $start -le $end ]; do
# 	echo $start
# 	let start++;
# done

# Infinite while loop

# while true
# do
# 	echo "Infinite"
# done

# while :
# do
# 	echo "Infinite"
# done

# Until loop
# Inverse of while loop
# Executes until condition becomes true
# counter=0
# until [ $counter -ge 5 ]; do
# 	echo "Count: $counter"
# 	((counter++))
# done

# Infinite until loop
# until false; do
# 	echo "Infinite"
# done

# function sayHello() {
# 	echo $nam
# }

# sayHello

# function greet() {
# 	echo "Good evening $1"
# }

# greet "Sam"
# greet
# greet "John"