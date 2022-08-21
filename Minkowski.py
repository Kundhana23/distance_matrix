import pandas as pd
import numpy as np

#Assume q = 1
q = 2
#Here k =3
s = 0
p1 = np.array([1,2,3])
p2 = np.array([4,5,6])
for i in range(3):
temp = (abs(p1[i] - p2[i]))**q
s = s + temp
l = s**(1/q)
print(f"Using Minkowski the distance will be {l}")