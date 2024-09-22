from utils6_bubble import *
from utils6_selection import *
from utils6_insrtion import *
from utils6_menu import *

numbers_bubbles = []
numbers_selection = []
numbers_insertion = []
menu()

while True:
    menu()
    user_list = input("choose option: "
                      "'(1-3) for 'sort',"
                      "'help' to see the options and "
                      "'0' for exit'")

    match user_list:
        case "1":
            choice = input("Please choose:"
                           "'1' to sort in 'Ascending' order"
                           "'2' to sort in 'Descending' order")

            number = input("Please enter a number or 'end' to sort the numbers: ")

            start_bubble(numbers_bubbles, choice)

        case "2":
            start_selection(numbers_selection, len(numbers_selection))

        case "3":
            start_insertion(numbers_insertion)

        case "0":
            break

        case "help":
            menu()



