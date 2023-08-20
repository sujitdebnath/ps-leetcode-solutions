import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'], keep='first')
    employee = employee.nlargest(N, 'salary')[['salary']]

    if N > len(employee):
        employee = pd.DataFrame(data=None)
    else:
        employee = employee.iloc[[-1]]
    
    return employee