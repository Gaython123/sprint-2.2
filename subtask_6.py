
list_of_numbers = []
while True:

    user_list = input("choose option: ")

    match user_list:
        case "1":

            while True:
                number = input("Please enter a number or 'end' to sort the numbers: ")

                if number == "end":
                    if len(list_of_numbers) == 0:
                        print("The list is empty")

                    else:
                        sort_choice = input("Enter '1' or '2' to sort from: \n1. 'min' to 'max' (increasing)\n2. 'max' to 'min' (decreasing)")
                        match sort_choice:
                            case "1":
                                print(f"\nUnsorted list is {list_of_numbers}")
                                for i in range(len(list_of_numbers)):
                                    for j in range(len(list_of_numbers)):
                                        if list_of_numbers[i] < list_of_numbers[j]:
                                            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                                print(f"Sorted list is {list_of_numbers}\n")

                            case "2":
                                print(f"\nUnsorted list is {list_of_numbers}")
                                for i in range(len(list_of_numbers)):
                                    for j in range(len(list_of_numbers)):
                                        if list_of_numbers[i] > list_of_numbers[j]:
                                            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                                print(f"Sorted list is {list_of_numbers}\n")

                elif number.isdigit() or number.lstrip("-").isdigit():
                    list_of_numbers.append(number)

                else:
                    print("Invalid input")