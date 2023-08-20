import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'], keep='first')
    employee = employee.nlargest(2, 'salary')[['salary']]

    if len(employee) < 2:
        employee = pd.DataFrame(data=[None], columns=['SecondHighestSalary'])
    else:
        employee = employee.iloc[[-1]]
        employee = employee.rename(columns={'salary': 'SecondHighestSalary'})
    
    return employee