

class AgentParameter:
    def __init__(self, name: str, function): # the function accepts an Agent and uses Agent.database
        self.name = name
        self.function = function
    
    def get_parameter_report(self, agent_list) -> dict:
        return {agent.name: self.function(agent) for agent in agent_list}
    
    def __str__(self) -> str:
        return f'AGENT PARAMETER OBJECT\nName: {self.name}\nFunction: {self.function}'