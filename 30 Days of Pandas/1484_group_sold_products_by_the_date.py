import pandas as pd

def products_list(products_df):
    return ','.join(products_df.sort_values(by='product')['product'].tolist())

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities_df = activities.drop_duplicates()

    sold_products     = pd.DataFrame({'sell_date': activities_df['sell_date'].unique()})
    num_sold_products = activities_df.groupby('sell_date')['product'].count().reset_index(name='num_sold')
    sold_products_all = pd.merge(sold_products, num_sold_products, on='sell_date', how='left')

    sold_products_all['products'] = sold_products_all.apply(lambda x: products_list(activities_df[activities_df['sell_date']==x['sell_date']]), axis=1)
    sold_products_all             = sold_products_all.sort_values(by='sell_date')

    return sold_products_all