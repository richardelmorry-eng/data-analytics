# Description: This script calculates gross pay, paying overtime
#              (hours over 40) at 1.5 times the regular rate
# Author: Richard Elmorry

pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"Pay rate: {pay_rate}, hours worked: {hours_worked}")
print(f"Gross pay: {gross_pay:.2f}")