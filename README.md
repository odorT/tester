# tester
tester is a tool for automatically checking multiple codes with multiple test cases in an easy way. Currently it is intended for python codes, but can easily be integrated to other programming languages.

## Requirements
- Bash version 4+ (tested in 4.4.20(1)-release)
- python3

## Installation
1. Just download source code to local machine

## Usage
### 1. You should upload a folder named "Students" to tester/.
This folder should have subdirectories with names like following:
```
Kamran_Karimov_Tasks
Name_Surname_Tasks
```
And those directories **must** have files like following:
```
task1_kamran_karimov.py
task10_name_surname.py
```
**If tasks are named different compared to examples above, program will not work properly in most cases.**
### 2. Run init.sh <num1> <num2>
init.sh will create create necessary folders. Also, it will create task folders starting from <num1> to <num2>
Following example will create Reports/ , Results/ , and Tasks/ folders. Tasks folder will include Task\_1, Task\_2 and Task\_3 subfolders.
```
./init.sh 1 3
```
