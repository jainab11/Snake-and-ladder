from game_win import play_game
from mover_player import check_option
from roll_dice import roll_dice
def check_winning_pos():
    player_pos  = 0
    while player_pos < 100:
        dice_roll = roll_dice
        player_pos = check_option(player_pos , dice_roll)
        
    return player_pos  == 100
if check_winning_pos():
    print("Congratulations! You won the game.")
else:
    print("Better luck next time! Try again.")
