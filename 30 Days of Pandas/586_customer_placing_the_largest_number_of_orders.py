import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_count = orders.groupby('customer_number')['order_number'].count().nlargest(1).reset_index()
    return orders_count[['customer_number']]
