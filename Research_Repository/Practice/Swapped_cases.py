# Getting user input
print("Please enter your class size")
student_1 = input("Please enter student 1 name:\n")
student_2 = input("Please enter student 2 name:\n")
student_3 = input("Please enter student 3 name:\n")

# reverse cases and display result
print(
    "Thank you, the names of your students in swapped case are: ",
    student_1.swapcase(),
    student_2.swapcase(),
    student_3.swapcase(),
)

# testing
"""
student_1 = "Beyonce"
student_2 = "Michelle"
student_3 = "Kelly"
print(
    "Thank you, the names of your students in swapped case are: bEYONCE mICHELLE kELLY "
)
"""
