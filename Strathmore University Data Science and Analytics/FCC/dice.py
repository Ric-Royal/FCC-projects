import random

# Function for printing out rules
def print_rules():
    welcome = print("Hello players, Welcome to Dice-Life:\n Rules\n 1. The game can be played by more than 1 player.\n 2. The players are allowed to roll the die as much as they want. \n 3. If the rolled die lands on any number between 1 and 5 inclusive, you earn the points and are allowed to roll the die again. \n 4. If the rolled die lands on six, you get zero points no matter the points you had gained in previous rolls and the next player is allowed to roll the die. \n\n The game starts now.")
    return welcome

# Welcome players and inform them of the rules
welcome = print_rules()

print(welcome)

# Input the number of players
# no_of_players = int(input("Enter the number of players:"))

# Function for entering the number of players and their names
# Assigning variables to the individual players remaining
def no_of_players():
    players_no = int(input("Enter the number of players:"))
    
    plyrs_no_initial = 1
    while plyrs_no_initial <= players_no:
        player_name = input("Player name:")   
        name = print("Player",plyrs_no_initial, "is",player_name)
        plyrs_no_initial = plyrs_no_initial + 1
        
        continue
        plyrs_no_initial[0] = player_name
    return name

# Printing out the names of the players
player = no_of_players()
print(player)

# function for rolling the die. Genrates random numbers between 1 and 6
def roll():
    die_roll = random.randint(1,6)
    return die_roll


# Ask user if they want to roll  again
def roll_option():
    while True:
        try:
            
            print("Do you want to roll again?")
            roll_consent = input("Enter Y/y for yes and n/N for no:")
            if roll_consent[0] == "y":
                print("roll again")
                roll()
                nb_trials = 10000
                random_list = []
                for i in range(nb_trials):
                    n = roll()
                    if roll() <= 5:
                        random_list.append(n)
                        print(random_list)
                        continue
                    else:
                        random_list.append(n)
                        break
                # nb_trials = 10000

                # for i in range(nb_trials):
                #     sum_value = 0
                #     if roll() < 6:
                #         sum_value += roll()
                #         print("Your total is:", sum_value)
                #         continue
                #     else:
                #         sum_value = sum_value
                #         print("Your total is:", sum_value)
                #         break
                # nb_trials = 10000
                # tot = 0

                # for i in range(nb_trials):
                #     sum_value = 0
                #     roll() < 6
                #     while roll():
                #         a = random.randint(1,6)
                #         if a >=1:
                #             roll() == 6
                #         sum_value += a
                #     tot += sum_value 
                # print(tot)
                continue
            elif roll_consent[0] == "Y":
                print("roll again")
                roll()
                continue
            elif roll_consent[0] == "n":
                print("Next player roll the dice")
                break
            elif roll_consent[0] == "N":
                print("Next player roll the dice")
                break    
            #else:
                #print("Next player roll the dice")
        except:
            print("Please input y/Y for yes and N/n for no")
            continue
    return roll_consent

roll_cons = roll_option()
print(roll_cons)
# # computer move
# def comp_move(): #comp_score, hum_score
#     comp_score = 0
#     while roll() == 6:
#         print("You get 0 points\n Next player")
#         #comp_score = 0
#         comp_score = comp_score + roll()
#         print("Computer score:", comp_score)
#         break
#     else : #0 < roll() < 6
#         #comp_score = 0
#         comp_score = comp_score + roll()
#         roll_option()
#         print("Computer score:", comp_score)
#     # else:
#     #     #hum_score = 0
#     #     print("Computer score:", comp_score)
#     #     #print("Human score:", hum_score)
#     return comp_score #, hum_score

# computer_move = comp_move()
# print(computer_move)  


