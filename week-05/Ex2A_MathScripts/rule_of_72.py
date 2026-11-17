# Rule of 72: years to double = 72 / interest rate (as a percent)
savings = 5000
interest_rate = 0.07
years = 72 / (interest_rate * 100)
doubled = savings * 2

print("Your current savings is " + format(savings, ".2f") + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be")
print("worth " + format(doubled, ".2f") + " in " + format(years, ".1f") + " years")