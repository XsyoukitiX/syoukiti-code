#2026/9/6
print("Guess the integer [X] (0 < [X] < 101)")
import random
X = random.randint(1,100) #1~100
C = 0 #C=Count

while True: #execute roop / break - end / 1set(while True:)(break)
    G = input("Guess the number = ")
    C += 1 #input number is str
    if G.isdecimal():
        G = int(G) #G:str = int

        if G == X:
            print("That's correct!")
            print("Attempts:", C)
            break
        else:
            if G > X:
                print("guessed number > [X]")
                print("Try again")
            else:
                print("guessed number < [X]")
                print("Try again")
    else:
        print("-ERROR- This number isn't integer")            
            