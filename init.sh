#!/bin/bash

for i in $@; do
    mkdir Tasks/Task_"$i"
    mkdir Tasks/Task_"$i"/Answers
    mkdir Tasks/Task_"$i"/Outputs
    mkdir Tasks/Task_"$i"/Inputs
    mkdir Tasks/Task_"$i"/Students
done
