import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    all_customers         = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    customers_with_no_ord = all_customers[all_customers['customerId'].isnull()]
    customers_with_no_ord = customers_with_no_ord.rename(columns={'name': 'Customers'})

    return customers_with_no_ord[['Customers']]