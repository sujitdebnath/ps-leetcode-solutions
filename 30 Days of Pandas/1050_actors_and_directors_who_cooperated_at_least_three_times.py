import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director_coop       = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    actor_director_coop_three = actor_director_coop[actor_director_coop['timestamp'] >= 3]

    return actor_director_coop_three[['actor_id', 'director_id']]