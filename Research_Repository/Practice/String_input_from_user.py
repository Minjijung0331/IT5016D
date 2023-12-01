# Input statement returns a string from the user
print("Welcome to your first data entry program\n")
user_first_name = input("Please enter your first name... \n")
user_last_name = input("Please enter your las name...\n")
user_yob = int(input("Please enter your year of birth...\n"))

print("Thank you for your input\n")
print("The name that you entered is ", user_first_name + user_last_name)
print("Your age in years is ", 2023 - user_yob)


# # Sleep calculator
print("Welcome to Sleep Calculator\n")
user_yob = int(input("Please enter your year of birth\n"))
user_sleep_hours = int(input("Please enter your total sleep hours for a week \n"))

print("\n\nThank you for your input\n")
print("The year of birth that you entered is ", user_yob)
print("Your age in years is ", 2023 - user_yob)
print("Your average sleep hours is", user_sleep_hours / 7)
