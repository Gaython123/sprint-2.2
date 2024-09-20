from utils6_bubble import *

list_of_numbers = []
while True:
    user_list = input("choose option: ")

    match user_list:
        case "1":
            start_bubble(list_of_numbers)

        case "2":
