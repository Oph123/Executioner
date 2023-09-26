try:
    from resources.Agent import Agent, get_agent_database
except:
    from Agent import Agent, get_agent_database

agent_names = {
    "Ostkaka": 'mf',
    #"Black_Forest": 'mb',
    "Brownie": 'mb',
    "Crystal": 'mb',
    "Flan": 'mf',
    "Carrot": 'mb',
    "Suncake": 'mf',
    #"Gingerbread": 'mb',
    "Blackout": 'mb',
    "Cornbread": 'mf',
    "Spit": 'mf',
    #"Pancake": 'mf',
    #'Lemon': 'mb',
    #'Mango_BQL': 'mf'
}

AGENTS = [Agent(key, get_agent_database(key, True), value == 'mb') for key, value in agent_names.items()]

