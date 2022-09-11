'''
Function for creating bricks and returns a list of values in main_pile
and an empty list for the discard pile.
'''
def setup_bricks():
    main_pile = [] # Creating an empty main pile list 
    discard = [] # Creating an empty discard list
    i = 0
    for x in range(1,61):
        i = x
        main_pile.append(i) # Appending values from 1 - 60 on the main pile.

    return main_pile, discard

'''
This function shuffles the values in the main pile list using the 
random.shuffle inbuilt function
'''
def shuffle_bricks(main_pile):
    import random
    random.shuffle(main_pile) # Using random.shuffle to shuffle the values in the list.
    # print(main_pile)

'''
Function for checking if the main pile list is empty.
If the main pile is empty, copy the items in the discard pile 
to the main pile and turn the first item on the list.
Else, if the main pile has items then turn th first item on the list.

'''
def check_bricks(main_pile, discard):
    # main_pile, discard = setup_bricks()
    m = len(main_pile) # Getting the length of the list.
    
    if m == 0: # If the main pile has no elements, shuffle the bricks on discard pile.
        shuffle_bricks(discard)
        main_pile = discard.copy() # Copy the values to the main pile.
        discard = discard.clear() # clear the discard list
        print("Filled main pile: ", main_pile)
        print("New discard pile: ", discard)
        print("top main pile card: ", main_pile[0])
    else:
        print("Top main pile card: ", main_pile[0])

'''
This function removes and returns the top brick from 
the top of any pile i.e. main, discard, human and computer piles.
IT IS USED AT THE START OF THE GAME TO DEAL BRICKS 
IT WILL ALSO BE USED DURING EACH PLAYER'S TURN TO TAKE THE TOP BRICK
FROM EITHER THE MAIN OR DISCARD PILE
RETURN INTEGER
'''
def get_top_brick(main_pile, discard, human_tower, computer_tower):
    # print("Enter m for main pile and d for discard")
    brick_pile = input("Enter m for main pile and d for discard to choose the brick pile to get the top brick: ").lower()

    if brick_pile == 'm':
        brick = main_pile[0]
        main_pile.pop(0)
    
    elif brick_pile == 'd':
        brick = discard[0]
        discard.pop(0)

    elif brick_pile == 'h':
        brick = human_tower[0]
        human_tower.pop(0)

    elif brick_pile == 'c':
        brick = computer_tower[0]
        computer_tower.pop(0)

    return brick


'''
This function creates the computer and human tower lists.
The lists are creted by slicing the main pile using two steps,
by starting with index 0 for the computer pile and index 1
for the human tower. Hence dealing the ten bricks in an alternating manner.
'''
def deal_initial_bricks(main_pile):
    computer_tower =[]
    human_tower = []
    computer_tower, human_tower = main_pile[0:20:2], main_pile[1:20:2]
    print(computer_tower, human_tower)
    
    del main_pile[0:20]
    # for i in range(0,20):
    #     main_pile.pop(i)
    # i = 0
    # while i <= 20:
    #     i = i + 1
    #     main_pile.pop(i)

    print("Main pile after deal:", main_pile)
    return computer_tower, human_tower


'''
A function that picks the popped brick and adds it to the discard pile. 
'''
def add_brick_to_discard(brick, discard):
    discard.append(brick)

'''

'''
def find_and_replace(new_brick, brick_to_be_replaced, computer_tower,human_tower, discard):
    tower = input("Enter h for human tower: ").lower() #and c for computer tower
    
    

    if tower == "c":

        while True:
            try:
                print("Computer Tower 1:",computer_tower)
                index_value = computer_tower.index(brick_to_be_replaced)
                # print("New brick: ", new_brick)
                discard.insert(0, brick_to_be_replaced)
                print("Top discard brick: ", discard[0])
                computer_tower.pop(index_value)
                computer_tower.insert(index_value, new_brick)
                break
            except ValueError:
                print("The value is not on the computer tower. Enter the value of brick to be replaced")
                break
    elif tower == "h":
        while True:
            try:
                print("Human tower 1: ", human_tower)
                index_value = human_tower.index(brick_to_be_replaced)
                # new_brick = human_tower[index]
                # print("New brick: ", new_brick)
                discard.insert(0, brick_to_be_replaced)
                # print("Top discard brick: ", discard[0])
                human_tower.pop(index_value)
                human_tower.insert(index_value, new_brick)
                break
            except ValueError:
                print("The value is not on the human tower. Enter the value of brick to be replaced")
                break

    return True  

