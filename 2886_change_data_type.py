# [EASY] https://leetcode.com/problems/change-data-type
# Completed 2026/03/17
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int')
    return students