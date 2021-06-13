from random import randint

start = 1
end = 100
value = randint(start, end)
print("clue: ",bin(value))
print("")
print("I'm thinking of a number between", start, "and", end)
print("")

guess = None
count = 1
while guess != value:
    print("You are Trying for the %d time" % count)
    print("")

    count = count + 1
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
print("")

