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
### 2. Run init.sh 'num1' 'num2'
Before trying to execute scripts, they should have execution permissions. For that, copy and run the following command.
```
chmod +x analyzer.sh checker.sh compiler.sh init.sh locator.sh result_generator.sh runit.sh
```
init.sh will create create necessary folders. Also, it will create task folders starting from 'num1' to 'num2'
Following example will create Reports/ , Results/ , and Tasks/ folders. Tasks folder will include Task\_1, Task\_2 and Task\_3 subfolders.
```
./init.sh 1 3
```
### 2. Run checker.sh
For testing codes you should have test cases and the sample answers of them. For creating them, change directory to proper Task folder. For input cases, change directory to Inputs/ folder. Here, create input.txt files with test case in it. Following example indicates how it should be done for Task\_1.
```
cd Tasks/Task_1/Inputs
touch input1.txt input2.txt
```
Note that you can create multiple input cases. After that change directory to Answers folder. Here, you should create one answer.txt file and fill it with the correct answers. Following example shows how it should be done:
```
cd Tasks/Task_1/Asnwers
touch answer.txt
```
**NOTE** Let's assume that we have python code which finds the product of two integer inputs, and we have two input cases like following:
code:
```
print(int(input()) + int(input()))
```
input1.txt:
```
1
2
```
input2.txt:
```
3
4
```
**Note that in answer.txt you should put new lines after each answer(even after last one). Following that, the answer.txt should be like following:**
```
2

12

```

After all, run checker.sh 
```
./checker.sh
```
You can specify which Task folders to check. By default without any arguments it will check all Task folders. For example, following example will check only Task_1 folder:
```
./checker.sh 1 1
```
### 3. Run runit.sh
runit.sh will
1. (locator.sh) locate tasks by their task numbers from Students/ folder to Tasks/ folder
2. (compiler.sh) run and save the outputs of codes to Tasks/Outputs folder
3. (result_generator.sh) compare answer.txt with the outputs files and save the differences in Results/ folder.
4. (analyzer.sh) create analyzed reports in Reports/ folder. Lines that start with '+' sign indicates that the code is correct. If the output and answer files are different, it will show both of them to check the output manually.
For all of the above, simply run:
```
./runit.sh
```
By default it will check all Tasks. If you want to specify which Tasks to check, run following:
```
./runit.sh 1 2
```
The example above will create reports based on Task_1 and Task_2


## Notes
1. It is suggested to start task numbers from 1. (e.g. Task_1 Task_2 Task_3 ...)
2. Strictly follow the rules of task file names and task folder names.
    2.1 Task folder example: Name_Surname_Tasks
    2.2 Task file example: task1_name_surname_Tasks

