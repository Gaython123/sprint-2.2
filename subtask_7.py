import random
from subtask_7_linear import *
from subtask_7_binary import *

while True:
    menu()
    user_choice = input()

    match user_choice:
        case "1":
            array = list(range(1, 10))
            random.shuffle(array)
            print(array)

            target = int(input("\nEnter a number to get its index, "
                               "\nor '0' to finish"))

            linear_search(array, target)

        case "2":
            array = list(range(1, 10))
            print(array)

            target = int(input("\nEnter a number to get its index, \nor '0' to finish\n"))
            binary_search(array, target)

        case "3":
            array = list(range(1, 10))
            random.shuffle(array)
            print(array)

            target = int(input("\nEnter a number to get its index, \nor '0' to finish \n"))
            binary_search(array, target)
            print("\nBinary search doesnt work for unsorted arrays\n")

        case "0":
            break






