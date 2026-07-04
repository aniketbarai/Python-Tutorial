# ============================================
# NumPy - Part 1
# ============================================

# NumPy (Numerical Python)
# -> Used for numerical computing
# -> Works with multi-dimensional arrays
# -> Faster than Python lists
# -> Widely used in Data Science, AI and ML

import numpy as np


# ==========================================================
# 1. Creating Arrays
# ==========================================================

# ---------- 1D Array ----------
# Definition:
# A one-dimensional array is similar to a Python list.

arr_1d = np.array([10, 20, 30, 40, 50])

print(arr_1d)

# Output:
# [10 20 30 40 50]


# ---------- 2D Array ----------
# Definition:
# A two-dimensional array consists of rows and columns.

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr_2d)

# Output:
# [[1 2 3]
#  [4 5 6]]


# ==========================================================
# 2. shape
# ==========================================================

# Definition:
# shape returns the dimensions of an array.
# It tells how many rows and columns are present.

print(arr_2d.shape)

# Output:
# (2, 3)

# Meaning
# 2 -> Rows
# 3 -> Columns

# Remember
# Shape = (Rows, Columns)


# ==========================================================
# 3. size
# ==========================================================

# Definition:
# size returns the total number of elements in an array.

print(arr_2d.size)

# Output:
# 6

# Calculation
# 2 Rows × 3 Columns = 6 Elements


# ==========================================================
# 4. ndim
# ==========================================================

# Definition:
# ndim returns the number of dimensions of the array.

print(arr_2d.ndim)

# Output:
# 2

# Examples
# [1,2,3]           -> 1 Dimension
# [[1,2],[3,4]]     -> 2 Dimensions
# [[[1],[2]]]       -> 3 Dimensions


# ==========================================================
# 5. dtype
# ==========================================================

# Definition:
# dtype returns the datatype of elements stored in the array.

print(arr_2d.dtype)

# Output (depends on system)
# int32 or int64

# Common Datatypes
# int32
# int64
# float32
# float64
# bool
# str


# ==========================================================
# 6. astype()
# ==========================================================

# Definition:
# Used to convert one datatype into another.

arr = np.array([1.2, 3.8, 5.9, 9.4])

print(arr)

# Convert float into integer

int_arr = arr.astype(int)

print(int_arr)

# Output
# [1 3 5 9]

# Note:
# Decimal part is removed.
# It DOES NOT round the value.


# ==========================================================
# 7. Arithmetic Operations
# ==========================================================

# NumPy performs operations on every element.

print(int_arr + 5)

# Output
# [ 6  8 10 14]


print(int_arr - 2)

# Output
# [-1 1 3 7]


print(int_arr * 2)

# Output
# [ 2  6 10 18]


print(int_arr / 2)

# Output
# [0.5 1.5 2.5 4.5]


print(int_arr ** 2)

# Output
# [ 1  9 25 81]


# ==========================================================
# 8. Aggregation Functions
# ==========================================================

# Aggregation means converting multiple values
# into one single value.


# ---------- Sum ----------
# Returns total of all elements.

print(np.sum(int_arr))

# Example
# 1 + 3 + 5 + 9 = 18


# ---------- Mean ----------
# Returns average value.

print(np.mean(int_arr))

# Formula
# Mean = Sum / Number of Elements


# ---------- Minimum ----------
# Returns smallest element.

print(np.min(int_arr))

# ---------- Maximum ----------
# Returns largest element.

print(np.max(int_arr))

# ---------- Standard Deviation ----------
# Measures how spread the data is.

print(np.std(int_arr))

# Small STD
# 10 11 12 13

# Large STD
# 10 50 90 150

# ---------- Variance ----------
# Variance = (Standard Deviation)^2

print(np.var(int_arr))

# np.array()     -> Create NumPy Array
# shape          -> Rows & Columns
# size           -> Total Elements
# ndim           -> Number of Dimensions
# dtype          -> Datatype
# astype()       -> Change Datatype

# np.sum()       -> Sum
# np.mean()      -> Average
# np.min()       -> Minimum
# np.max()       -> Maximum
# np.std()       -> Standard Deviation
# np.var()       -> Variance

import numpy as np

# ==========================================================
# --> Indexing & Slicing <--
# ==========================================================

