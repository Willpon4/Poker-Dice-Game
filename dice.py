"""Project 1.0 Poker Dice (Dice.py).

Author: Will Ponczak
Version: 10/19/2023
"""
import random

FACES = ['9', '10', 'J', 'Q', 'K', 'A']
FACE_VALUES = {'9': 9, '10': 10, 'J': 10,
               'Q': 10, 'K': 10, 'A': 11}


def roll_dice(num_dice='', seed=0):
    """Determine the faces in the dice list.

    Args:
        num_dice (int): Number of dice rolls.
        seed (int): Random seed integer.
        
    Returns:
        list: List of die faces.
    """
    q = 0 
    dice_list = [] 
    out_of_range = '9' 
    
    if num_dice is None: 
        random.seed(seed)
        while q != 5: 
            dice_list.append(random.choice(FACES)) 
            q += 1 
        return dice_list
    
    if seed is None:
        q = 0
        while q != num_dice:
            dice_list.append(random.choice(FACES)) 
            q += 1
        return dice_list
    
    if num_dice < 1 or num_dice > 10: 
        return [out_of_range]
    
    random.seed(seed)
    while num_dice != q: 

        dice_list.append(random.choice(FACES)) 
        q += 1 
    return dice_list 

    
def are_valid(dice_rolls):
    """Determine if the list of faces is valid.

    Args:
        dice_rolls (list): List of faces.
        
    Returns:
        bool: True or False.
    """
    if dice_rolls is None: 
        return False
    for element in dice_rolls: 
        if element not in FACES: 
            return False 
    if len(dice_rolls) < 1 or len(dice_rolls) > 10: 
        return False
    if len(dice_rolls) >= 1 and len(dice_rolls) <= 10:
        return True
    else:
        return False


def add_values(dice):
    """Add the values of the die faces.

    Args:
        dice (list): Dice faces.
        
    Returns:
        int: Total value of the dice faces.
    """
    is_valid = are_valid(dice)
    total = 0
    if is_valid is False:
        return -1
    else:
        for element in dice:
            if element in FACE_VALUES:
                total += FACE_VALUES[element]
        return total


def num_faces(dice_list, face):
    """Determine the number of a specific face in the list.

    Args:
        dice_list (list): List of dice faces.
        face (str): Specified face.
        
    Returns:
        int: Number of specified faces.
    """
    num_face = 0
    valid_dice_list = are_valid(dice_list)
    
    if valid_dice_list is False:
        return -1
    else:
        for n in dice_list:
            if n == face:
                num_face += 1 
        return num_face
