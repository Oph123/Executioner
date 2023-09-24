import csv
import numpy as np
from tabulate import tabulate
with open('results.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    first_row = spamreader.__next__()
    success_index = first_row.index("success")
    learning_index = first_row.index("learning")
    wall_time_index = first_row.index("wall-time")
    print(first_row)
    print(success_index)

    mat = []

    for row in spamreader:
        mat.append(row)
mat = np.array(mat)

data = {}

for row in mat:
    agent, learning, status, wall_time = row[0], row[learning_index], row[success_index], row[wall_time_index]
    if agent not in data.keys():
        data[agent] = {'solved-problems': 0, 'running-wall-time': 0, 'learning-wall-time': 0, 'total-problems': 0, 'learning-count': 0, 'running-count': 0}
    
    if status == "True":
        data[agent]['solved-problems'] += 1
        data[agent]['total-problems'] += 1
    elif status == "False":
        data[agent]['total-problems'] += 1

    if learning == "True":
        data[agent]['learning-count'] += 1
        data[agent]['learning-wall-time'] += float(wall_time)
    else:
        data[agent]['running-count'] += 1
        data[agent]['running-wall-time'] += float(wall_time)    

def create_table(agent):
    total_problems = data[agent]['total-problems']
    solved_problems = data[agent]['solved-problems']
    solved_percentage = data[agent]['solved-problems'] / data[agent]['total-problems'] * 100
    average_running_wall_time = data[agent]['running-wall-time']/data[agent]['running-count']
    average_learning_wall_time = data[agent]['learning-wall-time']/data[agent]['learning-count']
    report = [
        ["Total problems", total_problems],
        ["Solved problems", solved_problems],
        ["Solved percentage", solved_percentage],
        ["Average running wall time", average_running_wall_time],
        ["Average learning wall time", average_learning_wall_time]
    ]
    return report

report = ""
for agent in data.keys():
    report += '\n' + f"Agent: {agent}" + '\n' + tabulate(create_table(agent), tablefmt="presto") + '\n'
print(report)

open('report.txt', 'w+').write(report)