
list_of_numbers = []
while True:

    user_list = int(input("choose option: "))
    match user_list:
        case 1:
            while True:
                number = int(input("Please enter a number or 'end' to sort the numbers: "))
                if number == 00:
                    print(list_of_numbers)

                elif number == int(number):
                    list_of_numbers.append(number)
                    for i in list_of_numbers:
                        a = 0
                        b = user_list
                        if a > b:
                            a = b
                            list_of_numbers[a], list_of_numbers[b] = list_of_numbers[b], list_of_numbers[a]

                else:
                    print("Invalid input")


        ##case 11:





