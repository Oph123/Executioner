try:
    from resources.Agent import Agent
except:
    from Agent import Agent
try:
    from resources.AgentParameter import AgentParameter
except:
    from AgentParameter import AgentParameter
try:
    from resources.Domain import DOMAINS, Domain
except:
    from Domain import DOMAINS, Domain
import pandas as pd 


def average(iter):
    return sum(iter)/len(iter)

def total_solved(agent: Agent): # number of solved problems
    success_column = agent.database.loc[:, 'success'].tolist()
    sum = 0
    for s in success_column:
        if s == True:
            sum += 1
    return sum 

def number_total(agent: Agent): # number of total problem attempts, not including learning runs
    success_column = agent.database.loc[:, 'success'].tolist()
    sum = 0
    for s in success_column:
        if s == True or s == False:
            sum += 1
    return sum


def time_mean(agent: Agent): # returns an average of wall times
    return agent.database.loc[:, 'wall-time'].mean()

def time_median(agent: Agent): # returns a median of wall times
    return agent.database.loc[:, 'wall-time'].median()

def time_std(agent: Agent): # returns the standard deviation of wall times
    return agent.database.loc[:, 'wall-time'].std()

def time_max(agent: Agent): # returns the maximum of wall times
    return agent.database.loc[:, 'wall-time'].max()

def time_min(agent: Agent): # returns the minimum of wall times
    return agent.database.loc[:, 'wall-time'].min()

def solved_percentage(agent: Agent):
    return total_solved(agent) / number_total(agent) 

def total_time(agent: Agent):
    return agent.database.loc[:, 'wall-time'].sum()

def total_learning_time(agent: Agent):
    valid_items = agent.database['learning'] == True
    print(valid_items)
    data = agent.database.loc[valid_items]
    return data.loc[:, 'wall-time'].sum()

def average_seconds_per_instance(agent: Agent): # average seconds per attempt
    return total_time(agent)/number_total(agent)

def average_learning_seconds_per_instance(agent): # average learning time per attempt
    return total_learning_time(agent)/number_total(agent)

"""def average_solved_instances_per_total_seconds(agent: Agent): # the average of: solved instances / total seconds spent on the problem
    data = {}
    for i in range(agent.database.shape[0]):
        data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']] = [0, 0] # wall-time, problems solved
    for i in range(agent.database.shape[0]):
        if agent.database.loc[i, 'success'] and not agent.database.loc[i, 'learning']:
            data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']][1] += 1
        data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']][0] += \
            agent.database.loc[i, 'wall-time'] if pd.notna(agent.database.loc[i, 'wall-time']) else 0
    
    return average([x[1]/x[0] for x in data.values() if x[0] != 0])
"""
"""def average_solved_instances_per_learning_seconds(agent: Agent): # the average of solved instances divided by 
                                                                # learning time, for every problem
    data = {}
    for i in range(1, agent.database.shape[0] + 1):
        data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']] = [0, 0] # learning wall time, problems solved
    for i in range(agent.database.shape[0]):
        if agent.database.loc[i, 'success'] and not agent.database.loc[i, 'learning']:
            data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']][1] += 1
        if agent.database.loc[i, 'learning']:
            data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']][0] += \
            agent.database.loc[i, 'wall-time'] if pd.notna(agent.database.loc[i, 'wall-time']) else 0
    
    return average([x[1]/x[0] for x in data.values() if x[0] != 0])

def average_solved_per_instance(agent: Agent): # returns the average of values calculated as follows:
                                               # number of succesful instance attempts in a problem / the number of instances in a problem
    data = {}
    for i in range(agent.database.shape[0]):
        data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']] = 0 # counter for solved problems
    for i in range(agent.database.shape[0]):
        if agent.database.loc[i, 'success'] and agent.database.loc[i, 'learning'] == False:
            data[agent.database.loc[i, 'domain'] + '_' + agent.database.loc[i, 'problem']] += 1
    return average(data.values()) / 10 # divide by 10 to account for 10 instance in every problem"""
    
        
def average_solved_instances_per_total_seconds(agent: Agent):
    domains = [d.name for d in DOMAINS]
    instances = ['instance-' + str(i) for i in range(1, 6)]
    data = []
    for domain in domains:
        for instance in instances:
            new_df = agent.database.loc[(agent.database['problem'] == instance) & (agent.database['domain'] == domain)]
            successes = new_df.loc[:, 'success'].sum()
            total_problem_time = new_df.loc[:, 'wall-time'].sum()
            data.append(successes/total_problem_time) 
    return pd.Series(data).mean()



parameters = {
    "Wall times mean": time_mean,
    "Wall times median": time_median,
    "Wall times standard deviation": time_std,
    "Wall times minimum": time_min,
    "Wall times maximum": time_max,
    "Total number of succesful instance attempts": total_solved,
    "Total number of instance attempts": number_total,
    "Percentage of succesful attempts (out of 1)": solved_percentage,
    "Total spent time": total_time,
    "Total spent learning time": total_learning_time,
    "Average time spent on an attempt": average_seconds_per_instance,
    "Average learning time spent on an attempt": average_learning_seconds_per_instance,
    "Average of the ratios between number of problems solved succesfuly and total time spent on the problem": \
        average_solved_instances_per_total_seconds,
    #"Average of the ratios between number of problems solved succesfuly and total learning time spent on the problem": \
    #    average_solved_instances_per_learning_seconds,
    #"Average of the percentages of succesful instances in every problem (out of 1)": average_solved_per_instance
}

PARAMETERS = [AgentParameter(key, value) for key, value in parameters.items()]
