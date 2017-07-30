def commaCode():
    my_list = []
    userInput = input('Enter something: ')
    my_list.append(userInput)
    for item in my_list[:-1]:
        print(item + ',  ', end=' ')
    # print specifically the last
        print('and ' + my_list[-1])

commaCode()
