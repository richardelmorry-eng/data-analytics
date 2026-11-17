# Description: This script tests various numeric
#              conversion techniques
# Author: Richard Elmorry

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a) Cast as integer using int()
# a_int = int(a)  # ValueError

# b) Cast as integer using int()
b_int = int(b)

# c) Cast as integer using int()
# c_int = int(c)  # ValueError

# d) Cast as integer using int()
# d_int = int(d)  # ValueError

# b) Cast as float using float()
a_float = float(a)

# float() on b
b_float = float(b)

# float() on c
# c_float = float(c)  # ValueError

# float() on d
# d_float = float(d)  # ValueError

# c) int(float(a))
a_int_float = int(float(a))

# d) Slicing out the numeric part of c and d
c_slice = c[0:3]
c_slice_int = int(c_slice)
d_slice = d[7:8]
d_slice_int = int(d_slice)

# e) Using .strip() inside print
print(a.strip())
print(d.strip())

# Print each variable and its type
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(b_int, type(b_int))
print(a_float, type(a_float))
print(b_float, type(b_float))
print(a_int_float, type(a_int_float))
print(c_slice, type(c_slice))
print(c_slice_int, type(c_slice_int))
print(d_slice, type(d_slice))
print(d_slice_int, type(d_slice_int))

# Observations:
# int() only works on a string that is a whole number, like b. It fails on a
# because of the decimal point and spaces, and on c and d because of the letters.
# float() accepts decimals and ignores spaces, so a and b work, but c and d
# still fail with a ValueError.
# int(float(a)) turns the string into a float first and then into an int,
# which drops the .1 and gives 101.
# Slicing pulls out just the digits from c and d so int() can convert them.
# .strip() removes the spaces from the start and end of a and d.