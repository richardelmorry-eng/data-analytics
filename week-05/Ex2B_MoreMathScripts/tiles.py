# Calculate how many boxes of tiles to buy
import math

length = 13
width = 11
tiles_per_box = 12

area = length * width
boxes_needed = math.ceil(area / tiles_per_box)
total_boxes = math.ceil(area * 1.10 / tiles_per_box)

print("The room is " + str(length) + " by " + str(width) + " feet, which is " + str(area) + " square feet.")
print("Boxes needed: " + str(boxes_needed))
print("Boxes to buy with 10% extra: " + str(total_boxes))