# Deal or No Deal (Modified w/ only 14 cases)
# Python 2.7.13
# Hackbright Prep Project, May 2017
# by Kathleen Domingo

import os # needed for function to clear screen
import random # needed for function to randomize prize values

# set randomized prize values
prizes = random.sample([.01, 5, 25, 75, 200, 400, 750, 1000, 10000, 50000, 100000, 300000, 500000, 1000000], 14)

# set case values
cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# where cases and prizes will be stored
cases_dict = {}

# used to access and assign the indexes of prizes and cases to 'i'
for i in range(len(cases)): 
    cases_dict[cases[i]] = prizes[i] # adds keys and values to cases_dict

# list where eliminated cases will be stored
removed_cases = []

# dictionary where player's initial choice will be stored
selected_dict = {}

# dictionary where the player's choice on the final round will be stored
final_dict = {}

def show_cases(cases, removed_cases):
    """displays cases still in play, and crosses out the selected and
    eliminated cases"""

    print "Available CASES: "
    for case in cases:
        if case in removed_cases:
            print "x",
        else:
            print case,

    print "\n"

def show_prizes(cases_dict):
    """displays available prizes in ascending order"""

    print "\nAmounts still in play:\n "
    available_prizes = cases_dict.values()
    for prize in sorted(available_prizes):
        print "$ " + str(prize)

    print "\n"


def how_to_play():
    """asks player if familiar with the game and if not, prints game directions"""

    while True:
        instructions = raw_input("Are you familiar with the game (Y/N)? ")
        instructions = instructions.lower()
        
        if instructions == 'y':
            print "\nCool! Let's Play!\n"
            enter = raw_input("\nPress ENTER to continue.")
            clear_screen = os.system("clear") # clears the screen
            break
        
        elif instructions == 'n':
            print "\nThe mission is to win the $1M or the higher amount between the banker's offer and your selected case.\n\n"
            print "Player selects 1 out of 14 cases with varying amounts of virtual cash - ranging from $.01 to $1M.\n\n"
            print "Each round, the player eliminates cases to reveal the amounts not chosen.\n\n"
            print """The "Banker" then offers to buy the player's case for a certain amount at the end of each round.\n\n"""
            print 'The player can accept the offer and end the game by saying "DEAL" or reject it and continue the game by saying "NO DEAL".\n\n'      
            print "Now, let's play!\n\n"

            enter = raw_input("\nPress ENTER to continue.")
            clear_screen = os.system("clear") # clears the screen
            break
        
        else:
            print "\nY or N only please...\n"


def eliminate_cases(turn, player_case, removed_cases, cases_dict):
    """eliminates and reveals cases selected by player one at a time,
    then ends with the Banker's "call" """

    while turn != 0:
        case_to_remove = raw_input("Choose a case to remove: ")
        if case_to_remove.isdigit(): # ensures that the input is a number
            case_to_remove = int(case_to_remove)
        else:
            "\nChoose from the available cases only\n"
            continue # skips the conditions below and loops over from the start
        
        if case_to_remove == player_case:
            print "\nThis is the case you have selected\n"
        elif case_to_remove < 1 or case_to_remove > len(cases):
            print "\nChoose from the available cases only\n"    
        elif case_to_remove in removed_cases:
            print "\nThis case has been removed.\n"     
        else:
            print "\n$ " + str(cases_dict[case_to_remove]) + " is out.\n"
            del cases_dict[case_to_remove] # deletes the value from the dictionary
            removed_cases.append(case_to_remove) # adds the removed case to removed_cases list
            turn = turn - 1
            show_cases(cases, removed_cases) # shows cases still in play at the end
    enter = raw_input("\nThe Banker just called and wants to give you an offer... Press ENTER.")
    clear_screen = os.system("clear") # clears the screen

def compute_banker_offer(cases_dict):
    """computes average of remaining boxes and prints out the amount"""

    banker_offer = sum(cases_dict.values()) / len(cases_dict.values())
    banker_offer = round(banker_offer, 2) # rounds off to two decimal places
    print "\nThe Banker wants to buy your case for $ " + str(banker_offer) + "."
    return banker_offer


def ask_deal_no_deal(banker_offer, player_case):
    """asks player to take banker's offer and end game, or reject 
    offer and continue"""

    while True:    
        decision = raw_input("\nDEAL OR NO DEAL \n\n> ")
        decision = decision.upper()
        if decision == "DEAL":
            print "\nYOU WON $ " + str(banker_offer) + "."
            enter = raw_input("\n")
            open_player_case(selected_dict, player_case, banker_offer)
        elif decision == "NO DEAL":
            print "\nLet's proceed to the next round!\n"
            enter = raw_input("\nPress ENTER to continue.")
            clear_screen = os.system("clear") # clears the screen
            break
        else:
            "\nDEAL or NO DEAL only please."

