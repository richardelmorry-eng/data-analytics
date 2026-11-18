# Description: This script uses a while loop to add weekly savings to a
#              bank balance until a savings goal is met
# Author: Richard Elmorry

balance = 100
savings_goal = 500
weekly_savings = 50
treat_cost = 10

while balance < savings_goal:
    balance = balance + weekly_savings
    print(f"This week my balance increased to ${balance:.2f}.")

    if balance >= savings_goal * 0.75:
        balance = balance - treat_cost
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}.")
    elif balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to ${balance:.2f}.")

print(f"Goal met! My current balance is ${balance:.2f}.")