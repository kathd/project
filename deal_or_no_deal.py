# Deal or No Deal

import random

# set values
prizes = [.01, 1, 10, 100, 1000, 10000, 50000, 100000, 500000, 1000000]

def draw_case():
    """draw case"""
    print "[1] [2] [3] [4] [5]"
    print "\n[6] [7] [8] [9] [10]\n"

def how_to_play():
    """prints the game instructions"""

def eliminate_cases():
    """eliminates and reveals cases each round"""

def display_prizes():
    """displays remaining prizes available"""

def compute_banker_offer():
    """computes average of remaining boxes"""

def ask_deal_no_deal():
    """asks player to take banker's offer and end game, or reject 
    offer and continue"""

def main_flow():
    """main game"""
    
    while True:
        instructions = raw_input("Are you familiar with the game (Y/N)? ")
        instructions = instructions.lower()
        if instructions == 'y':
            print "Great! Let's Play!\n"
            draw_case()
            while True:
                myCase = raw_input("Choose a case: \n")
                myCase = int(myCase)
                if myCase < 1 or myCase > 10:
                    print "Choose from the available boxes only"
                else: 
                    sure = raw_input("Are you sure with your pick (Y/N)?")
                    sure = sure.lower()
                    if sure == 'y':
                        print "Let's open some cases!"
                        eliminate_cases()
                    elif sure == 'n':
        
        elif instructions == 'n':
            how_to_play()
        else:
            print "Y or N only please..."


print "Welcome to Deal or No Deal." # short introduction before the game
main_flow()

# Ask to choose 1 out of 10 boxes with random cash amts
# 10 boxes = .01, 1, 10, 100, 1000, 10000, 50000, 100000, 500000, 1000000
# Ask player if she's sure about her choice (Y/N)
# if sure, start game
# if not, ask to choose again
# if answer is not Y/N, show error message

# Let's play!

# Round 1: eliminate 4 boxes
# Call Function B 4x
### FUNCTION B: TO ELIMINATE AND REVEAL
# ask to eliminate a box
# reveal the cash amount

### FUNCTION C: TO SHOW AVAILABLE PRIZES
# show all the prizes not eliminated yet

### FUNCTION D: computes the average of the remaining prizes
# banker offers cash amount equivalent to the average of the remaining prizes

### FUNCTION E: ask DEAL or NO DEAL
# DEAL or NO DEAL
# if player chooses DEAL, end game and print cash amount offered by banker
# if player chooses NO DEAL, proceed to next round

# Round 2: eliminate 3 boxes
# Call Function B 3x
### FUNCTION B
# ask to eliminate a box
# reveal the cash amount

### FUNCTION C
# show all the prizes not eliminated yet

### FUNCTION D
# banker offers cash equivalent to the ave of remaining prizes

### FUNCTION E
# DEAL or NO DEAL
# if player chooses DEAL, end game and print cash amount offered by banker
# if player chooses NO DEAL, proceed to next round

# Round 3: eliminate 1 boxes 
# Call function B 1x
### FUNCTION B

### FUNCTION C

### FUNCTION D

### FUNCTION E

# Round 5 - FINAL ROUND: eliminate 1 box
### FUNCTION F
# ask if player wants to interchange the boxes
# if yes, interchange
# if no, continue
# open box
# player wins what's inside the box




### There should be a list for remaining prizes

