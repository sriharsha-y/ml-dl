import numpy as np

# index always starts from 0

# ndarray slicing using slice object
a = np.arange(10)
sl = slice(2,7,2)
print("ndarray sliced with slice object: ", a[sl])

# ndarray sliced without slice object
a = np.arange(20)
print("ndarray sliced with out slice object: ", a[2:7:2])

# ndarray slicing with only lower bound
a = np.arange(10)
print("ndarray sliced with only lower bound: ", a[2:])

# ndarray slicing with only upper bound
a = np.arange(10)
print("ndarray sliced with only upper bound: ", a[:5])

# ndarray slicing with only lower and upper bound
a = np.arange(10)
print("ndarray sliced with lower & upper bound: ", a[2:7])

# ndarray multi dimensional slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("ndarray multidimensional slicing: ", a[1:])

# ndarray multi dimensional get columns 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("ndarray multidimensional column: ", a[...,1])

# ndarray multi dimensional get rows 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("ndarray multidimensional row: ", a[1,...])

# ndarray multi dimensional slice and get columns 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("ndarray multidimensional slice & get columns: ", a[...,1:])