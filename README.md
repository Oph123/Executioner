# Executioner
An experiment to determine the difference in performance between model-based and model-free agents in a PDDL environment.

### stripper-main
This directory contains the files of the script used to convert PDDL domains with typing to domains based only on STRIPS. <br>
The script runs in the command line and alters PDDL files so they will require only STRIPS. <br>
To use the stripper, run the python script with the directory of pddl files:
```
python stripper <directory>
```
<br>
The script will go over all PDDL files in the directory and convert them. <br>
The script supports the following requirements:
```:strips```
```:typing```
```:negative-preconditions```
```:equality```
