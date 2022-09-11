"""
Exercise 2: Hotel booking sytem
Create a simple program that takes in two inputs:
1. Number of guests
2. Period of day

Our hotel can accomomdate a minimum of 1 person and a maximum of 4 in a room.
Write a program that given the two inputs will allow for room bookings or deny bookings if the
number of guests is greater than 4. However, the program will give a 10% discount for stays
greater than 10 days.

The rate per night per guest is Kshs. 15,000.0. Gve the total bill for the booking as a final output


"""

while True:
    try:
        number_of_guests = int(input("Welcome how many guests are you?"))
        if number_of_guests < 1:
            print("enter a valid guest count")
            continue
        elif number_of_guests > 4:
            print("we are sorry but we cutrrently can not accomodate more than 4 people")
            break
        else:
            while True:
                try:
                    stay = int(input("How long will you stay with us?"))
                    if stay < 1:
                        print("enter a valid duration")
                        continue
                    elif stay > 10:
                        print("We are pleased to offer toa a 10% discount")
                        print("Your total bill is", number_of_guests * stay * 15000 * 0.9)
                        break
                    else:
                        print("Your total bill is:", number_of_guests * stay * 15000)
                        break
                except:
                    print("Kindly enter an integer" )
        break
    except:
        print("please enter an integer")


   