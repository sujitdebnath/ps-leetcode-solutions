import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    lead_id_df         = daily_sales.groupby(['date_id', 'make_name'])['lead_id'].nunique().reset_index()
    unique_partners_df = daily_sales.groupby(['date_id', 'make_name'])['partner_id'].nunique().reset_index()

    out_daily_sales_df = pd.merge(lead_id_df, unique_partners_df, on=['date_id', 'make_name'], how='inner')
    out_daily_sales_df = out_daily_sales_df.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})

    return out_daily_sales_df