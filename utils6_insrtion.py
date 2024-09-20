

array = [1, 8, 4, 10, -7, -9, -5, 120, -9, -120, 0, 46]
print(array)
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

insertion_sort_increasing(array)
print(array)