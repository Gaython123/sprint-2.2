
list_of_numbers = []
while True:

    user_list = int(input("choose option: "))
    match user_list:
        case 1:
            while True:
                number = input("Please enter numbers you need to sort")
                list_of_numbers.append(number)
                for i in list_of_numbers:
                    a = 0
                    b = user_list
                    if a > b:
                        a = b
                        list_of_numbers[a], list_of_numbers[b] = list_of_numbers[b], list_of_numbers[a]

                    match number:
                        case "end":
                            print(list_of_numbers)
        ##case 11:





