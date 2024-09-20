from utils6 import *

#list_of_numbers = []
while True:

    user_list = input("choose option: ")

    match user_list:
        case "1":
            list_of_numbers = []
            while True:
                number = input("Please enter a number or 'end' to sort the numbers: ")

                if number == "end":
                    if len(list_of_numbers) == 0:
                        print("The list is empty")

                    else:
                        sort_choice = input("Enter '1' or '2' to sort from: \n1. 'min' to 'max' (increasing)\n2. 'max' to 'min' (decreasing)")
                        match sort_choice:
                            case "1":
                                bubble_sort_increasing(list_of_numbers)

                            case "2":
                                bubble_sort_decreasing(list_of_numbers)

                elif number.isdigit() or number.lstrip("-").isdigit():
                    list_of_numbers.append(number)

                else:
                    print("Invalid input")