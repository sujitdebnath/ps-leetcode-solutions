import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    desire_classes = courses.groupby('class')['student'].size().reset_index()
    desire_classes = desire_classes[desire_classes['student'] >= 5]

    return desire_classes[['class']]
