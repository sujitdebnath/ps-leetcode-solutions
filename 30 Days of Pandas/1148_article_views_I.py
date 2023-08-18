import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    author_self_view = views[views['author_id'] == views['viewer_id']]
    author_self_view = author_self_view.drop_duplicates(subset=['author_id'], keep='first')
    author_self_view = author_self_view.rename(columns={'author_id': 'id'})
    author_self_view = author_self_view.sort_values(by=['id'])

    return author_self_view[['id']]