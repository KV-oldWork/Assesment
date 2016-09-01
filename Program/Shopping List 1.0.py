import csv
def main():
    mainMenuOutput = mainMenu()
    print(mainMenuOutput)

def mainMenu():
    items = open("items.csv")
    numberOfItems = sum(1 for row in items)  # calculates the number of items
    print("shopping list 1.0 - by Kyle Vincent")
    print("{} items loaded from {}".format(numberOfItems, items.name))
    print("Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item as completed\nQ - Quit")
    mainMenuLetters = ["R", "C", "A", "M", "Q"]
    mainMenuInput = input()
    mainMenuInput = mainMenuInput.upper()

    while mainMenuInput not in mainMenuLetters:  #makes sure menu input is valid
        print("invalid input")
        mainMenuInput = input()
        mainMenuInput = mainMenuInput.upper()

    return mainMenuInput


main()

