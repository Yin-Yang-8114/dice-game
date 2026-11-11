from validations import validate_input
from random import randint
from display import print_new_game, display_round_results,print_round,display_game_results
from logic import calculate_winner

user_choice = lambda: validate_input("Enter your choice (1-4): ", "positive_int")

def get_player_names():
    player_name = validate_input("Enter your name: ", "str")
    return player_name

def number_of_rounds():
    rounds = validate_input("Enter the number of rounds you want to play (1-10): ", "positive_int")
    if rounds < 1 or rounds > 10:
        print("Please enter a number between 1 and 10.")
        return number_of_rounds()
    return rounds


def roll_dice():
    return randint(1, 6)

def play_round(player_name,round_number):
    print_round(round_number)
    player_score = roll_dice()
    computer_score = roll_dice()
    winner = calculate_winner(player_score, computer_score,player_name)
    display_round_results(player_name, player_score, computer_score, winner)

def start_game():
    player_name = get_player_names()
    rounds = number_of_rounds()
    print_new_game(player_name, rounds)
    for round_number in range(1, rounds + 1):
        play_round()

    # display_game_results(game)







