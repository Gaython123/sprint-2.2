

list_of_numbers = [-4, -9, -3, -199, -200, -400, -23, 4, 7, -400, -300, -200, 7, 5, 9, 140, 499]
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

def bubble_function:


