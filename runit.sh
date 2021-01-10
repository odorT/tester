#!/bin/bash

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "runit.sh is an automated script that calls all important scripts to get reports. Check Reports/ folder for them."
    echo -e " Usage:\n\t./runit.sh [option] [task start number] [task end number]"
    echo -e " Example:\n\t./runit.sh\tIt will automate all tasks and create reports of all tasks"
    echo -e " \t./runit.sh -h\tIt will show the help page"
    echo -e " \t./runit.sh -v\tIt will show all execution messages"
    echo -e " \t./runit.sh 4 10\tIt will automate all tasks and create reports of task 4 to task 10"
    echo -e " \t./runit.sh 5 5\tIt will automate all tasks and create report of task 5"
    exit
fi

task_num=$(ls Tasks/ | wc -l)
starts=${1:-1}
ends=${2:-"$task_num"}

if [[ "$3" == "-v" || "$3" == "--verbose" ]]; then
    echo "from task "$starts" to task "$ends""

    echo "locator.sh locating all files from Students/ folder to Tasks_Task_<num>/Students"
    source ./locator.sh $starts $ends

    echo "compile.sh running and saving outputs in Tasks/Task_<num>/Outputs"
    source ./compiler.sh $starts $ends

    echo "result_generator.sh generating results file in Results/ folder"
    source ./result_generator.sh

    echo "analyzer.sh creating final reports of codes"
    source ./analyzer.sh $starts $ends
else
    echo "from task "$starts" to task "$ends""
    source ./locator.sh $starts $ends
    source ./compiler.sh $starts $ends
    source ./result_generator.sh
    source ./analyzer.sh $starts $ends
fi
