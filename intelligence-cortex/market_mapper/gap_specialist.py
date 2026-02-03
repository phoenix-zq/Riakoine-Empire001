import pandas as pd
from dataclasses import dataclass

@dataclass
class KeyLevel:
    name: str
    top: float
    bottom: float

class GapSpecialist:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_opening_gaps(self):
        # Logic for NWOG, NDOG
        return [KeyLevel("NWOG_Example", 1.0500, 1.0510)]

    def get_fvgs(self):
        # Logic for FVG
        return [KeyLevel("Bullish_FVG", 1.0450, 1.0460)]
