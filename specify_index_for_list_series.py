import pandas as pd
import numpy as np

x = [540, 555, 456]
s = pd.Series(x, index = ["day1", "day2", "day3"])      #this is to specify the index
print(s)        #prints the entire series
print(s["day1"])        #prints the element wrt the index mentioned
