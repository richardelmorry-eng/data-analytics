# Description: This script prints a greeting based on the current hour
# Author: Richard Elmorry

hour = 12

if hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")

if hour >= 23 or hour <= 4:
    print("What are you doing up so late??")