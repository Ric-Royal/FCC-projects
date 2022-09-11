'''
Name: Richard Kabiru Waithera
Strathmore student ID: 150684
Reference sources: https://realpython.com/python-main-function/
                    https://www.w3schools.com/python/python_functions.asp
I worked alone with assistance from open source learning materials.

'''
import random

# Function for printing out rules
def print_rules():
    '''
    The function welcomes the players by printing a welcome statement and the rules.
    the function returns the welcome statement.
    '''
    welcome = print("Hello players, Welcome to Dice-Life:\n Rules\n 1. The game can be played by more than 1 player.\n 2. The players are allowed to roll the die as much as they want. \n 3. If the rolled die lands on any number between 1 and 5 inclusive, you earn the points and are allowed to roll the die again. \n 4. If the rolled die lands on six, you get zero points no matter the points you had gained in previous rolls and the next player is allowed to roll the die. \n\n The game starts now.")
    return welcome

# Function for entering the number of players and their names
# Assigning variables to the individual players remaining
def no_of_players():
    '''
    This function asks the user to input the number of players and their names.
    It returns the names of the players.
    '''
    players_no = int(input("Enter the number of players:"))
    player = []
    plyrs_no_initial = 1
    while plyrs_no_initial <= players_no:
        player_name = input("Player name:")
        player.append(player_name)   
        name = print("Player",plyrs_no_initial, "is",player_name)
        plyrs_no_initial = plyrs_no_initial + 1
        
        continue
    
    print(player)
    return name

# function for rolling the die. Genrates random numbers between 1 and 6
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
                print("roll again")            
                continue
            elif roll_consent[0] == "Y":
                print("roll again")
                continue
            elif roll_consent[0] == "n":
                print("Next player roll the dice")
                break
            elif roll_consent[0] == "N":
                print("Next player roll the dice")
                break    
        except:
            print("Please input y/Y for yes and N/n for no")
            continue
    return roll_consent

# computer move
def comp_move(): 
    '''
    This function provides for the computer move. 
    The roll_option function is called to initiate the rolling of the die.
    If the roll is equiavelent to 6 a score of zero is given.
    If the roll is less than or equal to 5, the value is added to an array.
    The functions returns the total of the values in the array.
    '''
    roll_option()
    comp_score = [0]
    if roll() == 6:
        score = 0
        comp_score.append(score)
        print("The computer score is:", comp_score)
        print("next player")
        
    elif roll() <= 5:
        comp_score.append(roll())
        print("The computer score is:", comp_score)

    comp_total = 0
    for i in comp_score:
        comp_total += i
        print("The computer total is",comp_total)    
    return comp_total

# Human move
def human_move():
    '''
    This function provides for the human move. 
    The roll_option function is called to initiate the rolling of the die.
    If the roll is equiavelent to 6 a score of zero is given.
    If the roll is less than or equal to 5, the value is added to an array.
    The functions returns the total of the values in the array.
    '''
    roll_option()
    hum_score = [0]
   
    if roll() == 6:
        no_score = 0
        hum_score.append(no_score)
        print("The human score is", hum_score)
        

    elif roll() <= 5:
        hum_score.append(roll())
        print("The human score is", hum_score)
    
    
    hum_total = 0
    for i in hum_score:
        hum_total += i
        print("The human total is",hum_total)
    return hum_total

# Checking the current game status
def current_game_status():
    '''
    This function checks the current game status. 
    It checks whether the computer or player hass higher points
    and returns the point difference.
    '''
    hum_total = human_move()
    comp_total = comp_move()
    print("Human score: "+str(hum_total), "\nComputer score: " +str(comp_total))
    if comp_total > hum_total:
        point_diff = comp_total - hum_total
        print("You are ", point_diff, "ahead of human")
    
    elif comp_total < hum_total:
        point_diff = hum_total - comp_total
        print("You are ", point_diff, "ahead of computer")

    else:
        print("Its a tie")

    return point_diff

# Function to declare the winner
def show_final_result(comp_total, hum_total):
    '''
    This function takes in the total of the 
    computer and the player and checks if they 
    are greater than 50. If true the game ends
    '''
    if comp_total > 50 and hum_total <= 50:
        print("Computer has won")

    elif hum_total > 50 and comp_total <= 50:

        print("Human has won")


def main():
    with open("template_behavior_{dice}.txt", "a") as f:
        # Variables
        trigger = 6
        run = True
        # Welcome players and inform them of the rules
        welcome = print_rules()
        print(welcome, file = f)

        # Printing out the names of the players
        player = no_of_players()
        print(player, file = f)
        while run:
            # Calling Computer move function
            computer_move = comp_move()
            print("This is the computer score",computer_move, file = f)

            # Calling human move function
            hum_move = human_move()
            print("This is the human score",hum_move, file = f)

            # Checking if the game is over
            show_current = current_game_status()
            print(show_current, file = f)

        else:
            run = False
            print("Score", show_final_result(), file = f)

if __name__ == "__main__":
    main()