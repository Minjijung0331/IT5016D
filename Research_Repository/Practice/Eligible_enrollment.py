# Getting user inputs
distance_from_school = int(input("Please enter distance from school in km\n"))
student_age = int(input("Please enter age of student \n"))
has_residency = True
does_pay_international_fee = False

# Check enrollment eligibility
is_eligible = (
    distance_from_school < 4
    and 10 < student_age
    and student_age < 18
    and has_residency
    or does_pay_international_fee
)

# Display Result of eligible enrolment of the student
print("Student eligible enrolment is ", is_eligible)

# Testing
"""
print("Student eligible enrolment is"
"\n distance_from_school < 4 and and 10 > student_age and student_age < 18 and has_residency
    or does_pay_international_fee output: False"
"\n distance_from_school < 4 and and 10 < student_age and student_age < 18 and has_residency
    or does_pay_international_fee output: True)
"""
