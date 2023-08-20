import pandas as pd

def diabetes_condition(conditions):
    conditions_list = conditions.split(" ")

    for condition in conditions_list:
        if condition.startswith('DIAB1'):
            return True
    return False

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients['diabetes'] = patients.apply(lambda x: diabetes_condition(x['conditions']), axis=1)
    patients             = patients[patients['diabetes'] == True]

    return patients[['patient_id', 'patient_name', 'conditions']]