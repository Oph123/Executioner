import pandas as pd
try:
    from resources.AgentParameter import AgentParameter
except: 
    from AgentParameter import AgentParameter

# CONSTANTS: The data from these domains and agents will not be taken into account in the final results
AGENTS_TO_IGNORE = ['Cornbread']

def get_agent_database(name, get_learning): # if get_learning i set to false then lines with learning=True will not be included 
    database = pd.read_csv('master.csv').drop(columns=['stderr', 'perception-requests', 'actions', 'terminated'])
    valid_items = (database['agent'] == name) & ((database['learning'] == False) | (database['learning'] == get_learning))
    database = database.loc[valid_items]
    database.sort_values(by='wall-time')
    return database



class Agent:

    def __init__(self, name, database: pd.DataFrame, mb: bool): # the database is pandas DataFrame
        self.name = name
        self.database = database
        self.mb = mb
    
    def calculate_parameter(self, param: AgentParameter):
        return [param.name, param.function(self)]
    
    def get_agent_report(self, parameter_list: list[AgentParameter]):
        return {p.name: p.function(self) for p in parameter_list}
    
    def __str__(self):
        return f"AGENT OBJECT\nAgent name: {self.name}\nMB: {self.mb}"
    
    


    
