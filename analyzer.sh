#!/bin/bash 
if [[ $# -lt 1 ]]; then
	echo "Error: Not enough arguments" >&2; exit 0

elif [[ $1 == "-h" || $1 == "--help" ]]; then
	echo "analyzer.sh is a script for creating reports based on task results with detailed information.\
 Reports will be saved in Reports/ folder."
	echo -e "  Usage:\n\t./analyzer [option] [task numbers]"
	echo -e "  Examle:\n\t./analyzer -h\tIt will show the help page of analyzer.sh"
	echo -e "\t./analyzer 1\tIt will create a report of task 1 in Reports/ folder"
	echo -e "\t./analyzer 1 20\tIt will create reports from task 1 to task 20 separately in Reports/ folder"

	exit 1

fi

for i in $(seq "$1" "$2"); do
	if [ -z "${i##*[!0-9]*}" ]; then
		echo "Error: Not a number" >&2; exit 2
	fi

	touch Reports/task"$i".txt
	echo -n '' > Reports/task"$i".txt

	while read line; do
		if [[ "$line" =~ "Answer" ]]; then
				
			output=$(echo $line | cut -d " " -f1)
			answer=$(echo $line | cut -d " " -f2)

			echo -n "- " >> Reports/task"$i".txt
			echo -n $line | cut -d "_" -f 3,4 | cut -d "." -f1 >> Reports/task"$i".txt
			echo "######### Output: #########" >> Reports/task"$i".txt; echo "" >> Reports/task"$i".txt
			cat "$output" >> Reports/task"$i".txt
			echo "######### Answer: #########" >> Reports/task"$i".txt; echo "" >> Reports/task"$i".txt
			cat "$answer" >> Reports/task"$i".txt	
			echo "###########################" >> Reports/task"$i".txt
		
		elif [[ "$line" != "" ]]; then
			echo -n "+ " >> Reports/task"$i".txt
			echo -n $line | cut -d "_" -f 3,4 | cut -d "." -f1 >> Reports/task"$i".txt
		fi
	done < Results/Task_"$i"_results.txt
    echo "."
done
echo "Done"
