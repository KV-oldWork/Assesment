import csv
def main():
    load_information()
    while True:
        mainMenuOutput = mainMenu()
        items = mainMenuOutput[1]
        if mainMenuOutput[0] == 'R':
            required_items()
        if mainMenuOutput[0] == 'C':
            required_items()
        if mainMenuOutput[0] == 'A':
            required_items()
        if mainMenuOutput[0] == 'M':
            mark_completed()
        if mainMenuOutput[0] == 'Q':
            break

def load_information():
    items = open("items.csv")
    numberOfItems = sum(1 for row  in items)  # calculates the number of items
    print("shopping list 1.0 - by Kyle Vincent")
    print("{} items loaded from {}".format(numberOfItems, items.name))

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

def required_items():
        file = open("items.csv",)
        delimit_file = csv.reader(file, delimiter=",")
        item_storage = []
        item_number = int(1)
        for line in delimit_file:
            item_storage.append(line)
        for row in item_storage: #Making progress towards finishing the file calling for loop.
            if "r" in row:
                print("({}) {} ${:>10} ".format(item_number, row[0], row[1], row[2]))
                item_number += 1

        file.close()
        return item_storage

def mark_completed():
    file = open("items.csv", )
    delimit_file = csv.reader(file, delimiter=",")
    item_storage = []
    item_number = int(0)
    for line in delimit_file:
        item_storage.append(line)
    for row in item_storage:  # calls the file, and prints it with file formating
        if "r" in row:
            print("({}) {} ${:>10} ".format(item_number, row[0], row[1], row[2]))
            item_number += 1
    interval_conversion = []
    for row in item_storage:
        interval_conversion.append(row[1])
    interval_conversion = [float(i) for i in interval_conversion]
    expected_price = sum(interval_conversion) #Calculates the expected price and presents it to the user
    print ("Total expected price for {} items: ${}\nEnter the number of an item to mark as completed".format(item_number, expected_price))
    #counts number of rows, if input exceeds rows the error, for later, input 1 will be 0 on the list.
    numberOfItems = sum(1 for row in item_storage)
    user_input_completed = int(input())
    while user_input_completed > numberOfItems: #error checking to check variable qualithy,
        print("Invalid input")
        user_input_completed = int(input())



    file.close()

main()

