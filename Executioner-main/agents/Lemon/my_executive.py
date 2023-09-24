import os
import sys

import static
from executing_executor import ExecutingExecutor
from learning_executor import LearningExecutor
from pddlsim.local_simulator import LocalSimulator

for dir in static.get():
    if not os.path.exists(dir):
        os.mkdir(dir)
flag = sys.argv[1]
domain_path = sys.argv[2]
problem_path = sys.argv[3]
if flag == '-L':
    while True:
        print LocalSimulator().run(domain_path, problem_path, LearningExecutor())
elif flag == '-E':
    print LocalSimulator().run(domain_path,problem_path, ExecutingExecutor())
else:
    raise NameError("Wrong flag")
