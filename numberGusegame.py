import random

number = random.randint(1, 100)

attempts = 0  
print(number)

while True: 
    GuseNumber = int(input("Enter a number: "))

    attempts = attempts + 1
    
    if GuseNumber > number:
        print("Number is to high")
    elif GuseNumber < number:
        print("Number is to low")
    else:
        print(f"Conguration you gusse the number: {number} ")
        print(f" Attempts: {attempts}")
        break