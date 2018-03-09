import numpy as np

# ndarray creation with one dimension
a = np.array([1,2,3])
print('One dimension array: ',a)

# ndarray creation with two dimesnions
a = np.array([[1,2],[2,3]])
print('Two dimension array: ', a)

# ndarray creation with minimum dimensions
a = np.array([1,2,3,4,5,6], ndmin = 2)
print('Array with minimum dimensions: ', a)

# ndarray creation with dtype
a = np.array([1,2,3,4,5,6], dtype = complex)
print('Array with dtype specified: ', a)

# Intializing empty ndarray
a = np.empty((3,2), dtype=np.int)
print("Empty ndarray with shape :", a)

# Initializing zeros ndarray
a = np.zeros(5, dtype=np.int16)
print("Zeros ndarray with scalar shape: ", a)

a = np.zeros((2,3), dtype=np.float)
print("Zeros ndarray with shape: ", a)

# Initialize ones ndarray
a = np.ones((4,2), dtype=np.int32)
print("Ones ndarray with shape: ", a)

# Initialize ndarray from another list/tuple of python
x = [1,2,3]
a = np.asarray(x, dtype=np.float)
print("ndarray form list: ", a)

x = (4,5,6)
a = np.asarray(x, dtype=np.int16)
print("ndarray from tuple: ", a)

x = [(1,2),(4,5,6)]
a = np.asarray(x)
print("ndarray from list of tuples: ", a)

# Initialize ndarray from buffer (b represent bytestring)
s = b"Hello World"
a = np.frombuffer(s, dtype='S1')
print('ndarray from string buffer: ', a)

s = "Hello World"
a = np.array(list(s))
print('ndarray from string list: ', a)

# Initilaize ndarray from iterable object
x = range(5)
it = iter(x)
a = np.fromiter(it, dtype=np.float)
print("ndarray from iterable object: ", a)

# Initialize ndarray from arange(create evenly spaced values)
x = np.arange(start=5,stop=20,step=2,dtype=np.float)
print("ndarray from arange: ", x)

# Initialize ndarray from linspace(the number of evenly spaced values between the interval is specified)
x = np.linspace(start=10, stop=20, num=5, endpoint=True, dtype=np.float)
print("ndarray from linspace: ", x)

# Initialize ndarray from logspace(numbers that are evenly spaced on a log scale)
x = np.logspace(start=1.0,stop=2.0,num=20,dtype=np.float)
print("ndarray from logspace with base 10: ", x)

x = np.logspace(start=1.0,stop=2.0,num=20,base=2,dtype=np.float)
print("ndarray from logspace with base 2: ", x)





