""" IT@JCU CP1404 Assignment 1 from 2016
    Shopping List
    Kyle Vincent
    08/09/2016

Pseudocode:

function main()
    load_information()
    completed item list storage
    while True
        run mainMenu
        if main menu output is m
            runs function mark_completed()
        if main menu output is c
            runs function list_completed()
        if main menu output is a
            runs function add_new_items()
        if main menu output is r
            runs function required_items()
        if main menu output is q
            runs function endProgram
            breaks

function mainMenu
    prints user options
    gets user input
    while user input not in user options
        print invalid input
        gets user input
        makes user input upperCase
    returns user input


function load_information()
    opens items.csv
    counts number of rows in items.csv
    prints tittle
    prints number of rows loaded from items.csv

function required_items()
    opens items.csv
    counts number of rows in items.csv
    delimit_file is csv.reader
    item_storage list
    for line in delimit_file
        append line to item_storage
    prints 'required items'
        for row in item storage
            print row with formating
    interval_conversion list
    for row in item storage
        append row to interval_conversion
    expected price is sum of interval_conversion
    print expected price
    close file
    return item_storage

function mark_completed()
    opens items.csv
    counts number of rows in items.csv
    delimit_file is csv.reader
    item_storage list
    for line in delimit_file
        append line to item_storage
    prints 'required items'
        for row in item storage
            print row with formating
    interval_conversion list
    for row in item storage
        append row to interval_conversion
    expected price is sum of interval_conversion
    while True
        try
            get desired marked item from user
            while desired marked item bigger than number of items
                print error message
                get desired marked item from user
            break
        except value error
            print error message
    while user input bigger than number of items
        print error message
        get value from user
    print item that is marked as complete
    file.close

function list_completed(completed_item_list)
    opens items.csv
    counts number of rows in items.csv
    delimit_file is csv.reader
    item_storage list
    for line in delimit_file
        append line to item_storage
    if no items in completed_item_list
        print no completed items
        return to main
    print title completed items
    for elem in completed_item_list
        print completed items
    interval_conversion list
    for elem in completed_item_list
        append item storage elem to interval conversion list
    expected price is sum of interval_conversion
    print expected price
    close file

function add_new_items()
    opens items.csv
    holding list
    gets name from user
    while name has no input besides space
        print error message
        gets name from user
    appents name to holding list
    while true
        try
            get float price from user
            while price smaller than 0
                print error message
                get float price from user
            break
        except value error
            print error message
    append price to holding list
    while true
        try
            gets priority int from user
            while priority not a possible prioirity
                print error message
                gets value from user
                if prioirity is in possible prioiritys
                    break
            break
        except value error
            print error message
    appent priority to  holding list
    print holding list added to list
    with items.csv open as outfile
        outfilewriter is csv.writer
        outfilewriter writerows from holding list
    outfile.close

function endProgram
    open items.csv
    delimit file is csv reader
    for line in delimit file
        number of items plus 1
    print number of items saved to csv
    print goodbye message

main()

"""

import csv
#main function, runs the program and calls function.
def main():
    load_information()
    completed_item_list = []
    while True:
        mainMenuOutput = mainMenu()
        items = mainMenuOutput[1]
        if mainMenuOutput[0] == 'M':
            completed_item = mark_completed()
            completed_item_list.append(completed_item)
        if mainMenuOutput[0] == 'C':
            list_completed(completed_item_list)
        if mainMenuOutput[0] == 'A':
            add_new_items()
        if mainMenuOutput[0] == 'R':
            required_items()
        if mainMenuOutput[0] == 'Q':
            endProgram()
            break

#loads the ammount of items in list and displays it at top of program.
def load_information():
    items = open("items.csv")
    numberOfItems = sum(1 for row  in items)
    print("shopping list 1.0 - by Kyle Vincent")
    print("{} items loaded from {}".format(numberOfItems, items.name))

#function for the main menu, prints options, takes input from user and returns their input.
def mainMenu():
    items = open("items.csv")
    print("Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit")
    mainMenuLetters = ["R", "C", "A", "M", "Q"]
    mainMenuInput = input()
    mainMenuInput = mainMenuInput.upper()
    while mainMenuInput not in mainMenuLetters:  #makes sure menu input is valid
        print("invalid input")
        mainMenuInput = input()
        mainMenuInput = mainMenuInput.upper()

    return mainMenuInput, items,

