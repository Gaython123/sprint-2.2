import random

def menu():
    """

    :return: all the options available
    """
    print("Enter your choice:"
                    "\n1. Linear search "
                    "\n2. Binary search with sorted list"
                    "\n3. Binary search with unsorted list")




def linear_search(array, target):
    """
    :param array: - list of numbers where to find the target
    :param target: - a number to search for
    :return: index of the searched number, or '-1' if target is not found
    """
    print(linear_search.__doc__)

    if target in array:
        target_index = array.index(target)
        print(f"\n'{target}'s index is '{target_index}'\n")

    elif target not in array:
        print(f"\n'{target}'s index is '-1'\n")

