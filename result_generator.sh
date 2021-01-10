#!/bin/bash 

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "This script generates results which is used  for analyzer.sh script."
    echo " Usage:"
    echo -e "\t./result_generator.sh [option]"
    echo " Example:"
    echo -e "\t./result_generator.sh -h\tIt will show the help page"
    echo -e "\t./result_generator.sh\tIt will generate results and update all files in Results/ folder"
    exit 0
fi

for task in Tasks/*; do
    
    touch "$task"_results.txt
    echo -n "" > "$task"_results.txt

    for answer in "$task"/Answers/*; do
        for output in "$task"/Outputs/*; do
            echo -en "$output\t\t" >> "$task"_results.txt
            cmp $answer $output >> "$task"_results.txt
            echo "" >> "$task"_results.txt
        done
    done
	echo "$task" | cut -d "/" -f2
	mv "$task"_results.txt Results/
done
echo "Done"
