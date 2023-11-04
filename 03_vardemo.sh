#!/bin/bash

# how to use variable

name="Ranjit"
age=28
pi=3.14
isEligibile=false

echo $name
echo $age
echo $pi
echo $isEligibile

name="raja"
echo "my name is $name"

#var to store the output of the command

HOSTNAME=$(hostname)
echo "$HOSTNAME"

school="DSES"
echo "${school}"

