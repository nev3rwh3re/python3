answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess <  answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You are right!")
