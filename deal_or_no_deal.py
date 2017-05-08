# Deal or No Deal
import random

# set values
prizes = random.sample([.01, 1, 10, 100, 1000, 10000, 50000, 100000, 500000, 1000000], 10)
cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cases_dict = {}

for i in range(len(cases)):
    prizes[i]
    cases[i]
    cases_dict[cases[i]] = prizes[i]

# to store removed cases
removed_cases = []

# to store player's selected case

selected_case = []

# range(1,11) = random.choices(prizes)

# def draw_case():
#     """draw case"""

#     print "\n[1] [2] [3] [4] [5]"
#     print "\n[6] [7] [8] [9] [10]\n"


def how_to_play():
    """prints the game instructions"""

    while True:
        instructions = raw_input("Are you familiar with the game (Y/N)? ")
        instructions = instructions.lower()
        
        if instructions == 'y':
            print "\nGreat! Let's Play!"
            break
        
        elif instructions == 'n':
            print "\n<INSERT INSTRUCTIONS HERE>"
            print "\nNow let's play!"
            break
        
        else:
            print "\nY or N only please..."
            continue


def eliminate_cases(turn, player_case, removed_cases, cases_dict):
    """eliminates and reveals cases 3x"""

    # print cases_dict[player_case]

    while turn != 0:
        #draw_case()
        case_to_remove = raw_input("Choose a case to remove: ")
        if case_to_remove.isdigit():
            case_to_remove = int(case_to_remove)
        else:
            "Choose from the available boxes only"
            continue
        
        if case_to_remove == player_case:
            print "This is the case you have selected"
            continue
        elif case_to_remove < 1 or case_to_remove > 10:
            print "Choose from the available boxes only"
            print cases_dict.keys()
            continue        
        elif case_to_remove in removed_cases:
            print "This case has been removed.\n"
            continue        
        else:
            print "$ " + str(cases_dict[case_to_remove]) + " is out.\n"
            del cases_dict[case_to_remove]
            removed_cases.append(case_to_remove)
            turn = turn - 1

    print "\nAmounts still in play: " + str(cases_dict.values())
    compute_banker_offer(cases_dict)


def compute_banker_offer(cases_dict):
    """computes average of remaining boxes"""

    banker_offer = sum(cases_dict.values()) / len(cases_dict.values())
    print "The Banker wants to buy your case for $ " + str(banker_offer) + "."

    ask_deal_no_deal(banker_offer)


def ask_deal_no_deal(banker_offer):
    """asks player to take banker's offer and end game, or reject 
    offer and continue"""

    while True:    
        decision = raw_input("\nDEAL OR NO DEAL \n\n> ")
        decision = decision.upper()
        if decision == "DEAL":
            print "CONGRATULATIONS! YOU WON $ " + str(banker_offer) + "."
            open_player_case(selected_case, banker_offer)
        elif decision == "NO DEAL":
            print "Let's proceed to the next round!"
            break ### HOW DO I GET OUT OF THE LOOP *AND* THE FUNCTION TO CONTINUE TO ROUND 2???
        else:
            "DEAL or NO DEAL only please."
            continue

def open_player_case(selected_case, banker_offer):
    """opens player's case when player chooses DEAL"""

    print "THE PRIZE IN YOUR CASE IS "
    for i in selected_case:
        print "$ " + str(i)
    if banker_offer < selected_case[0]:
        print "YOU GOT THE LOWER PRIZE, BUT NOT BAD."
    elif banker_offer > selected_case[0]:
        print "CONGRATULATIONS! YOU GOT THE HIGHER PRIZE!"

    exit()


def main_flow():
    """main game"""


    print "\nWelcome to Deal or No Deal!\n"

    how_to_play()

    while True:
        player_case = raw_input("\nChoose a case: ")
        if player_case.isdigit():
            player_case = int(player_case)
        else:
            print "Choose from the available boxes only"
            print cases_dict.keys()
            continue

        if player_case < 1 or player_case > 10:
            print "Choose from the available boxes only"
            print cases_dict.keys()
        
        else: 
            while True:
                sure = raw_input("\nAre you sure with your pick (Y/N)? ")
                sure = sure.lower()
            
                if sure == 'y':
                    player_prize = cases_dict[player_case]
                    del player_prize
                    selected_case.append(cases_dict[player_case])
                    print "\nGreat! Let's try your luck and open some cases!\n"

                   #ROUND 1
                    eliminate_cases(4, player_case, removed_cases, cases_dict)
                    compute_banker_offer(cases_dict)
                    ask_deal_no_deal(banker_offer)

                    #ROUND 2
                    eliminate_cases(3, player_case, removed_cases, cases_dict)

                    #ROUND 3
                    eliminate_cases(2, player_case, removed_cases, cases_dict)

                elif sure == 'n':
                    print "Take your time!"
                    break
            
                else:
                    print "Y or N only please."
                
        


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

