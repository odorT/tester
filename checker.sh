#!/bin/bash

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
    exit 1
fi
