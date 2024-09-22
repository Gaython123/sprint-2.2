import random

def menu():
    print("Enter your choice:\n"
                    "1. Linear search "
                    "2. Binary search "
                    "3. ")




def linear_search(array, target):
    if target in array:
        target_index = array.index(target)
        print(f"\n'{target}'s index is '{target_index}'\n")

    elif target not in array:
        print(f"\n'{target}'s index is '-1'\n")

