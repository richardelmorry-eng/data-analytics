# Description: This script prints a summary line for each salesperson
#              and flags top performers (sales over $5,000)
# Author: Richard Elmorry

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

for name, region, total in sales_data:
    print(f"{name} ({region}): ${total:,.2f}")
    if total > 5000:
        print(" ^ Top performer!")