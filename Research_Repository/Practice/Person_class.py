# Define class
class Person:
    # Define function
    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address  # Add address attribute
        self.height = height  # Add height attribute

    # Define function
    def myIntro(self):
        print("Hello my gender is " + self.gender)
        print(
            "Hello my age is", self.age
        )  # , is used when we need to show int or float values.
        # Add display element for address and height
        print("Hello my address is " + self.address)
        print("Hello my height is " + self.height)


# Add address and height as parameter
harry = Person(36, "male", "1 Nelson street, Auckland Central", "190cm")
sarrah = Person(34, "female", "1 Nelson street, Auckland Central", "190cm")

# Invoking the function
harry.myIntro()
sarrah.myIntro()
