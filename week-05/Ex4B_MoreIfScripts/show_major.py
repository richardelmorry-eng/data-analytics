# Description: This script looks up a student's major name and
#              department office from a major code
# Author: Richard Elmorry

student_name = "Richard"
student_major = "XYZ"

if student_major == "BIOL":
    major_name = "Biology"
    office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    office = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"
    office = ""

print(f"Student: {student_name}")
print(f"Major: {major_name}")
if office != "":
    print(f"Department office: {office}")