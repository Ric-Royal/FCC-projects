'''
Name: Richard Kabiru Waithera
Strathmore student ID: 150684
Reference sources: https://www.w3schools.com/python/python_while_loops.asp
                    https://www.geeksforgeeks.org/random-numbers-in-python/
I worked alone with assistance from open source learning materials.

'''
# Importing libraries
import random

with open("template_behavior_{richard_kabiru}.txt", "a") as f:

    # Input variables. 
    # Assign the user's name to a variable called name.
    # print out the name of the user and a welcome statementy
    name = input("Name:")
    print(name, file = f)

    print("Hello " + str(name) + ". Welcome to ABC Supermarket.", file = f)

    # Using a dictionary to list the available products
    products = {
    "lottery" : 200,
    "bread" : 95,
    "milk" : 70,
    "soda" : 60,
    }

    # Print out a list of products available
    print("The products available are", products, file = f)

    # Ticket purchase
    total_amt = float(input("Hey how much money do you have? Kshs. "))
    print("Your initial balance is Kshs.", total_amt, file = f)

    # Use a while loop to prevent keying in of a wrong entry when the user is asked whether they want to purchase a ticket.
    # Try and except have been used in case the user keys in the wrong entry.
    while True:
        try:
            # Ask the user whether they want to purchase a ticket.
            tct_purchase = input(str(name) + " do you want to purchase a ticket? Enter Y or y for yes and N or n for no:")
        
            # Use if statements to check which condition qualifies.
            # check if user has entered y for yes.
            if tct_purchase == "y":
                    # Generating random integers between 0 and 2 for the ticket and assign it to a variable.
                    tct_number = random.randint(0,2)
                    print("This is your ticket number:", tct_number)

                    # Use if statements to check if the user has won the lottery game
                    # Assigning the winning value of the winning ticket
                    if tct_number == 1:
                        winnings = random.randint(2,10) * 100
                        current_bal = total_amt - products["lottery"] + winnings
                    
                        print("Congratulations. You won Kshs.", winnings, file = f)
                        print("Your current balance is Kshs.", current_bal, file = f)
                        print("Thank you for purchasing a ticket. ***All the best***", file = f)
                        break

                    else:
                        current_bal = total_amt - products["lottery"]
                        winnings = 0
                        print("Your current balance is Kshs.", current_bal, file = f)
                        print("Thank you for purchasing a ticket. ***All the best next time***", file = f)
                        break
                    
            # Check if user has entered Y for yes
            elif tct_purchase == "Y":
                # Generating random integers
                    tct_number = random.randint(0,2)
                    print("This is your ticket number",tct_number, file = f)

                    # Use if statements to check if the user has won the lottery game
                    # Assigning the winning value of the winning ticket
                    if tct_number == 1:
                        winnings = random.randint(2,10) * 100
                        current_bal = total_amt - products["lottery"] + winnings
                    
                        print("Congratulations. You won Kshs.", winnings, file = f)
                        print("Your current balance is Kshs.", current_bal, file = f)
                        print("Thank you for purchasing a ticket. ***All the best***", file = f)
                        break
                    else:
                        current_bal = total_amt - products["lottery"]
                        winnings = 0 

                        print("Your current balance is Kshs.", current_bal, file = f)
                        print("Thank you for purchasing a ticket. ***All the best next time***", file = f)
                        break

            # Check if user has entered n for no               
            elif tct_purchase == "n":
                print("No tickets were purchased.", file = f)
                print("Thank you for shopping with ABC Supermarket. Here is a list of products", products, file = f)
                current_bal = total_amt
                winnings = 0
                print("Your current balance is:", current_bal, file = f)

            # Check ifuser has entered N for no.    
            elif tct_purchase == "N":
                print("No tickets were purchased.", file = f)
                print("Thank you for shopping with ABC Supermarket. Here is a list of products", products, file = f)
                current_bal = total_amt
                winnings = 0
                print("Your current balance is:", current_bal, file = f)

            # If user has entered an invalid input print out a message to prompt them to consent to purchase the ticket again
            else:
                print("Enter y/y for Yes and n/N for No", file = f)
                tct_purchase = input("Do you want to purchase a ticket? Enter Y or y for yes and N or n for no:")
            break
    
        except:
            tct_purchase = input("Do you want to purchase a ticket? Enter Y or y for yes and N or n for no:")
            break
    # Bread
    #print("Your current balance is: Kshs.", current_bal)

    # Ask the customer if they want to purchase bread.
    bread_purchase = input("Do you want to purchase bread? ")
    print(bread_purchase)

    # If customer enters y proceed on to add the bread in the basket.
    if bread_purchase == "y":
        # Ask the customer to enter the number of loaves that they wish to buy.
        no_of_loaves = int(input("How many loaves of bread? "))

        while True:
            try:
                # Calculate the total cost of bread.
                cost_of_bread = no_of_loaves * products["bread"]

                # If the cost of bread is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the bread.
                if cost_of_bread > current_bal:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)
                
                    # Assign the cost of bread to 0, if no bread is added to the basket.
                    cost_of_bread = 0
                    no_of_loaves = 0
                    current_bal_bread = current_bal   
                    break
                # If the current balance is sufficient add the number of loaves into the basket.
                else:
                    print(str(no_of_loaves) + " loaves have been added to your basket", file = f)
                    current_bal_bread = current_bal - cost_of_bread
                    print("Your current balance is Kshs.", current_bal_bread, file = f)
                break
            # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.", file = f)

    # If customer enters Y proceed on to add the bread in the basket.
    elif bread_purchase == "Y":

        # Ask the customer to enter the number of loaves that they wish to buy.
        no_of_loaves = int(input("How many loaves of bread? "))

        while True:
            try:
                # Calculate the total cost of bread.
                cost_of_bread = no_of_loaves * products["bread"]

                # If the cost of bread is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the bread.
                if cost_of_bread > current_bal:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)

                    # Assign the cost of bread to 0, if no bread is added to the basket.
                    cost_of_bread = 0
                    no_of_loaves = 0
                    current_bal_bread = current_bal
                # If the current balance is sufficient add the number of loaves into the basket.    
                else:
                    print(str(no_of_loaves) + " loaves have been added to your basket", file = f)
                    current_bal_bread = current_bal - cost_of_bread
                    print("Your current balance is Kshs.", current_bal_bread, file = f)
                break

            # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.", file = f)

    # If the customer enters n, assign the cost of bread with the value 0 because no bread was added to the basket.            
    elif bread_purchase == "n":
        print("Bread has not been added on the purchase list", file = f)
        current_bal_bread = current_bal
        print("Your current balance is:", current_bal_bread, file = f)
        cost_of_bread = 0
        no_of_loaves = 0

    # If the customer enters n, assign the cost of bread with the value 0 because no bread was added to the basket.    
    elif bread_purchase == "N":
        print("Bread has not been added on the purchase list", file = f)
        current_bal_bread = current_bal
        print("Your current balance is:", current_bal_bread, file = f)
        cost_of_bread = 0
        no_of_loaves = 0
    # If the user keys in any other value, inform them that the bread was not purchased and move them to the next product
    else:
        print("Bread not purchased. Check out our other products", file = f)
        current_bal_bread = current_bal
        print("Your current balance is:", current_bal_bread, file = f)
        cost_of_bread = 0
        no_of_loaves = 0


    # Milk
    # print("Your current balance is: Kshs.", current_bal)

    # Ask the customer if they want to purchase milk.
    milk_purchase = input("Do you want to purchase milk? ")
    print(milk_purchase)

    # If customer enters y proceed on to add the milk in the basket
    if milk_purchase == "y":
        # Ask the user to enter the number of packets to buy
        no_of_pckts = int(input("How many packets of milk? "))
        while True:
            try:
                # Calculate the cost of milk
                cost_of_milk = no_of_pckts * products["milk"]

                # If the cost of milk is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the milk.
                if cost_of_milk > current_bal_bread:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)

                    # Assign the cost of milk to 0, if no milk is added to the basket.
                    cost_of_milk = 0
                    no_of_pckts = 0
                    current_bal_milk = current_bal_bread
                # If the current balance is sufficient add the number of packets into the basket.      
                else:
                    print(str(no_of_pckts) + " packets have been added to your basket", file = f)

                    # Calculate the current balance after adding lottery tickets and milk to the purchase list.
                    current_bal_milk = current_bal_bread - cost_of_milk
                    print("Your current balance is Kshs.", current_bal_milk, file = f)
                break

        # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.",  file = f)
                break

    # If customer enters Y proceed on to add the milk in the basket
    elif milk_purchase == "Y":
        no_of_pckts = int(input("How many packets of milk? "))
        while True:
            try:
                # Calculate the cost of milk
                cost_of_milk = no_of_pckts * products["milk"]

                # If the cost of milk is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the milk.
                if cost_of_milk > current_bal_bread:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)

                    # Assign the cost of milk to 0, if no milk is added to the basket.
                    cost_of_milk = 0
                    no_of_pckts = 0
                    current_bal_milk = current_bal_bread

                # If the current balance is sufficient add the number of packets into the basket. 
                else:
                    print(str(no_of_pckts) + " packets have been added to your basket", file = f)

                    # Calculate the current balance after adding lottery tickets and milk to the purchase list.
                    current_bal_milk = current_bal_bread - cost_of_milk
                    print("Your current balance is Kshs.", current_bal_milk, file = f)
                break

            # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.", file = f)
                break
    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket. 
    elif milk_purchase == "n":
        print("Milk has not been added on the purchase list", file = f)

        # Assign the current balance after adding the cost of tickets.
        current_bal_milk = current_bal_bread
        print("Your current balance is Kshs.", current_bal_milk, file = f)
        cost_of_milk = 0
        no_of_pckts = 0

    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket. 
    elif milk_purchase == "N":
        print("Milk has not been added on the purchase list", file = f)

        # Assign the current balance after adding the cost of tickets.
        current_bal_milk = current_bal_bread
        print("Your current balance is Kshs.", current_bal_milk, file = f)
        cost_of_milk = 0
        no_of_pckts = 0 

    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket. 
    else:
        print("Milk not purchased. Check out our other products", file = f)

        # Assign the current balance after adding the cost of tickets.
        current_bal_milk = current_bal_bread
        print("Your current balance is Kshs.", current_bal_milk, file = f)
        cost_of_milk = 0
        no_of_pckts = 0

    # soda
    #print("Your current balance is: Kshs.", current_bal)

    # Ask the customer if they want to purchase soda.
    soda_purchase = input("Do you want to purchase soda? ")
    print(soda_purchase)

    # If customer enters y proceed on to add the soda in the basket
    if soda_purchase == "y":

        # Ask the user to enter the number of bottles to buy
        no_of_bottles = int(input("How many bottles of soda? "))
        while True:
            try:
                # Calculate the cost of soda
                cost_of_soda = no_of_bottles * products["soda"]

                # If the cost of soda is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the soda.
                if cost_of_soda > current_bal_milk:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)

                    # Assign the cost of soda to 0, if no soda is added to the basket.
                    cost_of_soda = 0
                    no_of_bottles = 0
                    current_bal_soda = current_bal_milk
                # If the current balance is sufficient add the number of bottles into the basket.     
                else:
                    print(str(no_of_bottles) + " bottles have been added to your basket", file = f)
                
                    #Calculate the current balance after adding soda and milk to the purchase list.
                    current_bal_soda = current_bal_milk - cost_of_soda
                    print("Your current balance is Kshs.", current_bal_soda)
                break

            # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.", file = f)

        # If customer enters Y proceed on to add the soda in the basket
    elif soda_purchase == "Y":

        # Ask the user to enter the number of bottles to buy
        no_of_bottles = int(input("How many bottles of soda? "))

        while True:
            try:
                # Calculate the cost of soda
                cost_of_soda = no_of_bottles * products["soda"]

                # If the cost of soda is greater than the current balance then, 
                # inform the user that they do not have eneough funds to purchase the soda.
                if cost_of_soda > current_bal_milk:
                    print("Sorry, your current balance is not enough to buy this product(s)", file = f)

                    # Assign the cost of soda to 0, if no soda is added to the basket.
                    cost_of_soda = 0
                    no_of_bottles = 0
                    current_bal_soda = current_bal_milk
                # If the current balance is sufficient add the number of bottles into the basket.     
                else:
                    print(str(no_of_bottles) + " bottles have been added to your basket", file = f)

                    #Calculate the current balance after adding soda and milk to the purchase list.
                    current_bal_soda = current_bal_milk - cost_of_soda
                    print("Your current balance is Kshs.", current_bal_soda, file = f)
                break

            # If the user enters a non integer value, prompt them to enter an integer
            except:
                print("Only enter numerical vaues.", file = f)

    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket. 
    elif soda_purchase == "n":
        print("Soda has not been added on the purchase list", file = f)

        # Assign the current balance after adding milk to the purchase list.
        current_bal_soda = current_bal_milk
        print("Your current balance is Kshs.", current_bal_soda, file = f)
        cost_of_soda = 0
        no_of_bottles = 0

    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket. 
    elif soda_purchase == "N":
        print("soda has not been added on the purchase list", file = f)
        # Assign the current balance after adding milk to the purchase list.
        current_bal_soda = current_bal_milk
        print("Your current balance is Kshs.", current_bal_soda, file = f)
        cost_of_soda = 0
        no_of_bottles = 0

    # If the customer enters n, assign the cost of milk with the value 0 because no milk was added to the basket.     
    else:
        print("Soda not purchased.", file = f)

        # Assign the current balance after adding milk to the purchase list.
        current_bal_soda = current_bal_milk
        print("Your current balance is Kshs.", current_bal_soda, file = f)
        cost_of_soda = 0
        no_of_bottles = 0


    # Calculating cost of lottery
    cost_of_lottery = total_amt - current_bal + winnings

    # Calculate the total cost of all products
    total_cost = cost_of_bread + cost_of_milk + cost_of_soda + cost_of_lottery

    # Assign the current balance calculated after the purchase of soda
    curr_bal = current_bal_soda

    # inform the customer what their initial balance was and what did they win from the lottery.
    print("Your initial balance was Kshs.", total_amt, file = f)
    print("Your won Kshs.", winnings, file = f)

    # Print out the total cost of each product together with the quantity purchased
    print("Total cost of lottery is Kshs.", cost_of_lottery, file = f)
    print("Total cost of Soda is Kshs.", cost_of_soda, file = f)
    print("Number of botles of soda:", no_of_bottles, file = f)
    print("Total cost of bread is Kshs.", cost_of_bread, file = f)
    print("Number of loaves:", no_of_loaves, file = f)
    print("Total cost of milk is Kshs.", cost_of_milk, file = f)
    print("Number of packets of milk:", no_of_pckts, file = f)
    print("Total cost is Kshs.", total_cost, file = f)
    print("Thank you for shopping at ABC Supermarket. Your current balance is Kshs.", curr_bal, file = f)