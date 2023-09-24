

class DomainParameter:
    def __init__(self, name: str, function): # the function accepts a Domain and uses Domain.database
        self.name = name
        self.function = function
    
    def get_parameter_report(self, domain_list) -> dict:
        return {domain.name: self.function(domain) for domain in domain_list}
    
    def __str__(self) -> str:
        return f'AGENT PARAMETER OBJECT\nName: {self.name}\nFunction: {self.function}'