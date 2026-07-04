# Removing elem from arr
"""
np.delete(arr,idx,axis=None)
    Eg: new_arr = np.delete(arr,0)

    >>> 2D Array elem delete

    arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    new_2d_arr = np.delete(arr_2d,1,axis=0)
    
    Op:
    [[1 2 3]
    [7 8 9]]

"""
import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.delete(arr,0)
print(new_arr)

arr_2d = np.array([
    [1,2,3],[4,5,6],[7,8,9]
])
print(arr_2d)
new_2d_arr = np.delete(arr_2d,1,axis=0)
print(new_2d_arr)

# Stacking 

"""
vstack() --> row-wise (vertically stack)
hstack() --> column-wise (horizontally stack)
"""
# Splitting the arr

"""
np.split() --> equally split
np.hsplit() --> horizontally split
np.vsplit() --> vertically split
"""

print(np.split(arr,3))
