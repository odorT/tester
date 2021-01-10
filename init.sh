#!/bin/bash

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo This script creates all necessary folders. Before running runit.sh, you should run init.sh.
    echo -e " Usage:\n\t./init.sh [task numbers]"
    echo -e " Example:\n\t.init.sh 1 1\tIt will create Task_1 folder with its subdirectories in Tasks folder"
    echo -e "\t.init.sh 1 3\tIt will create Task_1 Task_2 Task_3 folders with its subdirectories in Tasks folder"
    exit
fi

mkdir Reports/ Results/ Tasks/ 2> /dev/null

for task in $(seq "$1" "$2"); do
    path=Tasks/Task_"$task"

    mkdir "$path"
    mkdir "$path"/Answers
    mkdir "$path"/Students
    mkdir "$path"/Outputs
    mkdir "$path"/Inputs
done
