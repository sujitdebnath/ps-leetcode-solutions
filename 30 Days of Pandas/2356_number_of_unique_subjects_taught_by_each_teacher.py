import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_subs = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    unique_subs = unique_subs.rename(columns={'subject_id': 'cnt'})
    
    return unique_subs