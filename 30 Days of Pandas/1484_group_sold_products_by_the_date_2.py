import pandas as pd

def products_list(products):
    return ','.join(sorted(products.unique()))

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    sold_products = activities.groupby('sell_date')['product'].agg([
                        ('num_sold', 'nunique'),
                        ('products', lambda x: products_list(x))
                    ]).reset_index()

    return sold_products