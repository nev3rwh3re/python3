#         01234567890123
parrot = "Norwegian Blue"

print()
#653

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1] # doesn't include a - because up to but not including....
print(backwards)

backwards2 = letters[25::-1]
print(backwards2)

backwards3 = letters[::-1] # this is a common way to reverse a string. this is a reversing idiom                                                             //
print(backwards3)

#challenge
# create a slice that produces the characters qpo, edcba and the last 8 characters in reverse order

one = letters[16:13:-1]
print(one) # qpo
two = letters[4::-1]
print(two)
three = letters[25:17:-1]
print(three)

three = letters[:-9:-1]
print(three)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])

