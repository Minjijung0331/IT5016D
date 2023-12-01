import random

# False
bool1 = 1 > 2
print(bool)

# True
bool2 = 1 < 2
print(bool2)

# true
bool3 = 1 == 1
print(bool3)

# Random module to calculate random numbers
male = False
male = bool(random.randint(0, 1))

# Display conditionally
if male:
    print("We will use name Rangi")
else:
    print("We will use name Anihera")

# Bool test
print("Test 1 ", bool(True))
print("Test 2 ", bool(False))
print("Test 3 ", bool("text"))
print("Test 4 ", bool(""))
print("Test 5 ", bool(" "))
print("Test 6 ", bool(0))
print("Test 7 ", bool())
print("Test 8 ", bool(3))
print("Test 9 ", bool(None))
