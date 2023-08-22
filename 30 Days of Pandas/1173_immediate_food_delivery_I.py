import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_delivery = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    immediate_percentage = pd.DataFrame(
                                data=[round((immediate_delivery.shape[0] / delivery.shape[0])*100, 2)],
                                columns=['immediate_percentage'])
    
    return immediate_percentage