#!/bin/bash

function addition(){
	let num1=$1
	let num2=$2
	let sum=$num1+$num2
	echo "the sum is $sum"
}

addition 10 20
