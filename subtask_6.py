
list_of_numbers = []
while True:

    user_list = int(input("choose option: "))
    match user_list:
        case 1:
            while True:
                number = int(input("Please enter a number or 'end' to sort the numbers: "))

                if number == 12:
                    if len(list_of_numbers) == 0:
                        print("The list is empty")

                    else:
                        print(f"\nUnsorted list is {list_of_numbers}")
                        for i in range(len(list_of_numbers)):
                            for j in range(len(list_of_numbers)):
                                if list_of_numbers[i] > list_of_numbers[j]:
                                    list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                        print(f"Sorted list is {list_of_numbers}\n")

                elif number == int(number):
                    list_of_numbers.append(number)
                    
                else:
                    print("Invalid input")



        ##case 11:


