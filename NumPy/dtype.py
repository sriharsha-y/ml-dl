import numpy as np

# using array-scalar type
dt = np.dtype(np.int16)
print('Scalar data type int16: ',dt)

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc
dt = np.dtype('i4')
print('Scalar data type int32: ', dt)

# using little endian or big endian notation > is big endian, < is little endian
dt = np.dtype('>i8')
print('Scalar data type big endian: ',dt)

# Structured data type. here field name and corrosponding scalar data type is to be declared
dt = np.dtype([('age', np.int8)])
print("Structured data type: ", dt)

# Applying our Data Type to ndarray object
a = np.array([(10,),(20,),(30,)], dtype = dt)
print("Custom dtype applied array: ", a)

# File name can be used to access content of age column 
print("Accessing age column: ", a['age'])

# Another example with multiple fields in data type
student = np.dtype([('name', 'S20'),('age', 'i1'), ('marks', 'f4')])
a = np.array([('abcd', 10, 50),('xyzx', 20, 60)], dtype=student)
print(a)




# Each built-in data type has a character code that uniquely identifies it.
# 'b' − boolean
# 'i' − (signed) integer
# 'u' − unsigned integer
# 'f' − floating-point
# 'c' − complex-floating point
# 'm' − timedelta
# 'M' − datetime
# 'O' − (Python) objects
# 'S', 'a' − (byte-)string
# 'U' − Unicode
# 'V' − raw data (void)

