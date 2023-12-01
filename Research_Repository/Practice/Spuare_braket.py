# Getting user input
n = int(input("please enter the integer\n"))

# Count the number until n
counter = 0

# loop updating counter until n times and display results
while counter < n:
    print("[", counter + 1, "]")
    counter += 1

"""
# assertion test case 1
n = 3 
print(
[ 1 ]
[ 2 ]
[ 3 ])

# assertion test case 2
n = 5
print(
[ 1 ]
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
"""
