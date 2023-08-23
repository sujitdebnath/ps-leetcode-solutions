import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    salary_categories = ["Low Salary", "Average Salary", "High Salary"]
    low_salary        = accounts[accounts['income'] < 20000].shape[0]
    average_salary    = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
    high_salary       = accounts[accounts['income'] > 50000].shape[0]
    
    accounts_category = pd.DataFrame({
        'category': salary_categories,
        'accounts_count': [low_salary, average_salary, high_salary]
    })

    return accounts_category