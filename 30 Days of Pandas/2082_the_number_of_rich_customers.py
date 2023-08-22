import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_customer = store[store['amount'] > 500]
    rich_count_df = pd.DataFrame(data=[rich_customer['customer_id'].unique().size], columns=['rich_count'])
    
    return rich_count_df