# Define known values
bill = float(input("What is the amount of the bill? "))
tip_percent = float(input("How much do you want to tip? "))

# Calculate the unknown
tip_amount = bill * tip_percent

# Display the results
print("The tip on a $" + format(bill, ".2f") + " restaurant bill is $" + format(tip_amount, ".2f"))

# Pitfalls of input():
# 1. input() always returns text, so it must be converted with float() before doing math.
# 2. The user can type the wrong kind of number: 20 instead of 0.20 gives a tip of $1710.00 with no error.
# 3. Typing something that is not a plain number, like $85.50, crashes with a ValueError.