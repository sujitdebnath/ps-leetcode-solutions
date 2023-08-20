import pandas as pd

def bonus_calculator(emp_id, name, salary):
    if emp_id%2 == 1 and name[0] != 'M':
        return salary
    else:
        return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: bonus_calculator(x['employee_id'], x['name'], x['salary']), axis=1)
    employees          = employees.sort_values(by=['employee_id'])
    
    return employees[['employee_id', 'bonus']]