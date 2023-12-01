# Primitive types are the basic types of data that always has a value,
# including int, float, boolean, char

# Boolean
a = True
b = False

print(type(a), type(b))

# Strings
c = "Python"
d = "Language"

print(type(c), type(d))

# List
e = ["Jhon", "bob", "sarah"]

print(
    type(e),
)

# Tuple
f = ("Jhon", "Bob", "sarah")

print(type(f))

# Dictionary
g = {"std1": "Jhon", "std2": "bob", "std3": "sarah"}

print(type(g))

# Reference Types refers to a primitive type of data and by doing so, will not take up memory space as it has no value,
# including string, dictionary, list and tuple

x = 15
y = x
print(y)

# Reference type values can be null or none but Primitives always have a value
# so assign empty string as cannot crate empty int or null value

s = ""  # empty string

print(type(s))

# Using variables by reference or by value will result in different outputs

x = 5
y = x

print("x=", x, "y=", y)

x = 10

print("x=", x, "y=", y)
