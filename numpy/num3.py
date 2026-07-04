"""
>>> Insert in 1D Arr

np.insert(arr,idx,val)
arr - original arr
idx - position
val - new data

>>> Insert in 2D Arr

np.insert(arr,idx,val,axis=None)
arr - original arr
idx - position
val - new data
axis - 0 = row-wise insertion/ vertical stacking
    1 = column-wise instertion/ horizontal stacking

"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
# new_arr = np.insert(arr,1,15)
# print(new_arr)

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
# insert a new row at idx 1
new_arr_2d = np.insert(arr_2d,1,[5,6],axis=1)
print(new_arr_2d)

"""
append

"""

new_arr = np.append(arr,[70,80,90])
print(new_arr)

"""
concatination

np.concatenate((arr1,arr2), axis=0)
"""
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_conc_arr = np.concatenate((arr1,arr2))
print(new_conc_arr)
