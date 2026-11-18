# Description: This script calculates weekly gross pay, estimates annual
#              gross pay, and finds the federal tax withheld by filing status
# Author: Richard Elmorry

pay_rate = 40
hours_worked = 40
filing_status = "single"

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

annual_gross = gross_pay * 52

if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
else:
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withheld:.2f}")
print(f"Your net pay is ${net_pay:.2f}")