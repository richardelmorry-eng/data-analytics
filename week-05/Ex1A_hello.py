print('Hello, World!')
message = 'Hello world!'
print(message)
# It prints twice because I have two print statements, one for text and one for the variable.

# Displaying dollars and cents
dollars = 3
cents = .50
print(dollars + cents)
# I notice that the result is 3.5 instead of 3.50 because Python drops the extra zero and doesn't format it as money.
cents = cents + .25
print(dollars + cents)
d_str = '3 dollars'
c_str = '50 cents' 
print(d_str + " " + c_str) 