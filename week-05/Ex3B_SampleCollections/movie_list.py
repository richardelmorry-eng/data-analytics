# Description: This script creates a list of my favorite movies
#              and sorts it in different ways
# Author: Richard Elmorry

movies = ["Rush Hour 1", "Rush Hour 2", "Rush Hour 3", "John Wick 4"]

# Describe and print the list
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

# Sorted with sorted(), then the original list again
print(sorted(movies))
print(movies)

# Sort the list itself with .sort(), then print it again
movies.sort()
print(movies)

# Add one more movie with .append(), then describe and print the list again
movies.append("John Wick 3")
print(f"The list movies now includes {len(movies)} of my top favorite movies")
print(movies)

# Observations:
# sorted() printed a sorted copy, but the original list stayed in its
# original order.
# .sort() changed the list itself, so printing it again shows the sorted order.
# .append() adds the new movie to the end of the list.