def selection_sort_increasing(array, size):
    """

    Parameters
    ----------
    array - numbers to sort
    size - the length of the array

    Returns - sorted array in 'Ascending order'
    -------

    """
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

def selection_sort_decreasing(array, size):
    """

      Parameters
      ----------
      array - numbers to sort
      size - the length of the array

      Returns - sorted array in 'Descending' order
      -------

      """
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):

            # select the minimum element in each loop
            if array[i] > array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        print(f"Sorted list is {array}")

def start_selection(array, size):
    while True:
        number = input("Add a number or 'end' to sort the numbers: ")

        if number == "end":
            if len(array) == 0:
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
            array.append(number)

        else:
            print("Invalid input")