'''
Computer play function: 
1. Create a strategy for the computer. Given the top from main pile and discard, choose whether to take or not. 
2. Given the current computer tower, either pick main pile or discard brick.
3. Evaluate the value of the brick. Order from smallest to largest
4. Do not make a random decision, incorrect decision i.e value less than 10 being at the bottom of the tower or cheat.
5. Return new computer tower.
'''
def computer_play(computer_tower, main_pile, discard):
    # print("Top brick on discard pile: ", discard[0])
    # take_turn = input("Play: 0/No play: 1")
    # if 

    if discard[0] > computer_tower[9]:
        # computer_tower.pop(computer_tower[9])
        computer_tower.insert(9, discard[0])
        discard.pop(0)
        discard.insert(0, computer_tower[10])
        computer_tower.pop(10)
        print("Top discard brick: ", discard[0])
        # print("comp new: ", computer_tower)

    else: #discard[0] < computer_tower[9]:
        if discard[0] > computer_tower[8]:
            # computer_tower.pop(computer_tower[8])
            # computer_tower.pop(9)
            computer_tower.insert(8, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[9])
            computer_tower.pop(9)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[7]:
            # computer_tower.pop(computer_tower[7])
            # computer_tower.pop(8)
            computer_tower.insert(7, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[8])
            computer_tower.pop(8)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[6]:
            # computer_tower.pop(computer_tower[6])
            # computer_tower.pop(7)
            computer_tower.insert(6, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[7])
            computer_tower.pop(7)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[5]:
            # computer_tower.pop(computer_tower[5])
            computer_tower.insert(5, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[6])
            computer_tower.pop(6)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[4]:
            # computer_tower.pop(computer_tower[4])
            computer_tower.insert(4, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[5])
            computer_tower.pop(5)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[3]:
            # computer_tower.pop(computer_tower[3])
            computer_tower.insert(3, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[4])
            computer_tower.pop(4)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[2]:
            # computer_tower.pop(computer_tower[2])
            computer_tower.insert(2, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[3])
            computer_tower.pop(3)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[1]:
            # computer_tower.pop(computer_tower[1])
            computer_tower.insert(1, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[2])
            computer_tower.pop(2)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        elif discard[0] > computer_tower[0]:
            # computer_tower.pop(computer_tower[1])
            computer_tower.insert(0, discard[0])
            discard.pop(0)
            discard.insert(0, computer_tower[1])
            computer_tower.pop(1)
            print("Top discard brick: ", discard[0])
            # print("comp new: ", computer_tower)

        else:
            if main_pile[0] > computer_tower[9]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(9, main_pile[0])
                discard.insert(0, computer_tower[10])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[10])
                computer_tower.pop(10)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[8]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(8, main_pile[0])
                discard.insert(0, computer_tower[9])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[9])
                computer_tower.pop(9)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[7]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(7, main_pile[0])
                discard.insert(0, computer_tower[8])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[8])
                computer_tower.pop(8)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[6]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(6, main_pile[0])
                discard.insert(0, computer_tower[7])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[7])
                computer_tower.pop(7)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[5]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(5, main_pile[0])
                discard.insert(0, computer_tower[6])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[6])
                computer_tower.pop(6)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[4]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(4, main_pile[0])
                discard.insert(0, computer_tower[5])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[5])
                computer_tower.pop(5)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[3]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(3, main_pile[0])
                discard.insert(0, computer_tower[4])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[4])
                computer_tower.pop(4)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[2]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(2, main_pile[0])
                discard.insert(0, computer_tower[3])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[3])
                computer_tower.pop(3)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[1]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(1, main_pile[0])
                discard.insert(0, computer_tower[2])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[2])
                computer_tower.pop(2)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            elif main_pile[0] > computer_tower[0]:
                # computer_tower.pop(computer_tower[9])
                computer_tower.insert(0, main_pile[0])
                discard.insert(0, computer_tower[1])
                main_pile.pop(0)
                # main_pile.insert(0, computer_tower[1])
                computer_tower.pop(1)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)

            else:
            
                # computer_tower.pop(computer_tower[1])
                computer_tower.insert(0, discard[0])
                discard.pop(0)
                discard.insert(0, computer_tower[1])
                computer_tower.pop(1)
                print("Top discard brick: ", discard[0])
                # print("comp new: ", computer_tower)


    return computer_tower
