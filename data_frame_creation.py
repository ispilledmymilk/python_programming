import pandas as pd
import numpy as np

d = {"cal" : [420, 380, 390],
    "dur" : [50, 80, 90]}

x = pd.DataFrame(d, index = ["star", "moon", "di"])
print(x)
