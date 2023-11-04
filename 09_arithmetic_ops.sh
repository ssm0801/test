#!/bin/bash

# Maths Calculation

x=10
y=20

let mult=$x*$y
echo "$mult"

let sum=$(($x+$y))
echo "$sum"

res=$(($y-$x))
echo "$res"

divide=$((4/3))
echo $divide