"""Plays a text based game of Poker Dice.

Author: Will Ponczak
Version: 10/29/23
"""

import dice

PAIR = 1
TWO_PAIR = 2
THREE_OF_KIND = 3
FOUR_OF_KIND = 4
FIVE_OF_KIND = 5
FULL_HOUSE = 6
SMALL_STRAIGHT = 7
LARGE_STRAIGHT = 8
CHANCE = 9

ss1 = ['9', '10', 'J', 'Q']
ss2 = ['10', 'J', 'Q', 'K']
ss3 = ['J', 'Q', 'K', 'A']

ls1 = ['9', '10', 'J', 'Q', 'K']
ls2 = ['10', 'J', 'Q', 'K', 'A']


def calculate_score(dice_list, score_type):
    """Calculate the Poker Dice score based on the dice_list and score_type.

    Args:
        dice_list (list): 5 values representing the outcome of the rolls.
        score_type (int): The type (category) to score.

    Returns:
        (int): The score amount.
    """
    total = 0
    new_list = []
    count = 0
    type1 = 0
    
    if score_type == 9:
        total = dice.add_values(dice_list)
        return total
    if score_type == 8:
        for element in ls2:
            if element in dice_list:
                count += 1
        if count == 5:
            total = 95
    elif score_type == 8:
        for element in ls1:
            if element in dice_list:
                count += 1
        if count == 5:
            total = 95
    elif score_type == 7:
        for element in ss1:
            if element in dice_list:
                count += 1
        if count >= 4:
            total = 70
    elif score_type == 7:
        for element in ss2:
            if element in dice_list:
                count += 1
        if count >= 4:
            total = 70
    elif score_type == 7:
        for element in ss3:
            if element in dice_list:
                count += 1
        if count >= 4:
            total = 70
    elif score_type == 6:
        for n in dice_list:
            for x in dice_list:
                if dice_list.count(n) == 3:
                    if dice_list.count(x) == 2:
                        if n != x:
                            type1 = new_list.append((n * 2))
                            type1 = new_list.append((x * 3))
                            total = list_score(type1)
    if score_type == 5:
        for element in dice_list:
            if dice_list.count(element) == 5:
                total = 100
    if score_type == 4:
        for element in dice_list:
            if dice_list.count(element) == 4:
                type1 = new_list.append((element * 4))
                total = list_score(type1)
    if score_type == 3:
        for element in dice_list:
            if dice_list.count(element) == 3:
                type1 = new_list.append((element * 3))
                total = list_score(type1)
    if score_type == 2:
        for n in dice_list:
            for x in dice_list:
                if dice_list.count(n) == 2:
                    if dice_list.count(x) == 2:
                        if n != x:
                            type1 = new_list.append((x * 2))
                            type1 = new_list.append((n * 2))
                            total = list_score(type1)
    if score_type == 1:
        for element in dice_list:
            if dice_list.count(element) == 2:
                type1 = new_list.append((element * 2))
                total = list_score(type1)
                
    return total


def list_score(dice_list):
    """Calculate the score of certain rolls 1-6.

    Args:
        dice_list (list): 5 values representing the outcome of the rolls.

    Returns:
        (int): The score amount.
    """
    total = 0
    
    for x in dice_list:
        if x == 1:
            total = dice.add_values(x)
        elif x == 2:
            total = dice.add_values(x)
        elif x == 3:
            total = dice.add_values(x) + 10
        elif x == 4:
            total = dice.add_values(x) + 20
        elif x == 6:
            total = dice.add_values(x) + 50
    return total
