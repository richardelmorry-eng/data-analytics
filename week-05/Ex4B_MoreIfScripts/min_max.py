# Description: This script displays the smallest and then the largest
#              of three numbers
# Author: Richard Elmorry

a = -3
b = 0
c = -10

if a <= b and a <= c:
    smallest = a
elif b <= c:
    smallest = b
else:
    smallest = c

if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")