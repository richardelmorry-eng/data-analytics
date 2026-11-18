# Description: This script converts a department code
#              into a department name using match/case
# Author: Richard Elmorry

dept_code = 7

match dept_code:
    case 1:
        dept_name = "Marketing"
    case 5:
        dept_name = "Human Resources"
    case 10:
        dept_name = "Accounting"
    case 12:
        dept_name = "Legal"
    case 18:
        dept_name = "IT"
    case 20:
        dept_name = "Customer Relations"
    case _:
        dept_name = "Unknown department"

print(f"Department code {dept_code} is {dept_name}")