#function for when user inputs R. Opens the file and prints the required items.
def required_items():
        file = open("items.csv",)
        delimit_file = csv.reader(file, delimiter=",")
        item_storage = []
        item_number = int(0)
        for line in delimit_file:
            item_storage.append(line)
        print("Required items:")
        for row in item_storage: #Making progress towards finishing the file calling for loop.
            if "r" in row:
                item_number += 1
                print("({}) {:<23} $ {:<12} ".format(item_number, row[0], row[1], row[2]))
        interval_conversion = []
        for row in item_storage:
            interval_conversion.append(row[1])
        interval_conversion = [float(i) for i in interval_conversion]
        expected_price = sum(interval_conversion)  # Calculates the expected price and presents it to the user
        print("Total expected price for {} items: ${}".format(item_number, expected_price))
        file.close()
        return item_storage

#M function from menu. Marks an item and returns it to a list in the main.
def mark_completed():
    file = open("items.csv", )
    delimit_file = csv.reader(file, delimiter=",")
    item_storage = []
    item_number = int(0)
    for line in delimit_file:
        item_storage.append(line)
    for row in item_storage:  # calls the file, and prints it with file formating
        if "r" in row:
            item_number += 1
            print("({}) {:<23} $ {:<12} ".format(item_number, row[0], row[1], row[2]))
    interval_conversion = []
    for row in item_storage:
        interval_conversion.append(row[1])
    interval_conversion = [float(i) for i in interval_conversion]
    expected_price = sum(interval_conversion) #Calculates the expected price and presents it to the user
    print ("Total expected price for {} items: ${}\nEnter the number of an item to mark as completed".format(item_number, expected_price))
    #counts number of rows, if input exceeds rows the error.
    numberOfItems = sum(1 for row in item_storage)
    while True:
        try:
            user_input_completed = int(input())
            while user_input_completed > numberOfItems:  # error checking to check variable qualiy.
                print("Invalid item number")
                user_input_completed = int(input())
            break
        except ValueError:
            print("Invalid input; enter a valid number")

    while user_input_completed > numberOfItems: #error checking to check variable qualiy.
        print("Invalid item number")
        user_input_completed = int(input())
    user_input_completed -= 1
    print("{} marked as completed".format(item_storage[user_input_completed][0]))
    file.close()

    return user_input_completed

#Function for main menu input C. Shows the user the completed items, tells the user if no items are completed.
def list_completed(completed_item_list):
    file = open("items.csv", )
    delimit_file = csv.reader(file, delimiter=",")
    item_storage = []
    item_number = int(0)
    for line in delimit_file:
        item_storage.append(line)
    if not completed_item_list:
        print("No completed items")
        return False
    print("Completed items:")
    for elem in completed_item_list:
        print("({}) {:<23} $ {:<12} ".format(elem + 1, item_storage[elem][0], item_storage[elem][1],))
    interval_conversion = []
    for elem in completed_item_list:
        interval_conversion.append(item_storage[elem][1])
        item_number += 1
    interval_conversion = [float(i) for i in interval_conversion]
    expected_price = sum(interval_conversion)  # Calculates the expected price and presents it to the user
    print("Total expected price for {} items: ${}".format(item_number, expected_price))

    file.close()

#Function for menu option A. Opens the file and writes new list item to it.
def add_new_items():
    file = open("items.csv", )
    holdingList = []
    possiblePriorities = [1, 2, 3]
    newName = input("Item Name: ")
    while newName.isspace():
        print("Input can not be blank")
        newName = input("Item Name: ")
    holdingList.append(str(newName))
    while True:
        try:
            price = float(input("Price: $"))
            val = float(price)
            while price < 0:
                print("Price must be >= $0")
                price = float(input("Price: $"))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    holdingList.append(str(price))
    while True:
        try:
            priority = int(input("Priority: "))
            while priority not in possiblePriorities:
                print("Priority must be 1, 2 or 3")
                priority = int(input("Priority: "))  # error checking :(
                if priority in possiblePriorities:
                    break
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    holdingList.append(str(priority))
    holdingList.append('r')
    print("{}, ${} (priority {}) added to shopping list".format(holdingList[0], holdingList[1], holdingList[2]))
    with open('items.csv', 'a', newline='') as outFile:
        outFileWriter = csv.writer(outFile)
        outFileWriter.writerow(holdingList)
    outFile.close()

#Function for menu option Q. Ends the function and prints out a goodbye message for the user.
def endProgram():
    file = open("items.csv", )
    delimit_file = csv.reader(file, delimiter=",")
    numberOfItems = int(0)
    for line in delimit_file:
        numberOfItems += 1
    print("{} items saved to items.csv\nHave a nice day :)".format(numberOfItems))

main()

