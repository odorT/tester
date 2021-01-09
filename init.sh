#!/bin/bash

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo This script creates task folders. Before running runit.sh, you should run init.sh.
    echo -e " Usage:\n\t./init.sh [task numbers]"
    echo -e " Example:\n\t.init.sh 1\tIt will create Task_1 folder with its subdirectories in Tasks folder"
    echo -e "\t.init.sh 1 2 3\tIt will create Task_1 Task_2 Task_3 folders with its subdirectories in Tasks folder"
    exit
fi
for i in $@; do
    mkdir Tasks/Task_"$i"
    mkdir Tasks/Task_"$i"/Answers
    mkdir Tasks/Task_"$i"/Outputs
    mkdir Tasks/Task_"$i"/Inputs
    mkdir Tasks/Task_"$i"/Students
done
