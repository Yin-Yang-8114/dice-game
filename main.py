from display import display_menu
from validations import validate_input
from func import user_choice





def main():
    while True:
        display_menu()
        choice = user_choice()
        match choice:
            case 1:
                pass  # Start New Game logic goes here
            case 2:
                pass # View Game History logic goes here
            case 3:
                pass # View Statistics logic goes here
            case 4:
                print("Exiting the game. Goodbye!")
                break
            case _:
                print("chose between 1-4 only.")


if __name__ == "__main__":
    main()