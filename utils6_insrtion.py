def insertion_sort_increasing(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print(array)

def insertion_sort_decreasing(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print(array)

def start_insertion(array):
    while True:
        number = input("Please enter a number or 'end' to sort the numbers: ")

        if number == "end":
            if len(array) == 0:
                print("The list is empty")

            else:
                sort_choice = input(
                    "Enter '1' or '2' to sort from: \n1. 'min' to 'max' (increasing)\n2. 'max' to 'min' (decreasing)")
                match sort_choice:
                    case "1":
                        insertion_sort_increasing(array)

                    case "2":
                        insertion_sort_decreasing(array)

        elif number.isdigit() or number.lstrip("-").isdigit():
            array.append(number)

        else:
            print("Invalid input")