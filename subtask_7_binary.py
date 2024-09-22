
def binary_search(arr, target):
    """
    :param arr: list of numbers where to find the target
    :param target: - our searched number
    :return: - the index of the target found or '-1' if target not found
    """
    print(binary_search.__doc__)
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        #If x is greater, ignore left half
        if arr[mid] < target:
            low = mid + 1

        #If x is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1

        #means target is present at mid
        else:
            print(f"\n'{target}' found at index {mid}\n")
            return mid

    #If we reach here, then the element was not present
    print(f"\n'{target}'s index is '-1'\n")
    return -1


