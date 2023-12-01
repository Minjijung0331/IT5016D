from datetime import datetime, timedelta

# I need a program that requests a user to type in a date, and then displays one that is 125 days earlier than the date entered.

# Prompt a date to the user
date_input = input("Please enter any date in the format DD MM YYYY: \n")

# cast to a datetime object
date_object = datetime.strptime(date_input, "%d %m %Y")

# Show the result of year difference
print(
    "The date earlier 125 days than the date entered is ",
    date_object - timedelta(days=125),
)


# I need a program that prompts me for a date and then displays one that is 2 weeks later than the date entered.

# Prompt a date to the user
date_input = input("Please enter any date in the format DD MM YYYY: \n")

# cast to a datetime object
date_object = datetime.strptime(date_input, "%d %m %Y")

# Show the result of date 2 weeks later
print(
    "The date 2 weeks later than the date entered is ",
    date_object + timedelta(weeks=2),
)

# I need a program that takes 2 birthdays and returns the age difference.

# Prompt a date to the user
birthday1_input = input("Please enter first date of birth in the format DD MM YYYY: \n")
birthday2_input = input(
    "Please enter second date of birth in the format DD MM YYYY: \n"
)

# cast to a datetime object
birthday1_object = datetime.strptime(birthday1_input, "%d %m %Y")
birthday2_object = datetime.strptime(birthday2_input, "%d %m %Y")

# do a calculation
birthday1_age = datetime.today() - birthday1_object
birthday2_age = datetime.today() - birthday2_object

# Show the result of age difference
print(
    "The age difference of first and second birthday is",
    abs(birthday1_age.days / 365 - birthday2_age.days / 365),
)


# I need a program that displays a welcome message, then prompts the user to enter a date and an integer number representing number of years. The program should then display the date later than the date entered by the number of years provided.

# Confused what is the meaning about second int..

# Prompt welcome the user
print("Welcome :) \n")

# Prompt a date to the user
date_input = input("Please enter a date in the format DD MM YYYY: \n")

# cast to a datetime object
date_object = datetime.strptime(date_input, "%d %m %Y")

# Prompt a year to the user
years_input = input(
    "Please enter an integer number of years\n",
)

# I need a program that prompts me for 2 dates. The program should return the difference between the two dates in years.

# Prompt two dates to the user
date1_input = input("Please enter first date in the format DD MM YYYY: \n")
date2_input = input("Please enter second date in the format DD MM YYYY: \n")

# cast to a datetime object
date1_object = datetime.strptime(date1_input, "%d %m %Y")
date2_object = datetime.strptime(date2_input, "%d %m %Y")

# Show the result of year difference calculate
print(
    "The year difference of first and second dates is",
    abs(date1_object.year - date2_object.year),
)
