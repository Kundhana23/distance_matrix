import pandas as pd
import numpy as np

p1 = np.array([1,2,3])
p2 = np.array([4,5,6])
s = 0
for i in range(3):
temp = p1[i] - p2[i]
s = s + (temp)**2
print(f"Using Euclidean distance the distance will be {s**0.5}")