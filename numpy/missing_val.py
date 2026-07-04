# nan


import numpy as np

# np.isnan(arr) --> to detect the nan 

arr = np.array([1,2,3,np.nan,5,np.nan,6])
print(np.isnan(arr))

"we cannot compare the np.nan directly"

# nan_to_num(arr,nan=value)  default - 0

print(np.nan_to_num(arr))
print(np.nan_to_num(arr,nan=100))

# np.isinf()    10^1000

arr = np.array([1,2,3,np.inf,5,np.inf,6])
print(arr)
print(np.isinf(arr))
print(np.nan_to_num(arr,posinf=1))