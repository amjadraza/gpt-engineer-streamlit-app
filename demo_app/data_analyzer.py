from dataclasses import dataclass
import pandas as pd

@dataclass
class DataAnalyzer:
    df: pd.DataFrame

    def get_summary(self):
        return self.df.describe()

    def get_column_names(self):
        return list(self.df.columns)
