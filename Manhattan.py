import pandas as pd
import numpy as np

p1 = np.array([1,2,3])
p2 = np.array([4,5,6])
s = 0
for i in range(3):
temp = abs(p1[i] - p2[i])
s = s + temp
print(f"Using Manhattan the distance will be {s}")

