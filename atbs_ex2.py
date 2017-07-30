def is_spam():
    spam = input("Please enter a number: ")
    if spam == "1":
        print("Hello")
    elif spam == "2":
        print("Howdy")
    else:
        print("Greetings!")

is_spam()


def for_loop():
    number = 0
    for number in range(0,100):
        number += 1
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

for_loop()

def while_loop():
    number = 0
    while number < 10:
        number += 1
        print(number)

while_loop()
