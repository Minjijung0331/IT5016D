def divide_numbers(number_1, number_2):
    if number_2 == 0:
        return "Cannot divide by zero."
    return number_1 / number_2


print(divide_numbers(3, 0))


def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"


print(divide_numbers(3, 0))
