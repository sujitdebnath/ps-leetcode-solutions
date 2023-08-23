import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees.apply(lambda x: x['out_time']-x['in_time'], axis=1)
    employees_total_spent   = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    employees_total_spent   = employees_total_spent.rename(columns={'event_day': 'day'})
    
    return employees_total_spent