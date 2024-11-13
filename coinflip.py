import random
import time
import os
egyenleg = 100
jatek = input("Mit szeretnél játszan? (coinflip)\n")
ujra = "y"
while jatek == "coinflip" and ujra == "y":
    os.system('cls')
    coin = input("Mire szeretnél rakni?(f,i) ")
    print(f"Egyenleg: {egyenleg}\n")
    bet = int(input("\nMennyit szeretnél rakni? "))

    while bet > egyenleg:
        print("Nem tudsz ennyit rakni.")
        bet = int(input("Mennyit szeretnél rakni? "))
    
    egyenleg -= bet

    ctime = 0.01

    while time != 2:
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("f")
        time.sleep(ctime)
        ctime += ctime
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("i")
        time.sleep(ctime)
        ctime += ctime
    flip = random.randint(1,2)
    if flip == 1:
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("f")
        winner = "f"
    else:
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("i")
        winner = "i"

    if coin == "f" and winner == "f" or coin == "i" and winner == "i":
        os.system('cls')
        egyenleg += (bet*2)
        print(f"Egyenleg: {egyenleg}\n")
        print("Nyertél!")
    else:
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("Vesztettél!")
    time.sleep(1)

    ujra = input("\nSzeretnél még játszani?(y/n)\n")