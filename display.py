
def display_menu():
    print("================================")
    print("          ROLL DICE")
    print("================================")
    print("1. Start New Game")
    print("2. View Game History")
    print("3. View Statistics")
    print("4. Exit")
    print("\nChoose an option: ")


def display_game_results(game):
    pass


def display_game_history(history):
    pass


def display_statistics(history):
    pass

def print_new_game(player_name, rounds):
    print("================================")
    print("          NEW GAME")
    print("================================")
    print(f"\n player naem : {player_name} \n number of rounds : {rounds} ")

def print_round(round_number):
    print(f"\n           ROUND {round_number}\n")


def display_round_results(player_name,player_score, computer_score,winner):
    print("================================")
    print("          ROUND RESULTS")
    print("================================\n")
    print(f"{player_name} score : {player_score} \ncomputer score : {computer_score} ")
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins this round!\n")
  

