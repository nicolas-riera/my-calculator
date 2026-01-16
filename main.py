# Libraries

from src.menu import menu
from src.clear import clear
from src.history import create_json_if_not_found

# Main program

if __name__ == "__main__":

    clear()
    create_json_if_not_found()

    menu()
    