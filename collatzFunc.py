def collatz(number): 
    if number % 2 == 0:    
        return number // 2
    elif number % 2 == 1:
        return number * 3 + 1


def collatz_call():
    number = int(input('Enter a Number: '))

    while number != 1:
        print(number)
        number = collatz(number)
        if number == 1:
            print(number)
            break

while True:
    try:
        collatz_call()
        break
    except ValueError:
        print('Error: You must enter an integer.')
    
