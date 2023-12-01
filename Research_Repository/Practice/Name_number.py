name = input("Please enter your name\n")
number = input("Please enter your phone number\n")


def name_number(name, number):
    print(
        "Hello there, my name is, {0}, and my number is, {1}".format(
            name, number.rstrip()
        )
    )


name_number(name, number)
