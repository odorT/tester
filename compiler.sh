#!/bin/bash 

if [[ "$1" == "-h" ]]; then
	echo "This script compiles (actually runs) and saves python codes from Students/ to Outputs/ folder."
	echo " Usage:"
	echo -e "\t./compiler.sh [option] (task number to start) (task number to finish)"
	echo " Example:"
	echo -e "\t./compiler.sh -h\t It will show the help page of compiler.sh"
	echo -e "\t./compiler.sh 1 20\t It will run and save the outputs of codes from task 1 to task 20 (both included)"
	echo -e "\t./compiler.sh 25 25\t It will run and save the outputs of codes from task 25 only"
	exit
fi


if [[ $# -lt 2 ]]; then
	echo "Not enough arguments!" >&2; exit 0
fi

for task in $(seq "$1" "$2"); do
    path=Tasks/Task_"$task"

    for student in "$path"/Students/*; do
        touch "$student.txt"
        
        for input in "$path"/Inputs/*; do
            python3 $student < $input &>> "$student.txt"
            echo -e  >> "$student.txt"
        done
        mv "$student.txt" "$path"/Outputs/
    done
    echo "Task_$task"
done
echo Done
