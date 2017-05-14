# Deal or No Deal (Modified)
# Hackbright Prep Project, May 2017
# by Kathleen Domingo


import random
# set values

# set prize values randomize prizes
prizes = random.sample([.01, 5, 25, 75, 200, 400, 750, 1000, 10000, 50000, 100000, 300000, 500000, 1000000], 14)

# set case values
cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# where cases and prizes will be stored
cases_dict = {}

# used to access the indexes of prizes and cases lists
for i in range(len(cases)):
    prizes[i]
    cases[i]
    cases_dict[cases[i]] = prizes[i] # adds keys and values to cases_dict

# where eliminated cases will be stored
removed_cases = []

# where player's case and prize will be stored
selected_dict = {}

# where the last remaining case will be stored
swapped_dict = {}

def show_cases(cases, removed_cases):
    """shows the cases still in play, and crosses out the selected and
    eliminated cases"""

    for case in cases:
        if case in removed_cases:
            print "x",
        else:
            print case,

    print "\n"

def show_prizes(cases_dict):
    """shows available prizes"""

    print "\nAmounts still in play:\n " #+ str(cases_dict.values())
    available_prizes = cases_dict.values()
    for prize in sorted(prizes): # sorts the prizes from lowest to highest
        if prize in available_prizes:
            print prize

    print "\n"


def how_to_play():
    """prints the game instructions if player wants to know how the game is played"""

    while True:
        instructions = raw_input("Are you familiar with the game (Y/N)? ")
        instructions = instructions.lower()
        
        if instructions == 'y':
            print "\nGreat! Let's Play!\n\n"
            break
        
        elif instructions == 'n':
            print "\nThe mission is to win the $1M or the higher amount between the banker's offer and your selected case.\n\n"
            print "Player selects 1 out of 14 cases full of varying amounts of virtual cash - ranging from $.01 to $1M.\n\n"
            print "On each round, the player chooses to eliminate and reveal some of the remaining cases.\n\n"
            print "Then the Banker offers to buy the player's case at the end of each round.\n\n"
            print "The player can accept the offer and end the game by saying 'DEAL' or reject it and continue the game by saying 'NO DEAL'.\n\n"            
            print "Now let's play!\n"
            break
        
        else:
            print "\nY or N only please...\n"
            continue


def eliminate_cases(turn, player_case, removed_cases, cases_dict):
    """eliminates and reveals cases selected by player on each round"""

    while turn != 0:
        case_to_remove = raw_input("Choose a case to remove: ")
        if case_to_remove.isdigit(): # ensures that the input is a number
            case_to_remove = int(case_to_remove)
        else:
            "\nChoose from the available boxes only\n"
            continue
        
        if case_to_remove == player_case:
            print "\nThis is the case you have selected\n"
            continue
        elif case_to_remove < 1 or case_to_remove > len(cases):
            print "\nChoose from the available boxes only\n"
            continue        
        elif case_to_remove in removed_cases:
            print "\nThis case has been removed.\n"
            continue        
        else:
            print "\n$ " + str(cases_dict[case_to_remove]) + " is out.\n"
            del cases_dict[case_to_remove] # deletes the value from the dictionary
            removed_cases.append(case_to_remove) # adds the removed case to a list
            turn = turn - 1
            show_cases(cases, removed_cases) # shows cases still in play at then end

def compute_banker_offer(cases_dict):
    """computes average of remaining boxes"""

    banker_offer = sum(cases_dict.values()) / len(cases_dict.values())
    banker_offer = round(banker_offer, 2)
    print "\nThe Banker wants to buy your case for $ " + str(banker_offer) + "."
    return banker_offer


def ask_deal_no_deal(banker_offer, player_case):
    """asks player to take banker's offer and end game, or reject 
    offer and continue"""

    while True:    
        decision = raw_input("\nDEAL OR NO DEAL \n\n> ")
        decision = decision.upper()
        if decision == "DEAL":
            print "YOU WON $ " + str(banker_offer) + "."
            open_player_case(selected_dict, player_case, banker_offer)
        elif decision == "NO DEAL":
            print "\nLet's proceed to the next round!\n"
            break
        else:
            "\nDEAL or NO DEAL only please."
            continue

