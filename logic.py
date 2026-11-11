def calculate_winner(player_score, computer_score,player_name):
    if player_score > computer_score:
        return f"{player_name}"
    elif computer_score > player_score:
        return "Computer"
    else:
        return "Tie"