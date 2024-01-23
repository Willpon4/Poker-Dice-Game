"""Test the score_dice module.

Name: Will Ponczak
Date: 10/29/23
"""

import score_dice as sd


def test_one_pair():
    assert sd.calculate_score(['9', '9', '10', 'J', 'K'], sd.PAIR) == 18
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.PAIR) == 0
    
    
def test_two_pair():
    assert sd.calculate_score(['9', '9', 'J', 'J', 'K'], sd.TWO_PAIR) == 38
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.TWO_PAIR) == 0
    
    
def test_three_of_kind():
    assert sd.calculate_score(['9', '9', '9', 'Q', 'K'], sd.THREE_OF_KIND) == 37
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.THREE_OF_KIND) == 0
    
    
def test_four_of_kind():
    assert sd.calculate_score(['9', '9', '9', '9', 'K'], sd.FOUR_OF_KIND) == 56
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.FOUR_OF_KIND) == 0
    

def test_five_of_kind():
    assert sd.calculate_score(['9', '9', '9', '9', '9'], sd.FIVE_OF_KIND) == 100
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.FIVE_OF_KIND) == 0
    
    
def test_full_house():
    assert sd.calculate_score(['9', '9', '9', 'K', 'K'], sd.FULL_HOUSE) == 97
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.FULL_HOUSE) == 0
    
    
def test_small_straight():
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'A'], sd.SMALL_STRAIGHT) == 70
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.SMALL_STRAIGHT) == 0
    

def test_large_straight():
    assert sd.calculate_score(['9', 'Q', 'J', '10', 'K'], sd.LARGE_STRAIGHT) == 95
    assert sd.calculate_score(['9', 'A', 'J', 'Q', 'K'], sd.LARGE_STRAIGHT) == 0
    

def test_chance():
    assert sd.calculate_score(['K', 'Q', 'J', '10', 'K'], sd.CHANCE) == 50
