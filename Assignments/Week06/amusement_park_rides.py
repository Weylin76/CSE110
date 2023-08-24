try:
    print()
    can_ride = False

    # validate that only 1 or 2 is entered for number of riders
    num_of_riders = int(input('How many riders are there? '))
    if num_of_riders < 1 or num_of_riders > 2:
        raise ValueError(
            'Invalid number of riders. Only 1 or 2 riders allowed.')

    # Gather variable information
    rider_hieght1 = int(input("What is the first rider's height? "))
    rider_age1 = int(input("What is the first rider's age? "))

    # if there is an addition rider gather information for second rider
    if num_of_riders == 2:
        rider_hieght2 = int(input("What is the second rider's height? "))
        rider_age2 = int(input("What is the second rider's age? "))

        # conditional logic for a pair of riders
        if rider_hieght1 < 36 or rider_hieght2 < 36:
            can_ride = False
        elif (rider_age1 >= 18 or rider_age2 >= 18):
            can_ride = True
        elif (rider_age1 >= 18 and rider_hieght1 >= 62) or (rider_age2 >= 18 and rider_hieght2 >= 62):
            can_ride = True
        else:
            can_ride = False

    # conditional logic for a single rider
    else:
        if rider_hieght1 >= 62 and rider_age1 >= 18:
            can_ride = True
        else:
            can_ride = False

    # Print decision to screen
    print()
    if can_ride == True:
        print('You are able to ride, enjoy the roller coaster!\n')
    else:
        print("Sorry, you may not ride on this dangerous roller coaster!\n")

# Handle all exceptions with printout of error message
except Exception as e:
    print("An error occurred:", str(e))
