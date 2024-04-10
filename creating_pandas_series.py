import pandas as pd
import numpy as np

x = np.array([10, 12, 56])
s1 = pd.Series(x)
print(s1)

y = [1, 7, 6]
s2 = pd.Series(y)
print(s2)

z = {"num1" : 4, "num2" : 5, "num3" : "num"}
s3 = pd.Series(z)
print(s3)
