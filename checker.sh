#  TODOS
# checking if inputs and answers are provided
# unzipping students folder and replacing it
# creating task folders.
#!/bin/bash

for task in Tasks/*; do
    if [[ -z "$task"/Inputs ]]; then
        echo ""$task"/Inputs folder is empty"; fi

    if [[ -z "$task"/Answers ]]; then
        echo ""$task"/Inputs folder is empty"; fi

    if [[ -z "$task"/Students ]]; then
        echo ""$task"/Inputs folder is empty"
    fi
done