def open_player_case(selected_dict, player_case, banker_offer):
    """opens player's case when player chooses DEAL"""

    print "\nTHE PRIZE IN YOUR CASE IS "
    print "$ " + str(selected_dict[player_case]) # prints the item in selected_case list
    if banker_offer < selected_dict.values():
        print "\nYOU GOT THE LOWER PRIZE, BUT NOT BAD.\n\n"
    elif banker_offer > selected_dict.values():
        print "\nCONGRATULATIONS! YOU GOT THE HIGHER PRIZE!\n\n"

    exit()

def swap_case(cases_dict, player_case, selected_dict, swapped_dict):
    """asks player whether he/she wants to swap the case with the remaining case"""

    # where remaining items to be swapped will be stored
    swap_dict = {}
    # accesses keys, values and stores in swap_dict
    for k, v in cases_dict.items():
        k
        v
        swap_dict[k] = v

    print "\nIf you want to swap cases, this is your chance.\n"
    print swap_dict.keys()
    print "\nYOUR ORIGINAL CASE: " + str(player_case)
    while True:
        swap = raw_input("\nCHOOSE YOUR WINNING CASE: ")
        if swap.isdigit(): # ensures that the input is a number
            swap = int(swap)
        else:
            "Choose between " + swap_dict.keys() + " only."
            continue
        
        if swap in swap_dict:
            if swap in selected_dict:
                print "\nYou chose your original case.\n"
                return swap

            else:
                swapped_dict[swap] = swap_dict[swap]
                print "\nYou went for the other case.\n"
                return swap
        
        else:
            print "\nChoose between " + swap_dict.keys() + " only.\n"


def final_round(cases_dict, selected_dict, swapped_dict, swap):
    """prints the prize won by player if player reaches the final round"""

    print "YOU WON...\n\n"
    print "$ " + str(cases_dict[swap]) + "\n\n"
    print "CONGRATULATIONS!"
    # if swap in selected_dict:
    #     if selected_dict[swap] < 
    #     print "\nYOU GOT THE LOWER PRIZE, BUT NOT BAD.\n\n"
    # else:
    #     print "\nCONGRATULATIONS! YOU GOT THE HIGHER PRIZE!\n\n"

    exit()


def main_flow():
    """main game"""
    print "\nWelcome to Deal or No Deal!\n"
    how_to_play()
    show_prizes(cases_dict)
    while True:
        show_cases(cases, removed_cases)
        player_case = raw_input("\nChoose YOUR WINNING CASE: ")
        if player_case.isdigit(): 
            player_case = int(player_case)
        else:
            print "\nChoose from the available boxes only\n"
            continue

        if player_case < 1 or player_case > len(cases):
            print "\nChoose from the available boxes only\n"
        
        else: 
            while True:
                sure = raw_input("\nAre you sure with your pick (Y/N)? ")
                sure = sure.lower()
            
                if sure == 'y':
##                  del cases_dict[player_case] --> # DO NOT DELETE PLAYER_CASE FROM DICT
##                  selected_case.append(player_case) # adds player case to selected_case
                    selected_dict[player_case] = cases_dict[player_case] # adds player's case to selected_dict
                    removed_cases.append(player_case) # adds player case to removed_cases
                    print "\nGreat! Let's try your luck and eliminate some cases!\n"

                    # ROUND 1
                    print "Let's open 4 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(4, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)      

                    # ROUND 2
                    print "Let's open 3 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(3, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 3
                    print "Let's open 2 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(2, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 4
                    print "Let's open 2 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(2, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 5
                    print "Let's open 1 case!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(1, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # FINAL ROUND
                    print "You only have one case left.\n\n"
                    show_cases(cases, removed_cases)
                    swap = swap_case(cases_dict, player_case, selected_dict, swapped_dict)
                    final_round(cases_dict, selected_dict, swapped_dict, swap)
                    # banker_offer = compute_banker_offer(cases_dict)
                    # show_prizes(cases_dict)
                    # ask_deal_no_deal(banker_offer)

                elif sure == 'n':
                    print "\nTake your time!\n"
                    break
            
                else:
                    print "\nY or N only please.\n"
                  

main_flow()