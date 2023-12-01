string_1 = "here is a translation: Haera mai ki konei means come here!"

print("The number of times that i appears is {0}\n".format(string_1.count("i")))

konei_endindex = string_1.find("konei") + len("konei")
print("The end index position of konei is {0}\n".format(konei_endindex))

here_position = string_1.find("here", konei_endindex, len(string_1))
print(
    "Looking for the string_1 here, anytime after konei...\n\n"
    "The string_1 here appears at index position..{0}".format(here_position)
)
