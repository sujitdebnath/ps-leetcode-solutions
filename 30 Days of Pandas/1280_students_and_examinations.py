import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_sub    = pd.merge(students, subjects, how='cross')
    attended_exams = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    school_df                   = pd.merge(student_sub, attended_exams, on=['student_id', 'subject_name'], how='left')
    school_df                   = school_df.sort_values(by=['student_id', 'subject_name'])
    school_df['attended_exams'] = school_df['attended_exams'].fillna(0)

    return school_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]