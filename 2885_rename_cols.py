# [EASY][Pandas] https://leetcode.com/problems/rename-columns
# Completed 2026/03/17
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'id': 'student_id'})
    students = students.rename(columns={'first': 'first_name'})
    students = students.rename(columns={'last': 'last_name'})
    students = students.rename(columns={'age': 'age_in_years'})

    return students