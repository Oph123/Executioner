import pandas as pd
try:
    from Agent import Agent, get_agent_database
except:
    from resources.Agent import Agent, get_agent_database
try: 
    from agent_parameters import PARAMETERS
except:
    from resources.agent_parameters import PARAMETERS
try:
    from resources.Domain import DOMAINS, Domain
except:
    from Domain import DOMAINS, Domain
from domain_paramaters import DOMAIN_PARAMS

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
    mbfig = plt.figure(figsize=(12, 7))
    gs = mbfig.add_gridspec(1, 1, right=0.85, bottom=0.1)
    mbax = mbfig.add_subplot(gs[0, 0])
    plt.hist(data_mb, stacked=False, color=colors[:len(mb)], label=[a.name for a in mb])
    mbax.set_xlabel('זמן קיר בשניות'[::-1])
    mbax.set_title('פילוג אמפירי של זמני הפתרון בסוכנים מבוססי המודלים'[::-1])
    plt.legend(bbox_to_anchor=(1.02, 1))
    file = open('resources\graphs\model_based_histogram.png', 'wb+')
    plt.savefig(file)


def plot_model_free_histogram():
    mf = [agent for agent in agents_exec if not agent.mb]
    data_mf = pd.DataFrame( # create dataframe with the wall times of agents
    [[x for x in agent.database.loc[:, 'wall-time'].tolist() 
        if agent.database.loc[:, 'wall-time'].quantile(0.05) <= x and # filter out 0.95 <= percentile
        agent.database.loc[:, 'wall-time'].quantile(0.95) >= x] for agent in mf] # filer out percentile <= 0.05
    ).T
    data_mf.columns = [agent.name for agent in mf]
    mffig = plt.figure(figsize=(12, 7))
    gs = mffig.add_gridspec(1, 1, right=0.85, bottom=0.1)
    mbax = mffig.add_subplot(gs[0, 0])
    plt.hist(data_mf, stacked=False, color=colors[:len(mf)], label=[a.name for a in mf])
    mbax.set_xlabel('זמן קיר בשניות'[::-1])
    mbax.set_title('פילוג אמפירי של זמני הפתרון בסוכנים מבוססי המודלים'[::-1])
    plt.legend(bbox_to_anchor=(1.02, 1))
    file = open('resources\graphs\model_free_histogram.png', 'wb+')
    plt.savefig(file)

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


def plot_domain_bars_per_parameters():
    for param in DOMAIN_PARAMS:
        fig = plt.figure(figsize=(12, 7))
        data = pd.DataFrame({key: [value] for key, value in param.get_parameter_report(DOMAINS).items()}).T
        data.index = [d.name.split('-')[0] for d in DOMAINS]
        gs = fig.add_gridspec(1, 1, bottom=0.15, top=0.9)
        ax = fig.add_subplot(gs[0, 0])
        data.plot.bar(ax=ax)
        ax.get_legend().remove()
        plt.title(param.name)
        file = open('resources\graphs\domains\\' + param.name.split('-')[0] + '.png', 'wb+')
        plt.savefig(file)


def main():
    plot_bars_per_parameters()
    plot_domain_bars_per_parameters()
    plot_model_based_histogram()
    plot_model_free_histogram()


if __name__ == '__main__':
    main()