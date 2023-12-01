entry_is_valid = False
number_of_goes = 0
while not entry_is_valid:
    try:
        number_entered = int(input("Enter a valid positive integer\n"))
        if number_entered <= 0:
            raise ValueError("Entered value is not a positive integer.")
    except ValueError as e:
        print("The entry is not valid:\n{0}\n" "Please try again...".format(e))
    else:
        entry_is_valid = True
        print(
            "Thank you. The acceptable number entered "
            "was {0}.".format(number_entered)
        )
    finally:
        number_of_goes += 1
        print("The number of goes used is...{0}".format(number_of_goes))
