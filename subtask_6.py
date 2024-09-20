from utils6_bubble import *
from utils6_selection import *

numbers_bubbles = []
numbers_selection = []
numbers = []
while True:
    user_list = input("choose option: ")

    match user_list:
        case "1":
            start_bubble(numbers_bubbles)

        case "2":
            start_selection(numbers_selection, len(numbers_selection))




