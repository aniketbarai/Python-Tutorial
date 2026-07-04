prices = [100,200,300,400]
discount = 10 #10%

final_prices = []

for price in prices:
    final_price = price - ((price * discount)/100)
    final_prices.append(final_price)

print(final_prices)

# the above code is fine but it is very slow as we are using loops so we dont prefer this method so instead of this we use broadcasting.

"""
Broadcasting : Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array.

Rules:
1.Matching dimensions:

arr1[1,2,3]
+
arr2[4,5,6]
=
[5,7,9]

2.Expanding Single Elem
arr1[2,3,4] + 10
=
[12,13,14]

3.Icompatible shapes
eg:
[1,2,3] + [1,2]
shape is not matching...it is error

"""
import numpy as np

prices2 = np.array([100,200,300,400])
discount = 10 #10% | scalar

final_prices2 = prices2 -((prices2*discount)/100)
print(final_prices2) 


"""
Vectorization:

Vectorization means applying operations to entire arrays at once instead of iterating element-by-element.
"""

arr = np.array([10,20,30])
multiply_arr = arr*3
print(multiply_arr)