'''
Main part of the function.
'''
def main():
    import random
    main_pile, discard = setup_bricks()
    
    print("Main pile: ", main_pile)
    print("Discard pile: ", discard)

    shuffle_bricks(main_pile)
    print("Shuffled pile: ", main_pile)

    check_bricks(main_pile, discard)

    computer_tower, human_tower = deal_initial_bricks(main_pile)

    print("Computer tower: ", computer_tower)
    print("Human tower: ", human_tower)
    
    # print("Enter m - main pile, d - discard pile, h - human tower, c - computer tower")
    # brick_pile = input("Choose the brick pile to get top brick: ").lower()
    
    brick = get_top_brick(main_pile, discard, human_tower, computer_tower)
    print("Top brick:", brick)

    # discard.append(brick)
    add_brick_to_discard(brick, discard)
    print("New discard", discard)

    flag = 0
    flag_2 = 0
    while True:
        try:
            brick = get_top_brick(main_pile, discard, human_tower, computer_tower)
            print("Top brick:", brick)
            brick_to_be_replaced = int(input("Enter the value of the brick to be replaced: "))
            find_and_replace(brick, brick_to_be_replaced, computer_tower, human_tower, discard)
            #print("ADDED TO DISCARD: ",discard)
            print("Added HUMAN Tower:", human_tower)

            # flag = 0
            if(all(human_tower[i] <= human_tower[i + 1] for i in range(len(human_tower) - 1))):
                flag = 1
            # Checking if tower blaster
            if (flag):
                print("Yes: Human Tower Blaster")
                break  
            else:
                print("Player: Keep on going")
                
            computer_play(computer_tower, main_pile, discard)
            # print("Computer tower 2",computer_tower)
            if(all(computer_tower[i] <= computer_tower[i + 1] for i in range(len(computer_tower) - 1))):
                flag_2 = 1
            # Checking if tower blaster
            if (flag_2):
                print("Yes: Computer Tower Blaster")
                break  
            else:
                print("Computer: Keep on going")
        except:
            if(all(computer_tower[i] <= computer_tower[i + 1] for i in range(len(computer_tower) - 1))):
                flag_2 = 1
            # Checking if tower blaster
            if (flag_2):
                print("Yes: Computer Tower Blaster")
    # while True:
    #     computer_play(computer_tower, main_pile, discard)
    #     print("Computer tower 2",computer_tower)
    #     # flag_2 = 0
    #     if(all(computer_tower[i] <= computer_tower[i + 1] for i in range(len(computer_tower) - 1))):
    #         flag_2 = 1
    #     # Checking if tower blaster
    #     if (flag_2):
    #         print("Yes: Computer Tower Blaster")  
    #     else:
    #         print("No: Keep on going") 
    # tower = input("Enter h for human tower and c for computer tower: ").lower()
    # brick_to_be_replaced = int(input("Enter the value of the brick to be replaced: "))
    

    # computer_play(computer_tower, main_pile, discard)
    # print("Computer tower 2",computer_tower)

    # # Using all() to check sorted list
    # flag = 0
    # if(all(human_tower[i] <= human_tower[i + 1] for i in range(len(human_tower) - 1))):
    #     flag = 1
    # # Checking if tower blaster
    # if (flag):
    #     print("Yes: Human Tower Blaster")  
    # else:
    #     print("No: Keep on going")

    # # Using all() to check sorted list
    # flag_2 = 0
    # if(all(computer_tower[i] <= computer_tower[i + 1] for i in range(len(computer_tower) - 1))):
    #     flag_2 = 1
    # # Checking if tower blaster
    # if (flag_2):
    #     print("Yes: Computer Tower Blaster")  
    # else:
    #     print("No: Keep on going") 



if __name__ == "__main__":
        main()
