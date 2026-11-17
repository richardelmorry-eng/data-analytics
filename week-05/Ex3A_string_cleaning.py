# Description: This script cleans up messy contact records
#              using string methods
# Author: Richard Elmorry

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert the names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert the names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove the $ from the salaries
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")
print(salary_1_clean)
print(salary_2_clean)
print(type(salary_1_clean))

# Chain .replace() and int() to get a usable integer from salary_1
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)
print(type(salary_1_int))

# Observations:
# .title() changed LaTonya to Latonya because it lowercases every letter
# except the first letter of each word.
# After removing the $, the salaries are still strings, so math won't work.
# They still have a comma, which int() can't handle, so the comma has to be
# removed too before converting to an integer.