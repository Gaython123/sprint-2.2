def bubble_sort_decreasing(list_of_numbers):
    """
    Parameters
    ----------
    list_of_numbers  "list to sort"

    Returns sorted list_of_numbers in 'Descending' order
    -------

    """
    print(bubble_sort_decreasing.__doc__)
    print(f"\nUnsorted list is {list_of_numbers}")

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if list_of_numbers[i] > list_of_numbers[j]: #decreasing
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                print(f"Sorted list is {list_of_numbers}")

def bubble_sort_increasing(list_of_numbers):
    """
   Parameters
    ----------
    list_of_numbers  "numbers to sort"

    Returns sorted list_of_numbers in 'Ascending' order
    -------
    """
    print(bubble_sort_increasing.__doc__)
    print(f"\nUnsorted list is {list_of_numbers}")
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if list_of_numbers[i] < list_of_numbers[j]: #decreasing
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                print(f"Sorted list is {list_of_numbers}")



choice = input("Please:"
               " '1' for Ascending order"
               " '2' for Descending order")
number = input("Please enter a number or 'end' to sort the numbers: ")
def start_bubble(list_of_numbers, choice):
    """
    Parameters
    ----------
    list_of_numbers - list of numbers to sort
    choice - user chooses to sort:
     from 'min to max'
     from 'max to min'

    Returns sorted list of number in "Ascending" or "Descending" order
    -------
    """

    while True:
        if number == "end":
            if len(list_of_numbers) == 0:
                print("The list is empty")

            elif choice == "1":
               bubble_sort_increasing(list_of_numbers)

            elif choice == "2":
                bubble_sort_decreasing(list_of_numbers)

            else:
                print("Invalid choice")

        elif number.isdigit() or number.lstrip("-").isdigit():
            list_of_numbers.append(number)

        else:
            print("Invalid input")








