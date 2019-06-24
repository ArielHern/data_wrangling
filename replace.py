import pandas as pd
import numpy as np


class Replace:
    """Class to manage replaments"""

    def __init__(self, filename):

        self.filename = filename

    def missing_data(self):
        """Count missing values in each column"""
        missing_data = df.isnull()

        for column in missing_data.columns.values.tolist():
            print(column)
            print(f'{missing_data[column].value_counts()} \n')

    def replace_question_mark(self):
        df.replace('?', np.nan, inplace=True)
