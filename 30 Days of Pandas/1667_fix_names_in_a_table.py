import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(lambda x: x[0].upper()+x[1:].lower())
    users         = users.sort_values(by=['user_id'])

    return users