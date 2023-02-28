# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
general = int(input("Please write the daily rate of calories consumed: "))
breakfast = int(input("Please write the number of calories eaten for breakfast: "))
lunch = int(input("Please write the number of calories eaten for lunch: "))
supper = int(input("Please write the number of calories eaten for supper: "))

last = general - (breakfast + lunch + supper)
print("Calories left: ", last)

if 50 < last < 90:
    print("You can eat the banana")

elif 200 > last > 90:
    print("You can eat nuts and become a squirrel")
elif last < 50:
    print("Piggy go sleep")
else:
    print("You can eat raisin")
