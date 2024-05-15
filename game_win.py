from mover_player import check_option
from roll_dice import roll_dice

def play_game():
    player_pos = 0
    while player_pos <=100:
        dice_roll = roll_dice()
        player_pos = check_option(player_pos,dice_roll)
        print(f"Rolled a {dice_roll}. Current position: {player_pos}")

    print("Congratulations! You reached the winning position.")
play_game()