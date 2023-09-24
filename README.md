# Executioner
An experiment to determine the difference in performance between model-based and model-free agents in PDDLsim, a Python PDDL environment created by .

### stripper-main
This directory contains the files of the script used to convert PDDL domains with typing to domains based only on STRIPS. <br>
The script runs in the command line and alters PDDL files so they will require only STRIPS. <br>
To use the stripper, run the python script with the directory of pddl files:
```
python stripper <directory>
```
The script will go over all PDDL files in the directory and convert them. <br>
The script supports the following requirements:
```
  :strips
```
<br>
```
  :typing
```
<br>
```
  :negative-preconditions
```
<br>
```
  :equality
```
<br><br>
### uncerainator-main
This directory contains the script used to convert deterministic domains to tochastic domains.<br>
The script operates on domain and problem files, and it injects predicates into the domains and problems. These predicates are added in the effects of actions in the domain, and in the initial/goal conditions of the problem. This creates the randomness of the problems. <br>
The uncertainator is used as follows:
```
python uncertainator group [--suffix TEXT] DIRECTORY INJECTION_COUNT
```
Where 
