# Calculate the distance between two points
import math

x1 = 1
y1 = 2
x2 = 4
y2 = 6

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance between (" + str(x1) + ", " + str(y1) + ") and (" + str(x2) + ", " + str(y2) + ") is " + format(distance, ".2f"))