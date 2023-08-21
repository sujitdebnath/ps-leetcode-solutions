import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if not employee.empty and not department.empty:
        dept_max_salary_df     = employee.groupby('departmentId')['salary'].max()
        employee['max_salary'] = employee.apply(lambda x: True if x['salary']==dept_max_salary_df[x['departmentId']] else False, axis=1)
        employee_max_df        = employee[employee['max_salary']==True]
        output_df              = pd.merge(employee_max_df, department, left_on='departmentId', right_on='id', how='inner')
        output_df              = output_df.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
        
        return output_df[['Department', 'Employee', 'Salary']]
    else:
        return pd.DataFrame(data=None, columns=['Department', 'Employee', 'Salary'])