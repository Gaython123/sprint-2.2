array = [7, 4, 2, -8, -4, -400, 10000, 240, -600, -920]
def selection_sort_increasing(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    print(f"Sorted list is {array}")

selection_sort_increasing(array, len(array))

def selection_sort_decreasing(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):

            # select the minimum element in each loop
            if array[i] > array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    print(f"Sorted list is {array}")

selection_sort_decreasing(array, len(array))

def start_selection(list_of_numbers, size):
    while True:
        number = input("Add a number or 'end' to sort the numbers: ")

        if number == "end":
            if len(list_of_numbers) == 0:
                print("The list is empty")

            else:
                sort_choice = input(
                    "Enter '1' or '2' to sort from: \n1. 'min' to 'max' (increasing)\n2. 'max' to 'min' (decreasing)")
                match sort_choice:
                    case "1":
                        selection_sort_increasing(array, len(array))

                    case "2":
                        selection_sort_decreasing(array, len(array))

        elif number.isdigit() or number.lstrip("-").isdigit():
            list_of_numbers.append(number)

        else:
            print("Invalid input")