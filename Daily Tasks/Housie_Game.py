import random


ln=random.randint(1,100)
print(ln)

chances=5

while chances>0:
    guess=int(input("Please enter any number:"))
    chances-=1

    if guess==ln:
        print("Congratulations,you guessed correct number")
        break
    elif guess<ln:
        print("Too low!")
    else:
        print("Too high!")
    

    




