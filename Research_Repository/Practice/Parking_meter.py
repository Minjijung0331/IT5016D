print("Kia Ora, this is a parking meter")
# Getting park time from user input
park_time = int(input("Please enter the hour you would like to park for\n"))
# Display to confirm user input
print("park time entered is ", park_time, " hours.")


rate = 4
cost = 0
if park_time > 3:
    cost = rate * 3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)

# test case assertion 1
"""
park_time = 4
total cost of parking = $14
"""

# test case assertion 2
"""
park_time = 2
total cost of parking = $8
"""

# test case assertion 3
"""
park_time = 10
total cost of parking = $26
"""
