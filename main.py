import os
from pathlib import Path

import sklearn
import numpy as np
import pandas as pd

filepath = Path(__file__).resolve().parent
print(filepath)

df = pd.read_csv(filepath / 'cols.tbl.csv')
print('df.shape', df.shape)
