# Write a program that displays a welcome message, then displays the result of adding 2 integers. The integers must be defined in the add_numbers( ) function.

# Display welcome message
print("Welcome to simple function")


# Define add_number function
def add_number():
    print(3 + 7)


# Invoking the function
add_number()


# Write a program that stores an integer value x and a string of value y (you can choose these values). The program must use a method that displays the y text, x number of times.


# Define display_times function
def display_times():
    x = 2
    y = "Hi"
    for i in range(x):
        print(y)


# Invoking the function
display_times()
