import random

def sum_of_list(hum_score):
    total = 0
    for val in hum_score:
        total = total + val
    return total
# function for rolling the die. Genrates random numbers between 1 and 6
def no_of_players():
        '''
        This function asks the user to input the number of players and their names.
        It returns the names of the players.
        '''
        players_no = int(input("Enter the number of players:"))
        players = []
        plyrs_no_initial = 1
        while plyrs_no_initial <= players_no:
            player_name = input("Player name:")
            players.append(player_name)   
            name = print("Player",plyrs_no_initial, "is",player_name)
            plyrs_no_initial = plyrs_no_initial + 1
            
            continue
        
        print(players)
        return players_no #name,

def roll():
    '''
    This function rolls the die. A random value is generated and assigned to die_roll.
    The function returns the value of the die roll.
    '''
    die_roll = random.randint(1,6)
    return die_roll
    
# Ask user if they want to roll  again
def roll_option():
    '''
    This function provides consent for rolling the die.
    If the user enters a value starting with y, the die is rolled.
    If the user enters a value starting with n, the die is not rolled.
    It returns the roll consent.
    '''
    while True:
        try:
            
            print("Do you want to roll again?")
            roll_consent = input("Enter Y/y for yes and n/N for no:")
            # First value of string roll consent is y
            if roll_consent[0] == "y":
                print("roll again 1")            
                continue
            elif roll_consent[0] == "Y":
                print("roll again 2")
                continue
            elif roll_consent[0] == "n":
                print("Next player roll the dice 1")
                break
            elif roll_consent[0] == "N":
                print("Next player roll the dice 2")
                break    
        except:
            print("Please input y/Y for yes and N/n for no")
            continue
    return roll_consent
# Human move
def human_move():#players_no):
    '''
    This function provides for the human move. 
    The roll_option function is called to initiate the rolling of the die.
    If the roll is equiavelent to 6 a score of zero is given.
    If the roll is less than or equal to 5, the value is added to an array.
    The functions returns the total of the values in the array.
    '''
    print("HUMAN MOVE")
    roll_option()
    #score = [0]#*players_no
    #roll = roll()
    rolls = []
    while True:
        if roll() == 6:
            no_score = 0
            rolls.append(no_score)
            break
        else:
            rolls.append(roll())
        print(rolls)

    else:
        print("next")

    # rolls = []
    # for i in range(0, no_of_players()):
    #     rolls.append(roll())
    
    # for i in range(len(rolls)):
    #    score[i] = sum(rolls[i])
        
    # return rolls, score
    # hum_score = [0]
    
    # hum_total = 0
    # for i in hum_score:
    #     if roll() == 6:
    #         no_score = 0
    #         hum_score.append(no_score)
    #         print("The human score is", hum_score, file= f )
    #         hum_total += i
    #         print("The human total is",hum_total, file= f)

    #     elif roll() <= 5:
    #         hum_score.append(roll())
    #         print("The human score is", hum_score, file= f)
    #         hum_total += i
    #         print("The human total is",hum_total, file= f)
    #         # hum_total = 0
    #         # for i in hum_score:
    #         #     hum_total += i
    #         #     print("The human total is",hum_total)
    # return hum_total

# hum = human_move()
# sum_of_list(hum)

def main():
        #with open("template_behavior_{dice}.txt", "a") as f:
            # Variables
            # trigger = 6
            run = True
            # # Welcome players and inform them of the rules
            # welcome = print_rules()
            # print(welcome, file = f)

            # Printing out the names of the players
            players_no = no_of_players()
            #players = no_of_players()
            print(players_no)
            while run:
                # # Calling Computer move function
                # computer_move = comp_move()
                # print("This is the computer score",computer_move, file = f)

                # Calling human move function
                hum_move = human_move()#players_no)
                hmn = sum_of_list(hum_move)
                print("This is the human score",hmn)

                # # Checking if the game is over
                # show_current = current_game_status()
                # print("Current score",show_current, file = f)

            else:
                run = False
                print("Final Score", human_move())

if __name__ == "__main__":
        main()