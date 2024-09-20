

#list_of_numbers = [-4, -9, -3, -199, -200, -400, -23, 4, 7, -400, -300, -200, 7, 5, 9, 140, 499]
def bubble_sort_decreasing(list_of_numbers):
    print(f"\nUnsorted list is {list_of_numbers}")

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if list_of_numbers[i] > list_of_numbers[j]: #decreasing
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]

    print(f"Sorted list is {list_of_numbers}")

def bubble_sort_increasing(list_of_numbers):
    print(f"\nUnsorted list is {list_of_numbers}")
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if list_of_numbers[i] < list_of_numbers[j]: #decreasing
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]

    print(f"Sorted list is {list_of_numbers}")

def start_bubble(list_of_numbers):
    while True:
        number = input("Please enter a number or 'end' to sort the numbers: ")

        if number == "end":
            if len(list_of_numbers) == 0:
                print("The list is empty")

            else:
                sort_choice = input(
                    "Enter '1' or '2' to sort from: \n1. 'min' to 'max' (increasing)\n2. 'max' to 'min' (decreasing)")
                match sort_choice:
                    case "1":
                        bubble_sort_increasing(list_of_numbers)

                    case "2":
                        bubble_sort_decreasing(list_of_numbers)

        elif number.isdigit() or number.lstrip("-").isdigit():
            list_of_numbers.append(number)

        else:
            print("Invalid input")








