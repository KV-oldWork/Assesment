import csv
def main():
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
            required_items()
        if mainMenuOutput[0] == 'Q':
            break


def mainMenu():
    items = open("items.csv")
    numberOfItems = sum(1 for row in items)  # calculates the number of items
    print("shopping list 1.0 - by Kyle Vincent")
    print("{} items loaded from {}".format(numberOfItems, items.name))
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
        for line in delimit_file:
            item_storage.append(line)
        file.close()
        list_length = len(item_storage)
        for x in range(0, list_length): #Making progress towards finishing the file calling for loop.
            print ("x")

        print(item_storage[0][0])
        return item_storage

main()