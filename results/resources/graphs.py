import pandas as pd
try:
    from Agent import Agent, get_agent_database
except:
    from resources.Agent import Agent, get_agent_database
try: 
    from agent_parameters import PARAMETERS
except:
    from resources.agent_parameters import PARAMETERS
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import matplotlib.gridspec as gspc
from agents import AGENTS
import os.path as pth

#list of agents but with databases that include only lines with learning set to False
agents_exec = [Agent(agent.name, get_agent_database(agent.name, False), agent.mb) for agent in AGENTS]

exclude_params = {'Total spent time'}
params = [p for p in PARAMETERS if p.name not in exclude_params]
colors = list(clr.BASE_COLORS.keys())



def plot_model_based_histogram():
    mb = [agent for agent in agents_exec if agent.mb]
    data_mb = pd.DataFrame( # create dataframe with wall times of agents
    [[x for x in agent.database.loc[:, 'wall-time'].tolist() 
     if agent.database.loc[:, 'wall-time'].quantile(0.05) <= x and # filter out 0.95 <= percentile
     agent.database.loc[:, 'wall-time'].quantile(0.95) >= x] for agent in mb] # filter out percentile <= 0.05
    ).T
    data_mb.columns = [agent.name for agent in mb]
    mbfig, mbax = plt.subplots(figsize=(12, 10))
    mbfig.add_gridspec(1, 1, 
                       bottom=0.3)
    mbax.hist(data_mb, histtype='bar', bins=10, color=colors[:len(mb)], label=[a.name for a in mb])
    mbax.set_xlabel('זמן קיר בשניות'[::-1])
    mbax.set_title('פילוג אמפירי של זמני הפתרון בסוכנים מבוססי המודלים'[::-1])
    mbax.legend(bbox_to_anchor=(1.02, 1))
    plt.show()


def plot_model_free_histogram():
    mf = [agent for agent in agents_exec if not agent.mb]
    data_mf = pd.DataFrame( # create dataframe with the wall times of agents
    [[x for x in agent.database.loc[:, 'wall-time'].tolist() 
        if agent.database.loc[:, 'wall-time'].quantile(0.05) <= x and # filter out 0.95 <= percentile
        agent.database.loc[:, 'wall-time'].quantile(0.95) >= x] for agent in mf] # filer out percentile <= 0.05
    ).T
    data_mf.columns = [agent.name for agent in mf]
    mffig, mfax = plt.subplots(figsize=(12, 10))
    mfax.hist(data_mf, histtype='bar', bins=10, color=colors[:len(mf)], label=[a.name for a in mf])
    mfax.set_xlabel('זמן הקיר בשניות'[::-1])
    mfax.set_title('פילוג אמפירי של זמני הפתרון בסוכנים שאינם מבוססי מודלים'[::-1])
    mfax.legend(bbox_to_anchor=(1.02, 1))
    plt.show()

def plot_bars_per_agents():
    for agent in AGENTS:
        data = pd.DataFrame({key: [value] for key, value in agent.get_agent_report(params).items()})
        data.columns = [p.name for p in params]
        print(data)
        data.plot.bar()
        plt.legend(bbox_to_anchor=(1.02, 1))
        plt.show()


def plot_bars_per_parameters(): # saves results in graphs\plots_per_parameter
    for param in PARAMETERS:
        fig = plt.figure(figsize=(12, 7))
        data = pd.DataFrame({key: [value] for key, value in param.get_parameter_report(AGENTS).items()}).T
        data.index = [a.name + '\n' + a.mb*'MB' + (not a.mb)*'MF'  for a in AGENTS]
        gs = fig.add_gridspec(1, 1, bottom=0.15, top=0.9)
        ax = fig.add_subplot(gs[0, 0])
        data.plot.bar(ax=ax)
        ax.get_legend().remove()
        plt.title(param.name)
        file = open('resources\graphs\plots_per_parameter\\' + param.name + '.png', 'wb+')
        plt.savefig(file)
        

def main():
    plot_bars_per_parameters()

if __name__ == '__main__':
    main()