from utils6_bubble import *
from utils6_selection import *
from utils6_insrtion import *

numbers_bubbles = []
numbers_selection = []
numbers_insertion = []
while True:
    user_list = input("choose option: ")

    match user_list:
        case "1":
            start_bubble(numbers_bubbles)

        case "2":
            start_selection(numbers_selection, len(numbers_selection))

        case "3":
            start_insertion(numbers_insertion)

        case "0":
            break



