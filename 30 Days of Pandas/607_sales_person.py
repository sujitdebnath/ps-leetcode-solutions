import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    if 'RED' in company['name'].unique():
        company_red_id = company[company['name'] == 'RED']['com_id'].squeeze()
    else:
        company_red_id = None
    
    red_ord_sales_id     = orders[orders['com_id'] == company_red_id]['sales_id'].unique()
    sales_person_not_red = sales_person[~sales_person['sales_id'].isin(red_ord_sales_id)]

    return sales_person_not_red[['name']]