from resources.Agent import Agent
from resources.agent_parameters import PARAMETERS as params
from resources.agents import AGENTS as agents
from resources.AgentParameter import AgentParameter
from resources.Domain import Domain, DOMAINS
from resources.DomainParameter import DomainParameter
from resources.domain_paramaters import DOMAIN_PARAMS 
from tabulate import tabulate
import pandas as pd
from numpy import std, mean, median


def report_per_agent(agent_list: list[Agent], parameter_list: list[AgentParameter]):
    report = ""
    for agent in agent_list:
        report += '\n\n' + str(agent) + '\n' + tabulate(agent.get_agent_report(parameter_list).items())
    return report


def report_per_parameter(agent_list: list[Agent], parameter_list: list[AgentParameter]):
    report = ""
    for parameter in parameter_list:
        report += '\n\n' + str(parameter) + '\n' + tabulate(parameter.get_parameter_report(agent_list).items())
    return report


def report_table(agent_list: list[Agent], parameter_list: list[AgentParameter]):
    return tabulate({agent.name: agent.get_agent_report(parameter_list).items() for agent in agent_list}.items())


def domain_report(domain_list: list[Domain], parameter_list: list[DomainParameter]):
    report = ""
    for domain in domain_list:
        report += domain.name + "\n" + tabulate(domain.get_domain_report(parameter_list).items()) + "\n\n"
    return report


def mb_report(agent_list: list[Agent], parameter_list: list[AgentParameter], model_based: bool):
    new_list = [agent for agent in agent_list if agent.mb == model_based]
    df = pd.DataFrame(columns=[p.name for p in parameter_list], index=[a.name for a in new_list])
    for agent in new_list:
        df.loc[agent.name] = agent.get_agent_report(parameter_list)
    report = "=== Model Based Agents Report ===\n\n\n" if model_based else "=== Model Free Agents Report ===\n\n\n"
    for column in df:
        column_data = df[column].values
        column_dict = {'Mean': mean(column_data), 'Median': median(column_data), \
                       'Standard Deviation': std(column_data), 'Minimum': min(column_data), 'Maximum': max(column_data)}
        report += column + "\n" + tabulate(column_dict.items()) + '\n\n'
    return df

def main():
    open('agent_report.txt', 'w+').write(report_per_agent(agent_list=agents, parameter_list=params))


if __name__ == '__main__':
    main()