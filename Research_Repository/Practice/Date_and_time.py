from datetime import datetime, timedelta

# Getting user input
date_input = input("Please enter you DOB in the format DD Mmm YYYY: \n")

# Cast to a datetime object
date_object = datetime.strptime(date_input, "%d %m %Y")

# Output some confirmation
print("The year entered is ", date_object.year, "\n")

# Do a calculation
my_age = datetime.today() - date_object

# Display the result in different formats
print("My exact age is ", my_age, "\n")
print("My exact age just in days is ", my_age.days, "days\n")
print("My exact age just in years is ", int(my_age.days / 365), "years\n")

# Add 10 days to my current age
print("In 10 days time my age will be ", datetime.today() + timedelta(days=10), ".\n")

# Add my current age to today's date
print("I will be double my age in ", datetime.today() + my_age, ".")
