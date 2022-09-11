'''
Student Name: Richard Kabiru
Student Number: 150684
Statement of work: I worked alone with assistance from open source learning materials as listed below
    https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm 
    https://realpython.com/python-rock-paper-scissors/
    https://docs.python.org/3/library/collections.html#collections.deque
    https://realpython.com/python-append/#:~:text=append()%20will%20place%20new%20items%20in%20the%20available%20space.&text=Lists%20are%20sequences%20that%20can,finally%20a%20floating%2Dpoint%20number.
    https://appdividend.com/2022/05/30/how-to-find-element-in-list-in-python/#:~:text=To%20find%20an%20element%20in%20the%20list%2C%20use%20the%20Python,list%20and%20returns%20its%20position.
    https://www.simplilearn.com/tutorials/python-tutorial/global-variable-in-python
    https://www.simplilearn.com/tutorials/python-tutorial/pop-in-python#:~:text=List%20pop%20in%20Python%20is,last%20element%20of%20the%20list.
    https://stackoverflow.com/questions/59348027/splitting-a-list-into-2-lists-by-alternating-the-elements
    https://www.studytonight.com/post/how-to-copy-elements-from-one-list-to-another-in-python
    https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
    https://www.tutorialspoint.com/python/tuple_tuple.htm
    https://www.tutorialspoint.com/python/python_tuples.htm
'''
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
    

'''
Function for checking if the main pile list is empty.
If the main pile is empty, copy the items in the discard pile 
to the main pile and turn the first item on the list.
Else, if the main pile has items then turn th first item on the list.

'''
def check_bricks(main_pile, discard):
    m = len(main_pile) # Getting the length of the list.
    
    if m == 0: # If the main pile has no elements, shuffle the bricks on discard pile.
        shuffle_bricks(discard)
        main_pile = discard.copy() # Copy the values to the main pile.
        discard = discard.clear() # clear the discard list
        print("Filled main pile: ", main_pile)
        print("New discard pile: ", discard)
        print("top main pile card: ", main_pile[0])
    else: # If the main pile is not empty print the to main pile brick
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
    # User input for the brick pile that the user wants to remove the top brick. The input is converted to lower case
    brick_pile = input("Enter m for main pile and d for discard to choose the brick pile to get the top brick: ").lower()

    if brick_pile == 'm': # Main pile
        brick = main_pile[0] # Assign the value of the main pile to brick
        main_pile.pop(0) # Remove the top brick
    
    elif brick_pile == 'd': # Discard pile
        brick = discard[0] # Assign the value of the discard pile to brick
        discard.pop(0) # Remove the top brick

    elif brick_pile == 'h': # Human pile
        brick = human_tower[0] # Assign the value of the human pile to brick
        human_tower.pop(0) # Remove the top brick

    elif brick_pile == 'c': # Computer pile
        brick = computer_tower[0] # Assign the value of the computer pile to brick
        computer_tower.pop(0) # Remove the top brick

    return brick


'''
This function creates the computer and human tower lists.
The lists are creted by slicing the main pile using two steps,
by starting with index 0 for the computer pile and index 1
for the human tower. Hence dealing the ten bricks in an alternating manner.
'''
def deal_initial_bricks(main_pile):
    computer_tower =[] # Create a list for computer tower
    human_tower = [] # Create an empty list for the human tower
    computer_tower, human_tower = main_pile[0:20:2], main_pile[1:20:2] # Fill the computer tower and human tower using range values with 1 and 2 steps to alternate values.
    print(computer_tower, human_tower) 
    
    del main_pile[0:20] # Delete the values in the main pile from index 0 to 20
    print("Main pile after deal:", main_pile)

    return computer_tower, human_tower


'''
A function that picks the popped brick and adds it to the discard pile. 
'''
def add_brick_to_discard(brick, discard):
    discard.append(brick) # Appending the brick to discard pile


