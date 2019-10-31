import random

number = []
attempts = 0

def makenumber():
    for i in range(4):
        x = random.randrange(0, 10)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        makenumber()

def Game():
    global attempts
    attempts += 1
    cows = 0
    knights = 0
    choice = input("Please enter a 4 digit number: ")
    guess = []
    for i in range (4):
        guess.append(int(choice[i]))
    for i in range (4):
        for j in range (4):
            if(guess[i] == number[j]):
                cows += 1
    for x in range (4):
        if(guess[x] == number[x]):
            knights += 1
    print("Knights: ", knights)
    print("Cows: ", cows)
    if(knights == 4):
        print("You won after ", attempts, " attempts!")
    if(knights != 4):
        Game()

makenumber()
Game()

