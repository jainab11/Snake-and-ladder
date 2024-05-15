from mover_player import check_option
from roll_dice import roll_dice

def play_game():
    """
    Simulate the Snake and Ladder game played by a single player.
    """
    player_position = 0  # Starting position at 0
    dice_rolls = 0  # Initialize the number of dice rolls

    while player_position < 100:  # Continue playing until reaching or exceeding the winning position
        dice_roll = roll_dice()
        player_position = check_option(player_position, dice_roll)
        print(f"Rolled a {dice_roll}. Current position: {player_position}")
        dice_rolls += 1  # Increment the number of dice rolls

    print(f"Congratulations! You reached the winning position in {dice_rolls} dice rolls.")

# Example usage:
play_game()
