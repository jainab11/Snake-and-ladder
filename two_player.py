from mover_player import check_option
from roll_dice import roll_dice

def play_game_with_two_players():
    player_positions = [0, 0]
    players = ["player1", "player2"]
    dice_rolls = [0, 0]
    
    while True:
        for play, player in enumerate(players):
            dice_roll = roll_dice()
            player_positions[play] = check_option(player_positions[play], dice_roll)
            print(f"{player} Rolled a {dice_roll}. Current position: {player_positions[play]}")
            dice_rolls[play] += 1
            
            if player_positions[play] >= 100:
                print(f"Congratulations, {player}! You won the game in {dice_rolls[play]} dice rolls.")
                return

# Call the function to start the game
play_game_with_two_players()
