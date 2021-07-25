from random import randint

start = 1
end = 100
guess = None
count = 1
points = 100
value = randint(start, end)
print("")
print("I'm thinking of a number between", start, "and", end)
print("")
print("if you need clue,Press 1")
clue = int(input())
if clue == 1:
    print("To Continue with clue by giving 10 of your points press 1 again else print 0")
    y = int(input())
    if y == 1:
        print("clue: ",bin(value))
        points = points - 10
    else:
        print("Continue guessing without clue")
else:
    print("Continue guessing without clue")
while guess != value:
    print("You are Trying for the %d time" % count)
    print("")

    count = count + 1
    points = points - 1
    text = int(input("Guess the number: "))
    print("")

    guess = (text)

    if guess < value:
        print("Try Higher Number.")
        print("")

    elif guess > value:
        print("Try Lower Number.")
        print("")
print("Congratulations! You guessed the right answer %d in %d trys" % (value,count - 1))
print("Your points",points)
if points < 93:
    print("!!!could be better!!! - Thank you")
elif points >= 93:
    print("Good guess- Thank you")

