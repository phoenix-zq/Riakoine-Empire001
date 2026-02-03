import pandas as pd

class MarketMapper:
    def __init__(self, data: pd.DataFrame):
        self.df = data 

    def get_institutional_structure(self):
        return { "YEARLY_HIGH": self.df['high'].max() }
