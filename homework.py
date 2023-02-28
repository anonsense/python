import random

n = 3
print("Gamer #1")
car = input("Write the car brand: ")
number = input("Write your number: ")
print("Gamer #2")
car1 = input("Write the car brand: ")
number1 = input("Write your number: ")
print("Gamer #3")
car2 = input("Write the car brand: ")
number2 = input("Write your number: ")
numbs = range(50, 59)
time = random.choice(numbs)
time1 = random.choice(numbs)
#result = {"Car brand": car, "Your number": number,"Time": 0 }

result = {
    "Gamer #1": {
        "The car brand": car,
        "The number": number,
        "Time": 0
    },
    "Gamer #2": {
        "The car brand": car1,
        "The number": number1,
        "Time": random.randint(50, 59)
    },
    "Gamer #3": {
        "The car brand": car2,
        "The number": number2,
        "Time": random.randint(50, 59)
    }

}

if car2 == car or car2 == car1 or car == car1:
    print("Cannot be registered with the same car model")
else:
    print()
result.pop("Gamer #1")
print(result)

if time < time1:
    print("The winner is Gamer# 2")
else:
    print("The winner is Gamer #3")
