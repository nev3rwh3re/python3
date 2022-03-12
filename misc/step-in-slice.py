#         01234567890123
parrot = "Norwegian Blue"

print()

print(parrot[0:6:2]) # steps of 2
print(parrot[0:6:3]) # steps of 3

number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
print(number[1::4])

seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


