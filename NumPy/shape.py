import numpy as np

# Determine shape of array (rows,columns)
a = np.array([[1,2,3],[4,5,6]])
print("Shape 2 dimesnional: ", a.shape)

# Reshape an array
b = a.reshape(3,2)
print("Reshape 2 dimesnional: ", b)

# Evenly spaced values within given interval
a = np.arange(24)
print("Evenly Spaced values: ", a)

# Reshaping to multi dimensional array
b = a.reshape(2,4,3)
print("Reshape multi dimensional: ", b)

# Itemsize of element in an array
a = np.array([1,2,3,4], dtype=np.int8)
print("Item size in bytes for int8: ", a.itemsize)

a = np.array([1,2,3,4], dtype=np.int64)
print("Item size in bytes for int64: ", a.itemsize)

