try:
    from resources.DomainParameter import DomainParameter
except:
    from DomainParameter import DomainParameter
try:
    from resources.Domain import Domain, get_domain_database
except:
    from Domain import Domain, get_domain_database
import pandas as pd 
def time_mean(domain: Domain): # returns an average of wall times
    return domain.database.loc[:, 'wall-time'].mean()

def time_median(domain: Domain): # returns a median of wall times
    return domain.database.loc[:, 'wall-time'].median()

def time_std(domain: Domain): # returns the standard deviation of wall times
    return domain.database.loc[:, 'wall-time'].std()

def time_max(domain: Domain): # returns the maximum of wall times
    return domain.database.loc[:, 'wall-time'].max()

def time_min(domain: Domain): # returns the minimum of wall times
    return domain.database.loc[:, 'wall-time'].min()


DOMAIN_PARAMS = [DomainParameter(key, value) for key, value in 
                 {"Time mean": time_mean, "Time median": time_median, "Time standard deviation": time_std, "Time max": time_max, "Time min": time_min}.items()]
