# Description: This script builds a set of fruity candy combinations
#              from two tuples
# Author: Richard Elmorry

candy_types = ("gummies", "lollipops", "taffy")
fruit_flavors = ("strawberry", "watermelon", "green apple")

# Combine one candy and one flavor using the index of each tuple
candy_options = set()
candy_options.add(fruit_flavors[1] + " " + candy_types[0])
candy_options.add(fruit_flavors[2] + " " + candy_types[1])
candy_options.add(fruit_flavors[0] + " " + candy_types[2])

print("Today's candy options include:")
print(candy_options)

# Observations:
# The items come out in a different order each time I run the script,
# because a set is unordered and has no fixed order.