'''
This function finds a brick on a list and replaces the brick with a new brick.
'''
def find_and_replace(new_brick, brick_to_be_replaced, computer_tower,human_tower, discard):
    tower = input("Enter h for human tower: ").lower() # Input the value to choose the tower of interest
    
    

    if tower == "c":

        while True:
            try:
                print("Computer Tower:",computer_tower)
                index_value = computer_tower.index(brick_to_be_replaced) # Getting the index of the brick to be replaced
                discard.insert(0, brick_to_be_replaced) # Inserting the brick to be raplaced at index 0 in discard pile
                computer_tower.pop(index_value) # Removing the brick to be replaced from the computer pile
                computer_tower.insert(index_value, new_brick) # Inserting the new brick at the position of the removed brick to be replaced 
                break
            except ValueError:
                print("The value is not on the computer tower. Enter the value of brick to be replaced")
                break
    elif tower == "h":
        while True:
            try:
                print("Human tower 1: ", human_tower)
                index_value = human_tower.index(brick_to_be_replaced) # Getting the index value of the brick to be replaced in the human tower
                discard.insert(0, brick_to_be_replaced) # Inserting the brick to be replaced in the discard pile at index 0
                human_tower.pop(index_value) # Removing the brick at the index value of the brick to be replaced from the human tower
                human_tower.insert(index_value, new_brick) # Inserting the new brick at the position of the removed brick to be replaced
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
    # The computer will first check if the value at the end of its list is less than the value on the discard pile at index 0
    if discard[0] > computer_tower[9]:
        # Insert the value of the top brick on discard pile to computer tower at index 9
        computer_tower.insert(9, discard[0])
        discard.pop(0) # Remove the first element in discard pile
        discard.insert(0, computer_tower[10]) # Insert the 11th element on computer tower into the discard pile
        computer_tower.pop(10) # Remove the eleventh item on the computer list at index 10
        print("Top discard brick: ", discard[0])
        
    else: 
        if discard[0] > computer_tower[8]:
            # Repeat the same process for the next item on the computer tower list, if the top brick 
            # on discard pile is greater than value at index 8.
            computer_tower.insert(8, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 8
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[9]) # Insert the 10th element on computer tower into the discard pile
            computer_tower.pop(9) # Remove the tenth item on the computer list at index 9
            print("Top discard brick: ", discard[0])
           
        elif discard[0] > computer_tower[7]:
            computer_tower.insert(7, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 7
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[8]) # Insert the 9th element on computer tower into the discard pile
            computer_tower.pop(8) # Remove the nineth item on the computer list at index 8
            print("Top discard brick: ", discard[0])
            
        elif discard[0] > computer_tower[6]:
            computer_tower.insert(6, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 6
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[7]) # Insert the 8th element on computer tower into the discard pile
            computer_tower.pop(7) # Remove the eigth item on the computer list at index 7
            print("Top discard brick: ", discard[0])
            
        elif discard[0] > computer_tower[5]:
            computer_tower.insert(5, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 5
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[6]) # Insert the 7th element on computer tower into the discard pile
            computer_tower.pop(6) # Remove the seventh item on the computer list at index 6
            print("Top discard brick: ", discard[0])
    
        elif discard[0] > computer_tower[4]:
            computer_tower.insert(4, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 4
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[5]) # Insert the 6th element on computer tower into the discard pile
            computer_tower.pop(5) # Remove the sixth item on the computer list at index 5
            print("Top discard brick: ", discard[0])
            
        elif discard[0] > computer_tower[3]:
            computer_tower.insert(3, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 3
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[4]) # Insert the 5th element on computer tower into the discard pile
            computer_tower.pop(4) # Remove the fifth item on the computer list at index 4
            print("Top discard brick: ", discard[0])

        elif discard[0] > computer_tower[2]:
            computer_tower.insert(2, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 2
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[3]) # Insert the 4th element on computer tower into the discard pile
            computer_tower.pop(3) # Remove the fourth item on the computer list at index 3
            print("Top discard brick: ", discard[0])
    
        elif discard[0] > computer_tower[1]:
            computer_tower.insert(1, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 1
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[2]) # Insert the 3rd element on computer tower into the discard pile
            computer_tower.pop(2) # Remove the third item on the computer list at index 2
            print("Top discard brick: ", discard[0])

        elif discard[0] > computer_tower[0]:
            computer_tower.insert(0, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 0
            discard.pop(0) # Remove the first element in discard pile
            discard.insert(0, computer_tower[1]) # Insert the 2nd element on computer tower into the discard pile
            computer_tower.pop(1) # Remove the second item on the computer list at index 1
            print("Top discard brick: ", discard[0])

        # After comparing the value of the discard pile and all the conditions are not met, 
        # proceed to chose from the main pile by comparing the top brick main pile with all the elements on the list 
        # until the conditions are satisfied.
        else:
            if main_pile[0] > computer_tower[9]:
                computer_tower.insert(9, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 9
                discard.insert(0, computer_tower[10]) # Insert the eleventh item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(10) # Remove the eleventh item on the computer list at index 10
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[8]:
                computer_tower.insert(8, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 8
                discard.insert(0, computer_tower[9]) # Insert the tenth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(9) # Remove the tenth item on the computer list at index 9
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[7]:
                computer_tower.insert(7, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 7
                discard.insert(0, computer_tower[8]) # Insert the nineth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(8) # Remove the nineth item on the computer list at index 8
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[6]:
                computer_tower.insert(6, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 6
                discard.insert(0, computer_tower[7]) # Insert the eighth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(7) # Remove the eighth item on the computer list at index 7
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[5]:
                computer_tower.insert(5, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 5
                discard.insert(0, computer_tower[6]) # Insert the seventh item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(6) # Remove the seventh item on the computer list at index 6
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[4]:
                computer_tower.insert(4, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 4
                discard.insert(0, computer_tower[5]) # Insert the sixth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(5) # Remove the sixth item on the computer list at index 5
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[3]:
                computer_tower.insert(3, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 3
                discard.insert(0, computer_tower[4]) # Insert the fifth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(4) # Remove the fifth item on the computer list at index 4
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[2]:
                computer_tower.insert(2, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 2
                discard.insert(0, computer_tower[3]) # Insert the fourth item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(3) # Remove the fourth item on the computer list at index 3
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[1]:
                computer_tower.insert(1, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 1
                discard.insert(0, computer_tower[2]) # Insert the third item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(2) # Remove the third item on the computer list at index 2
                print("Top discard brick: ", discard[0])

            elif main_pile[0] > computer_tower[0]:
                computer_tower.insert(0, main_pile[0]) # Insert the value of the top brick on main pile to computer tower at index 0
                discard.insert(0, computer_tower[1]) # Insert the second item on the computer tower to discard pile at index 0
                main_pile.pop(0) # Remove the first element in main pile
                computer_tower.pop(1) # Remove the second item on the computer list at index 1
                print("Top discard brick: ", discard[0])

            else:
                computer_tower.insert(0, discard[0]) # Insert the value of the top brick on discard pile to computer tower at index 0
                discard.pop(0) # Remove the first element in discard pile
                discard.insert(0, computer_tower[1]) # Insert the second item on the computer tower to discard pile at index 0
                computer_tower.pop(1) # Remove the second item on the computer list at index 1
                print("Top discard brick: ", discard[0])
                
    return computer_tower
'''
Main part of the function.
'''
def main():
    # Importing library
    import random

    # Creating the main pile and discard pile
    main_pile, discard = setup_bricks()
    
    print("Main pile: ", main_pile)
    print("Discard pile: ", discard)

    # Shuffle the bricks on the main pile
    shuffle_bricks(main_pile)
    print("Shuffled pile: ", main_pile)

    # Checking whether the main pile is empty.
    check_bricks(main_pile, discard)

    # Dealing the values in the main pile to the computer and main towers
    computer_tower, human_tower = deal_initial_bricks(main_pile)

    print("Computer tower: ", computer_tower)
    print("Human tower: ", human_tower)
    
    # Get the top brick to be used in replacing a brick in the tower.
    brick = get_top_brick(main_pile, discard, human_tower, computer_tower)
    print("Top brick:", brick)

    # Add the first brick to the discard pile
    add_brick_to_discard(brick, discard)
    print("New discard", discard)

    # Looping between the computer and players until the condition is satisfied.
    flag = 0
    flag_2 = 0
    while True:
        try:
            brick = get_top_brick(main_pile, discard, human_tower, computer_tower) # Getting the top brick
            print("Top brick:", brick)
            brick_to_be_replaced = int(input("Enter the value of the brick to be replaced: ")) # Input the value to be replaced from the tower 
            find_and_replace(brick, brick_to_be_replaced, computer_tower, human_tower, discard) # Find and replace the brick in the tower
            print("Added HUMAN Tower:", human_tower)

            # Using the all function and a for loop to check if the bricks have been arranged in ascending order.
            if(all(human_tower[i] <= human_tower[i + 1] for i in range(len(human_tower) - 1))):
                flag = 1
            # Checking if tower blaster
            if (flag):
                print("Yes: Human Tower Blaster")
                break  
            else:
                print("Player: Keep on going")
            # Computer's turn to pick a brick   
            computer_play(computer_tower, main_pile, discard)

            # Checking if tower blaster
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
                break
            else:
                print("Computer: Keep on going")
  

if __name__ == "__main__":
        main()
