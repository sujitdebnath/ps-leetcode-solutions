import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login_activity = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login_activity = first_login_activity.rename(columns={'event_date': 'first_login'})
    
    return first_login_activity