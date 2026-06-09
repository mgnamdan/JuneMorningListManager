# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FILE FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadList():
    pass


def saveList():
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def addItems():
    pass


def removeItems():
    pass


def editItems():
    pass


def moveItems():
    pass



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRINT FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def printOptions():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("                MENU")
    print("")
    print("         1. View List")
    print("         2. Add Item(s)")
    print("         3. Remove Item(s)")
    print("         4. Edit Item(s)")
    print("         5. Move Item(s)")
    print("         6. Exit")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


def printList():
    pass




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True

    while appOn:
        # PUT INTO VALIDATION LOOP
        printOptions()
        userChoice = input(" --> ")
        # ACCOUNT FOR STRINGS AND INTS?
        if userChoice == "1":
            printList()
        elif userChoice == "2":
            addItems()
        elif userChoice == "3":
            removeItems()
        elif userChoice == "4":
            editItems()
        elif userChoice == "5":
            moveItems()
        else:
            appOn = False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