def open_player_case(selected_dict, player_case, banker_offer):
    """opens player's case when player chooses DEAL"""

    #clear_screen = os.system("clear") # clears the screen
    print "\nTHE PRIZE IN YOUR CASE IS $ " + str(selected_dict[player_case]) # prints the item in selected_case list
    if banker_offer < selected_dict[player_case]:
        print "\n\nYOU GOT THE LOWER PRIZE, BUT NOT BAD.\n\n"
    elif banker_offer > selected_dict[player_case]:
        print "\n\nCONGRATULATIONS! YOU GOT THE HIGHER PRIZE!\n\n"

    exit()

def swap_case(cases_dict, player_case, selected_dict, final_dict):
    """gives player the option to swap the initially chosen case with the remaining case"""

    swap_dict = {} # where remaining items to be swapped will be stored
        
    for k, v in cases_dict.items(): # accesses remaining keys & values in cases_dict
        swap_dict[k] = v # stores in swap_dict

    print "\nIf you want to swap cases, this is your chance.\n"
    
    print "\nYOUR ORIGINAL CASE: " + str(player_case)
    print "\n"

    while True:

        swap = raw_input("CHOOSE YOUR WINNING CASE: ")
        if swap.isdigit(): # ensures that the input is a number
            swap = int(swap) # converts input into an integer
        else:
            print "\nChoose between the following boxes only:"
            print swap_dict.keys()
            print "\n"
            continue
        
        if swap in swap_dict: # 
            if swap in selected_dict: # if the case chosen is the original choice
                final_dict[swap] = cases_dict[swap] # adds the selected case in final_dict
                del cases_dict[swap] # deletes the selected case from cases_dict
                # there must only be one key-value pair left in cases_dict at this point
                # which is the unchosen case
                print "\nYou chose your original case.\n"
                enter = raw_input("\nPress ENTER to continue.")
                clear_screen = os.system("clear") # clears the screen
                #return swap

            else:
                final_dict[swap] = cases_dict[swap]
                del cases_dict[swap] # deletes the selected case from cases_dict
                # there must only be one key-value pair left in cases_dict at this point
                # which is the unchosen case
                print "\nYou went for the other case.\n"
                enter = raw_input("\nPress ENTER to continue.")
                clear_screen = os.system("clear") # clears the screen
            
            return swap
        
        else:
            print "\nChoose between the following boxes only:"
            print swap_dict.keys()
            print "\n"


def final_round(cases_dict, selected_dict, final_dict, swap):
    """prints the prize won by player if player reaches the final round"""

    print "YOU WON...\n\n"
    enter = raw_input("\n...\n")
    enter = raw_input("\n...\n")
    print "\n$ " + str(final_dict[swap]) + "\n\n"
    
    for i in cases_dict:
        if final_dict[swap] < cases_dict[i]:
            print "\nYOU GOT THE LOWER PRIZE, BUT NOT BAD.\n\n"
        else:
            print "\nCONGRATULATIONS! YOU GOT THE HIGHER PRIZE!\n\n"

    exit()


def main_flow():
    """where the main flow of the game is stored"""

    print "\nWelcome to Deal or No Deal!\n"

    how_to_play()
    show_prizes(cases_dict)

    while True:
        show_cases(cases, removed_cases)
        player_case = raw_input("\nChoose YOUR WINNING CASE: ")
        if player_case.isdigit(): 
            player_case = int(player_case)
        else:
            print "\nChoose from the available cases only\n"
            continue

        if player_case < 1 or player_case > len(cases):
            print "\nChoose from the available cases only\n"
        
        else: 
            while True:
                sure = raw_input("\nAre you sure with your pick (Y/N)? ")
                sure = sure.lower()
            
                if sure == 'y':
                    selected_dict[player_case] = cases_dict[player_case] # adds player's case to selected_dict
                    removed_cases.append(player_case) # adds player case to removed_cases
                    clear_screen = os.system("clear") # clears the screen
                    print "\nGreat! Let's try your luck and eliminate some cases!\n\n"

                    # ROUND 1
                    print "Let's open 4!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(4, player_case, removed_cases, cases_dict)
                    banker_offer = compute_banker_offer(cases_dict) # to use as reference for ask_deal_no_deal()
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)      

                    # ROUND 2
                    print "Let's open 3 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(3, player_case, removed_cases, cases_dict)
                    compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 3
                    print "Let's open 2 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(2, player_case, removed_cases, cases_dict)
                    compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 4
                    print "Let's open 2 cases!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(2, player_case, removed_cases, cases_dict)
                    compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # ROUND 5
                    print "Let's open 1 case!\n\n"
                    show_cases(cases, removed_cases)
                    eliminate_cases(1, player_case, removed_cases, cases_dict)
                    compute_banker_offer(cases_dict)
                    show_prizes(cases_dict)
                    ask_deal_no_deal(banker_offer, player_case)

                    # FINAL ROUND
                    print "You only have one case left.\n\n"
                    show_cases(cases, removed_cases)
                    swap = swap_case(cases_dict, player_case, selected_dict, final_dict)
                    final_round(cases_dict, selected_dict, final_dict, swap)

                elif sure == 'n':
                    print "\nTake your time!\n"
                    break
            
                else:
                    print "\nY or N only please.\n"
                  

main_flow() # calls the main function