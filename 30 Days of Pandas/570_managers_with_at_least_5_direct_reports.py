import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers         = employee.groupby('managerId').size().reset_index(name='direct_reports')
    managers         = managers[managers['direct_reports'] >= 5]
    managers_details = pd.merge(managers, employee, left_on='managerId', right_on='id', how='inner')

    return managers_details[['name']]