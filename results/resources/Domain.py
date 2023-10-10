import pandas as pd
try:
    from resources.DomainParameter import DomainParameter
except:
    from DomainParameter import DomainParameter

def get_domain_database(name):
    database = pd.read_csv('results\master.csv').drop(columns=['stderr', 'perception-requests', 'actions', 'terminated'])
    return database[database.domain == name]



class Domain:

    def __init__(self, name, database: pd.DataFrame): # the database is pandas DataFrame
        self.name = name
        self.database = database
    
    def calculate_parameter(self, param: DomainParameter):
        return [param.name, param.function(self)]
    
    def get_domain_report(self, parameter_list: list[DomainParameter]):
        return {p.name: p.function(self) for p in parameter_list}
    
    def __str__(self):
        return f"DOMAIN OBJECT\nDomain name: {self.name}"


import os
print(os.getcwd())

DOMAINS = [Domain(t, get_domain_database(t)) \
                     for t in {x for x in pd.read_csv('results\master.csv').loc[:, 'domain'].tolist()}]