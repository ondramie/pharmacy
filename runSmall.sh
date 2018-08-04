#!/bin/bash

# NOTE: drug names have chemical abbreviations such as HCL; do we remove those? 
# NOTE: no distinction if drug name is descending by ASCII code or alphabetical order

program=$"./src/pharmacy_counting.py"
path=$"./insight_testsuite/tests/test_0"


for entry in "$path/input"/*
do 
	oldIFS=$IFS
	IFS="/"; read -ra array <<< "$entry"
	length=${#array[@]}
	index=$(($length - 1))
	IFS="."; read -ra filename <<< "${array[$index]}"
	file="${filename[0]}"
	
	printf "my input file:\t$file\n" 
	more "$entry"
	printf "\n"

	IFS=$oldIFS
	outputs="$path/output/$file-output.txt"
	python3 $program $entry $outputs
	pid=$!
	wait $pid
	printf "my output file:\t$file-ouput.txt\n"
	more "$outputs" 
	printf "\n"

done
