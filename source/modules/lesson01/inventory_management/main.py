# Launches the user interface for the inventory management system
import sys
import market_prices

def mainMenu(user_prompt=None):
    """
    Prompt user to send a Thank You, Create a report, create letters, or quit.
    """
    valid_prompts = {"1": addNewItem,
                     "2": printInventory,
                     "q": exitProgram}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Add a new item to the inventory")
        print("2. List all items in the inventory")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)

def getPrice():
    print("Get price")

def addNewItem():
    print("Add new item")

def printInventory():
    print("Print inventory")

def exitProgram():
    sys.exit()

if __name__ == '__main__':
    while True:
        mainMenu()()
        input("Press Enter to continue...........")
