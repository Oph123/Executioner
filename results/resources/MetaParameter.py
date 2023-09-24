from Agent import Agent
from AgentParameter import AgentParameter
class MetaParameter:
    def __init__(self, parameter: AgentParameter): 
        self.name = parameter.name
        self.function = parameter.function

    def get_meta_paramater_report(self, agent_list: list[Agent]):
        results = {'MB': 0, 'MF': 0}
        count_mb = 0
        count_mf = 0
        for agent in agent_list:
            if agent.mb:
                count_mb += 1
                results['MB'] += self.function(agent)
            else:
                count_mf += 1
                results['MF'] += self.function(agent)
        results['MB'] /= count_mb
        results['MF'] /= count_mf
        return results

    
