import pandas as pd
import numpy as np

x = {"day1" : 234, "day2" : 432, "day3" : 343}
s = pd.Series(x, index = ["day1", "day2", "day3"])      #this is to specify the index
print(s)        #prints the entire series
print(s["day1"])        #prints the element wrt the index mentioned

w = pd.Series(x, index = ["day1", "day2"])      #this is to selectively print the dictionary
print(w)
