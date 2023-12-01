# Getting uer inputs
side_q = int(input("Please enter the length of the small rectangle\n\n"))
side_w = int(input("Please enter the width of the small rectangle\n\n"))
side_s = int(input("Please enter the length of the large rectangle\n\n"))
side_g = int(input("Please enter the width of the large rectangle\n\n"))

# Calculate rectangle and display the result
print("\nThe area of your shape is ", side_g * side_s - side_q * side_w, "\n\n")

# Testing
"""
print("My assertions are:"
"\nq = 2, w = 2, s = 7, g = 6 output = 38"
"\nq = 1, w = 1, s = 7, g = 10 output = 69")
"""
