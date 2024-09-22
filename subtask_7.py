import random
from subtask_7_linear import *


while True:
    menu()
    user_choice = input()

    match user_choice:
        case "1":
            array = list(range(1, 10))
            random.shuffle(array)
            print(array)

            target = int(input("\nEnter a number to get its index, "
                               "\nor index '-1' if not in the array"))

            linear_search(array, target)

        case "2":
            




