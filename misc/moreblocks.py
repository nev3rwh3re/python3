
# uses indentation for new blocks
# when a line ends in a colon, python expects a code block to follow and it must be indented
# indent 4 spaces

# for year, month in generate_year_month(current_date):

"""
test
    test2
    test3
        test4
        test5



"""

# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
# print("*" * 80) # try tabbed in as well to get an idea of how a code block executes
#
# # if statements

name = input("please enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("you are old enough to vote")
#     print("please put an x in the box")
# else:
#     print("you are not old enough to vote. Come back in {0} years.".format(18-age))

if age < 18:
    print("you are not old enough to vote. Come back in {0} years.".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("you are old enough to vote")
    print("please put an x in the box")

