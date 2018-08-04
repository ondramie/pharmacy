#!/bin/bash

program=$"./src/pharmacy_counting.py"
path=$"./insight_testsuite/tests/test_2"

for entry in "$path/input"/*
do 
	number=$(echo "$entry" | tr -dc '^10+$')
	size=$(wc -c $entry)
	printf "the size is: $size\n"

	output=$"$path/output/ouput-$number.txt"
	printf "the output filename:\toutput-$number.txt\n"
	time python3 $program $entry $output
	pid=$!
	wait $pid
done