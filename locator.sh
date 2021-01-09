#!/bin/bash 

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "The script takes files from Students/ folder and places them to Tasks/ folder according to task numbers"
    echo " Usage:"
    echo -e "\t./locator.sh [option] (task number to start) (task number to finish)"
    echo " Example:"
    echo -e "\t./locator.sh -h  \tIt will show the help page"
    echo -e "\t./locator.sh 1 20\tIt will locate files from task 1 to task 20 in Tasks/ folder "
    echo -e "\t./locator.sh 11 11\tIt will locate files only from task 11 into Tasks/ folder "
    exit 0
fi

if [[ $# -lt 2 || $# -gt 2 ]]; then
    echo "Wrong number of arguments"
    exit 1
fi

for num in $(seq "$2" -1 "$1"); do    
    for student in Students/*; do
        for task in $student/*; do
            if [[ "$task" == *"$num"* && "$task" != *"checked"* ]]; then
                mv $task Tasks/Task_$num/Students
            fi
        done
    done
    echo "Task_$num"
done
echo "Done"
