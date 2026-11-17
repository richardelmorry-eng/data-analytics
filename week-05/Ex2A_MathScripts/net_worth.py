# Define known values
savings = 5000
car_value = 12000
student_loan = 8000
credit_card = 1500

# Calculate the unknowns
total_assets = savings + car_value
total_debts = student_loan + credit_card
net_worth = total_assets - total_debts

# Display the results
print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))