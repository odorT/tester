#!/bin/bash

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo checker.sh checks if all necessary files exists and in proper folder.
    echo -e " Usage:\n\t./checker.sh [task numbers]"
    echo -e " Example:\n\t./checker.sh\t\tIt will check wheter all files are provided or not"
    echo -e "\t./checker.sh 1 3\tIt will check if all files are provided in Task_1 Task_2 and Task_3"
    exit 
fi

task_num=$(ls Tasks/ | wc -l)
starts=${1:-1}
ends=${2:-"$task_num"}
if [[ "$ends" -gt task_num ]]; then
    ends=$task_num
fi

for task in $(seq "$starts" "$ends"); do
    path=Tasks/Task_"$task"
    flag=0
    if [[ -z "$(ls -A "$path"/Inputs)" ]]; then
        echo ""$task"/Inputs folder is empty"; fi

    if [[ -z "$(ls -A "$path"/Answers)" ]]; then
        echo ""$task"/Answers folder is empty"
    fi
done

if [[ "$flag" == 0 ]]; then
    echo "All files exists"
    exit 1
fi