# Definition:
# Indexing is used to access a single element from an array.
#
# Slicing is used to access multiple elements from an array.
#
# Index starts from 0.
#
# Positive Index:
# 0  1  2  3  4
#
# Negative Index:
# -5 -4 -3 -2 -1


# ==========================================================
# 1. Indexing in 1D Array
# ==========================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr)

# Access first element
print(arr[0])      # 10

# Access third element
print(arr[2])      # 30

# Access last element
print(arr[-1])     # 50

# Access second last element
print(arr[-2])     # 40


# ==========================================================
# 2. Slicing in 1D Array
# ==========================================================

# Syntax:
# array[start : end : step]

# Note:
# Start -> Included
# End   -> Excluded
# Step  -> Number of jumps

print(arr[1:4])

# Output
# [20 30 40]


print(arr[:3])

# Output
# [10 20 30]


print(arr[2:])

# Output
# [30 40 50]


print(arr[:])

# Output
# Entire Array
# [10 20 30 40 50]


print(arr[::2])

# Output
# [10 30 50]


print(arr[::-1])

# Output
# Reverse Array
# [50 40 30 20 10]


# ==========================================================
# 3. Indexing in 2D Array
# ==========================================================

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr_2d)

# Row Index, Column Index

print(arr_2d[0, 0])

# Output
# 10

print(arr_2d[1, 2])

# Output
# 60

print(arr_2d[2, 1])

# Output
# 80

print(arr_2d[-1, -1])

# Output
# 90


# ==========================================================
# Understanding Row & Column Index
# ==========================================================

#        Col
#        0   1   2
#
# Row 0 [10 20 30]
# Row 1 [40 50 60]
# Row 2 [70 80 90]
#
# Example:
#
# arr_2d[1,2]
#
# Row 1 -> [40 50 60]
# Column 2 -> 60


# ==========================================================
# 4. Slicing in 2D Array
# ==========================================================

# Syntax
# array[row_start:row_end, col_start:col_end]

# First two rows

print(arr_2d[0:2])

# Output
# [[10 20 30]
#  [40 50 60]]


# First row

print(arr_2d[0])

# Output
# [10 20 30]


# Second column

print(arr_2d[:, 1])

# Output
# [20 50 80]


# First column

print(arr_2d[:, 0])

# Output
# [10 40 70]


# First two columns

print(arr_2d[:, 0:2])

# Output
# [[10 20]
#  [40 50]
#  [70 80]]


# Last column

print(arr_2d[:, -1])

# Output
# [30 60 90]


# Last row

print(arr_2d[-1])

# Output
# [70 80 90]

# Last two rows

print(arr_2d[1:])

# Output
# [[40 50 60]
#  [70 80 90]]


# ==========================================================
# 5. Modify Elements
# ==========================================================

# We can also update array values using indexing.

arr = np.array([10, 20, 30, 40])

arr[2] = 100

print(arr)

# Output
# [10 20 100 40]


arr_2d[1, 1] = 500

print(arr_2d)

# Output
# [[ 10  20  30]
#  [ 40 500  60]
#  [ 70  80  90]]


# ==========================================================
# Quick Revision
# ==========================================================

# array[index]
# -> Access one element

# array[start:end]
# -> Slice elements

# array[start:end:step]
# -> Slice with step

# array[::-1]
# -> Reverse array

# array[row, column]
# -> Access 2D element

# array[:, column]
# -> Entire column

# array[row, :]
# -> Entire row

# array[row_start:row_end, col_start:col_end]
# -> Slice 2D array

# ==========================================================
# Questions
# ==========================================================

# Difference between Indexing and Slicing?
#
# Indexing:
# -> Returns a single element.
#
# Slicing:
# -> Returns multiple elements (sub-array).


# Why does slicing exclude the ending index?
#
# Because Python follows the rule:
# Start is Included
# End is Excluded


# How do you access the last element?
#
# array[-1]


# How do you reverse a NumPy array?
#
# array[::-1]


# How do you access the second column of a 2D array?
#
# array[:, 1]


# Reshaping & Manipulating Arrays

# reshape(rows,cols) -- specify new shapes
# if dimensions match

arr = np.array([1,2,3,4,5,6])
reshape_arr = arr.reshape(2,3)
print(reshape_arr)