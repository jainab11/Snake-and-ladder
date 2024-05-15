"""@Author: Jainab sheikh

@Date: 2024-05-15 11:32

@Title : Program Aim
"""
import random
from roll_dice import roll_dice

def check_option(player_position, dice_roll):
    """
    Check the option (No Play, Ladder, or Snake) based on the dice roll.
    Update the player's position accordingly.

    Parameters:
    - player_position (int): Current position of the player.
    - dice_roll (int): Number obtained from rolling the dice.
    
    Returns:
    - Updated position of the player.
    """
    options = ["No Play", "Ladder", "Snake"]
    option = random.choice(options)
    if option == "Ladder":
        print("Ladder! Moving ahead...")
        player_position += dice_roll
    elif option == "Snake":
        print("Snake! Moving back...")
        player_position -= dice_roll  
        if player_position < 0:
            player_position = 0
    else:
        print("No Play! Staying in the same position...")
    return player_position
