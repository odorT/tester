#!/bin/bash

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "runit.sh is an automated script that calls all important scripts to get Reports."
    echo -e " Usage:\n\t./runit.sh [option] [task start number] [task end number]"
    echo -e " Example:\n\t./runit.sh\tIt will automate all tasks and create reports of all tasks"
    echo -e " \t./runit.sh 4 10\tIt will automate all tasks and create reports of task 4 to task 10"
    exit
fi

task_num=$(ls Tasks/ | wc -l)
starts=${1:-1}
ends=${2:-"$task_num"}

echo "from task "$starts" to task "$ends""

echo "locator.sh in progress"
source ./locator.sh $starts $ends

echo "compile.sh in progress"
source ./compiler.sh $starts $ends

echo "result_generator.sh in progress"
source ./result_generator.sh

echo "analyze.sh in progress"
source ./analyzer.sh $starts $ends
