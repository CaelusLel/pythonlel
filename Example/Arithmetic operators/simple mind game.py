
def play_game(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Get input from players
player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ")
player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ")

# Play the game
result = play_game(player1_choice, player2_choice)
print(result)
