# Wong Horng Jun
# TP061271

# Teo Chen Ming
# TP060668

import datetime

###
# Update car status when run BACKGROUND PROCESS #1 RUN ON STARTUP 
def update_car_status():
    # read lines in Booking.txt
    file_fh = open("Booking.txt", "r")
    if file_fh.read() != "":
        file_fh = open("Booking.txt", "r")
        new_bookingdetails = ""
        for line in file_fh.readlines():
            check_pending = line.strip().split(",")
            payment_duedate = datetime.datetime.strptime(check_pending[3], "%Y-%m-%d")
            # check if payment time limit has reached
            if datetime.datetime.now() > payment_duedate and check_pending[6] == "pending":
                # Create empty string to add strings in later
                new_line = ""
                new_bookingdetails += new_line # Add "new_line" into
            else:
                # join all elements in the "check pending" list if condition not met
                new_line = ','.join(check_pending)
                new_bookingdetails += new_line + "\n"

        # rewrite everything in Booking.txt with 'new_bookingdetails'
        cardetails_fh = open("Booking.txt", "w")
        cardetails_fh.write(new_bookingdetails)
        cardetails_fh.close()

###
# Update car status (rented/available) BACKGROUND PROCESS #2 RUN ON STARTUP
def update_car_rented(): 

    file_fh = open("customerPayment.txt", "r")
    if file_fh.read() != "":
        carlist = []
        # create new blank string
        new_carstatusdetails = ""
        file_fh = open("customerPayment.txt", "r")
        for line in file_fh.readlines():
            check_pending = line.strip().split(",") # strips away front and end empty spaces. Splits on ',', and stores results in a list of strings
            # convert string type into date type
            starting_date = datetime.datetime.strptime(check_pending[2], "%Y-%m-%d")
            ending_date = datetime.datetime.strptime(check_pending[3], "%Y-%m-%d")
            if starting_date < datetime.datetime.now() < ending_date:
                # set value of car_plate to the value equal to index 1 of list check_pending
                car_plate = check_pending[1]
                carlist.append(car_plate)

        car_editStatus_fh = open("cars_details.txt", "r")
        for car_editstatus in car_editStatus_fh.readlines():
            car_editstatus_list = car_editstatus.strip().split(",")
            # check condition 1
            if car_editstatus_list[0] in carlist:
                car_editstatus_list[8] = "rented" # change index 8 to rented
                new_line = ','.join(car_editstatus_list)
                new_carstatusdetails += new_line + "\n"
            else:
                new_line = ','.join(car_editstatus_list)
                new_carstatusdetails += new_line + "\n"

        # rewrite everything in cars_details.txt with new_carstatusdetails
        cardetails_fh = open("cars_details.txt", "w")
        cardetails_fh.write(new_carstatusdetails)
        cardetails_fh.close()

###
# Main Menu and Login Interface
def login():
    ###
    # start while loop here if they give invalid input
    while True:
        # prints a welcome screen
        print('''
        Welcome to SUPER CAR RENTAL SERVICES (SCRS)
        Would you like to login as:
        - Admin? Enter A to continue.
        - User? Enter U to continue.
        - Enter E to exit''')

        loginAns = input("\nEnter your login type (A/U) or (E) to exit: ")
        if loginAns == "A" or loginAns == "a":
            #Login as Admin
            adminLogin()
        elif loginAns == "U" or loginAns == "u":
            #Link for Unregistered and Registered
            unregistered_customerPanel()
        elif loginAns == "E" or loginAns == "e":
            #Exit
            exit_panel()
            ###
            break
        else:
            print("Please insert a valid value.")
            continue # go back to while loop

###
# Register for New Users
def register():
    # start while loop
    while True:
        print("ඞ REGISTER ඞ")
        # read user inputs
        register.username = input("Enter username: ")
        register.password = input("Enter password: ")
        register.phonenum = input("Enter phone number: ")
        register.email_address = input("Enter e-mail address: ")
        
        # check condition
        if len(register.username) <=1 or len(register.password) <=1 or len(register.phonenum) <=1 or len(register.email_address) <=1:
            print("Values should be more than 1")
            continue #loop back to while loop
        else:
            # read user_details.txt file
            user_fh = open("user_details.txt", "r")
            if (register.username in user_fh.read()) or (register.phonenum in user_fh.read()) or (register.email_address in user_fh.read()):
                print("Username, Phone number or E-mail address already taken. Please Try Again")
                continue #loop back to while loop

            else:
                # append the register details into user_details.txt
                user_fh = open("user_details.txt", "a")
                user_fh.write(f"{register.username},{register.password},{register.phonenum},{register.email_address}\n")
                user_fh.close() # Close the file

        while True:
            print("Congratulation! You are now part of us!")
            print("1. Login")
            print("2. Exit")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                customerUsername = userLogin()
                customerUsername1 = customerUsername
                print(f"Welcome {customerUsername1}!")
                registered_customerPanel(customerUsername1)
            elif user_input == "2":
                exit_panel()
                break
            else:
                print("Invalid.")
                continue
        break

###
# Admin Login
def adminLogin():
    print("\nYou're now logging in as Admin\n")
    # read admin input
    adminName = input("Enter your username: ")
    adminPassword = input("Enter your password: ")
    usernameValid = False

    # read lines from admin_details.txt
    admin_fh = open("admin_details.txt", "r")

    for line in admin_fh:
        adminusername, adminpassword = line.strip().split(",") # split data and assign info to 2 variables
        # check condition(s)
        if adminName == adminusername:
            usernameValid = True
            if adminPassword == adminpassword:
                print(f"\nWelcome! {adminName}")
                print("What would you like to do today?")
                adminPanel()
            else:
                print("Login Failed. Please Try Again.")
                return

    # if Username not found in admin_details.txt
    if not usernameValid :
        print("Username or Password is invalid. Please try again.")
        return

###
# User login 
def userLogin():
    foundUsername = False
    # print something 
    print("\nYou're now logging in as User.\n")
    # read user input
    userName = input("Enter your username: ")
    userPassword = input("Enter your password: ")

    # Open user_details.txt and Read file
    user_fh = open("user_details.txt", "r")
    
    for line in user_fh:
        username, password, phonenum, email_address = line.strip().split(',')
        # check condition (if username and password matches)
        if userName == username:
            foundUsername = True
            if userPassword == password:
                return userName 
            else:
                print("Wrong password. Please Try Again.")
                return
    # if Username not found in user_details.txt
    if not foundUsername:
        while True:
            print("Username or Password is invalid, Try Again.")
            print("1. Main Menu")
            userLogin_choice = input("Enter 1: ")
            if userLogin_choice == "1":
                return
            else:
                print("Invalid input.")
                continue

###
# Display Cars Available to be rented
def cars_available():
    print("\n===========================================================================")
    print("Cars Available to be rented:")
    #take data from txt file, data inserted through modify_car_details()

    # print all cars
    carsAvailable_fh = open("cars_details.txt", "r")

    for cars_to_be_rented in carsAvailable_fh.readlines():
        available_cars = cars_to_be_rented.strip().split(",")
        cars_available_line = f"Car: {available_cars[1]} {available_cars[2]} Car Rental Fee: {available_cars[7]}"
        print(f"{cars_available_line}\n")

    while True:
        rentCar_input = input("\n1. Return to previous screen\n\nEnter a choice:")
        if rentCar_input == "1":
            return
        else:
            print("Invalid input.")
            continue

###
# Pre-Modify Car Detail Panel
def modify_add():
    # provides selections for user then directs user to the respective function
    while True:
        print("\n==============================")
        print("1. Modify a car detail")
        print("2. Return to admin panel")
        print("==============================")

        modify_choice = input("Enter your choice: ")
        if modify_choice == "1":
            car_details_modify()
        elif modify_choice == "2":
            return
        else:
            print("Invalid input. Choose 1 or 2.")
            continue

###
# Modify Car Details
def car_details_modify():
    print("\n===================================")
    print("MODIFYING CAR DETAILS\n")

    cars_fh = open("cars_details.txt","r")
    for line in cars_fh.readlines(): # Read the lines
        allcars = line.strip().split(",")
        print(allcars)

    found_car = False
    carChosen = input("Choose car to be modified (Car Plate): ")
    print("====================================")
    #Read a specific line from cars_details.txt with for loop
    cars_fh = open("cars_details.txt","r")
    for line in cars_fh.readlines(): # Read the lines
        car_info = line.strip().split(",") # Splits on ',', and stores results in a list of strings
        carPlate = car_info[0] #Read the first data 
        if carPlate == carChosen:
            found_car = True

            temp = carChosen
            newcarChosen = temp
            car_to_modify = car_info

    if not found_car:
        print(f"Car plate '{carChosen}' not found. Unable to modify details.")
        anykey = input("Enter any key to return: ")
        return

    while True:
        print(f"Currently Modifying: {car_to_modify}")
        print("Choose a part to modify:")
        print("0. Car Plate\n1. Car Brand\n2. Car Name\n3. Car Year\n4. Car Color\n5. Car Max Speed\n6. Car Pax\n7. Car Rental Fee\n8. Car Availability\n9. Exit")
        decision = input("Enter your choice: ")

        # Check if it can be converted to integer
        try:
            decision = int(decision)
        except ValueError:
            print("Only Integers are allowed")
            continue

        if 0 <= decision <= 8:
            # get new detail
            newvalue = input(f"Changing '{car_to_modify[decision]}' to: ")

            new_cardetails = "" #Open a blank string to add stuff inside

            #read and edit the specific index, else just append whole line back
            cars_fh1 = open("cars_details.txt","r")
            
            carChosen = newcarChosen
            for line in cars_fh1.readlines():
                if carChosen in line: 
                    car_chosen_list = line.strip().split(",")
                    # start loop in range of length of car_chosen_list
                    for count in range(len(car_chosen_list)):
                        if count == decision:
                            if decision == 0:
                                newcarChosen = newvalue
                                car_chosen_list[count] = newvalue
                            elif decision == 5:
                                car_chosen_list[count] = f"{newvalue}km/h"
                            elif decision == 7:
                                car_chosen_list[count] = f"RM{newvalue}"
                            else:
                                # replace the index of car_chosen_list with newvalue
                                car_chosen_list[count] = newvalue

                    new_line = ','.join(car_chosen_list)
                    new_cardetails += new_line + "\n"
                    
                else:
                    new_line = line
                    new_cardetails += new_line

            cardetails_fh = open("cars_details.txt", "w")
            cardetails_fh.write(new_cardetails)
            cardetails_fh.close()
            print("Successfully changed!")
            if decision == 5:
                car_to_modify[decision] = f"{newvalue}km/h"
            elif decision == 7:
                car_to_modify[decision] = f"RM{newvalue}"
            else:
                # replace the index of car_chosen_list with newvalue
                car_to_modify[decision] = newvalue   
            continue
        
        elif decision == 9:
            return

        else:
            print("Enter a value between 0 to 9")
            continue

###
# Append a car and its details in cars_details.txt
def add_a_car():
    while True:
        print("\n==========\nADDING A CAR\n==========\n")
        car_plate = input("Enter Car Plate: ")
        car_brand = input("Enter Car Brand: ")
        car_name = input("Enter Car Name: ")
        car_year = input("Enter Car Year: ")
        car_color = input("Enter Car Color: ")
        car_maxspeed = input("Enter Car Max Speed: ")
        car_pax = input("Enter Car Pax: ")
        car_rentalfee = input("Enter Car Rental Fee: ")
    
        while True:
            addcar_choice1 = input("Do you wish to add this car? (Y/N): ")
            if addcar_choice1 == "Y" or addcar_choice1 == "y":
                cardetails_fh = open("cars_details.txt", "a")
                # append the line into cars_details.txt
                cardetails_fh.write(f"{car_plate},{car_brand},{car_name},{car_year},{car_color},{car_maxspeed}km/h,{car_pax},RM{car_rentalfee},available\n")
                cardetails_fh.close()

                print("Successfully added a car!\n")
                while True:
                    print("Add another car? (Y/N)")
                    add_choice = input("Enter Y or N: ")

                    if add_choice == "Y" or add_choice == "y":
                        break
                    elif add_choice == "N" or add_choice == "n":
                        return
                    else:
                        print("Invalid input.")
                        continue
                break
            elif addcar_choice1 == "N" or addcar_choice1 == "n":
                print("Redirecting you back.\n")
                return
            else:
                print("Invalid input.")
                continue
        continue

# displays cars that are currently rented out
def admin_display_rented_record():
    print("\n===========================================================================")
    print("Records of cars rented out now:")
    #take data from txt file, data inserted through modify_car_details()
    
    cars_rented = 0 # Declare cars_rented to 0
    cars_rented_out_fh = open("cars_details.txt", "r")
    for cars_rented_out in cars_rented_out_fh.readlines():
        rented_cars = cars_rented_out.strip().split(",")
        if rented_cars[8] == "rented":
            # Insert and convert cars_details.txt to list
            cars_rented_line = f"Car Plate:{rented_cars[0]} Car brand:{rented_cars[1]} Car name:{rented_cars[2]} Car year:{rented_cars[3]} Car color:{rented_cars[4]} Car max speed:{rented_cars[5]} Car pax:{rented_cars[6]} Car Rental Fee:{rented_cars[7]}"
            print(cars_rented_line) 
            cars_rented += 1 # if car is rented then cars_rented + 1

    # if cars_rented equals to 0 or no cars rented then print statement
    if cars_rented == 0:
        print("No car is currently rented.")

    anykey = input("Enter any key to return to previous menu.\n")
    return

# display cars that are currently available
def admin_display_available_record():
    print("\n===========================================================================")
    print("Records of cars available now:")
    #take data from txt file, data inserted through modify_car_details()
    cars_available = 0
    cars_available_now_fh = open("cars_details.txt", "r")
    for cars_available_now in cars_available_now_fh.readlines():
        available_cars = cars_available_now.strip().split(",")
        if available_cars[8] == "available":
            cars_available_line = f"Car Plate:{available_cars[0]} Car brand:{available_cars[1]} Car name:{available_cars[2]} Car year:{available_cars[3]} Car color:{available_cars[4]} Car max speed:{available_cars[5]} Car pax:{available_cars[6]} Car Rental Fee:{available_cars[7]}"
            print(cars_available_line)
            cars_available += 1

    if cars_available == 0:
        print("No car is currently available.")

    anykey = input("Enter any key to return to previous menu.\n")
    return

# displays customer booking records
def admin_display_customer_bookings():
    print("\n===========================================================================")
    print("Records of customer bookings:")
    bookingfile_fh = open("Booking.txt","r")

    for bookingline in bookingfile_fh.readlines(): # Read the lines
        user_info = bookingline.strip().split(",") # Splits on ',', and stores results in a list of strings
        print(f"Customer name: {user_info[0]}\tCar booked: {user_info[1]}\tBooking initiated date: {user_info[2]}\tCar book starting date: {user_info[4]}\tCar book end date: {user_info[5]}")
    
    anykey = input("Enter any key to return to previous menu.\n")
    return

# display customer payment records
def admin_display_customer_payment():
    print("\n===========================================================================")
    print("Records of customer payment:")
    paymentfile_fh = open("customerPayment.txt","r")

    for paymentline in paymentfile_fh.readlines(): # Read the lines
        user_info = paymentline.strip().split(",")
        print(f"Customer name: {user_info[0]}\tCar booked: {user_info[1]}\tCar book starting date: {user_info[2]}\tCar book end date: {user_info[3]}\tDays Booked: {user_info[4]} days\tPayment method: {user_info[5]}\tPayment Total: {user_info[6]}\tPayment date: {user_info[7]}")

    anykey = input("Enter any key to return to previous menu.\n")
    return

###
# Display records
def display_records():
        
    while True:
        print("===================================")
        print("1. Display records of cars rented out")
        print("2. Display records of cars available for rent")
        print("3. Display records of customer bookings")
        print("4. Display records of customer payments")
        print("5. Exit to admin panel")
        print("===================================")

        admin_display_record_input = input("Enter your choice: ")
        if admin_display_record_input == "1":
            admin_display_rented_record()       
        elif admin_display_record_input == "2":
            admin_display_available_record()
        elif admin_display_record_input == "3":
            admin_display_customer_bookings()
        elif admin_display_record_input == "4":
            admin_display_customer_payment()
        elif admin_display_record_input == "5":
            return
        else:
            print("Enter a value between 1 to 5")
            continue

# search for a specific customer booking
def search_bookings():
    print("Enter a name to search customer bookings.\nName listed below:")
    searchBookings_fh = open("user_details.txt", "r")

    for name_line in searchBookings_fh.readlines():
        all_names = name_line.strip().split(",")
        print(all_names[0])
    
    search_booking_input = input("Enter a name (Case Sensitive): ")
    print("Customer Booking records:")
    found_user = False
    bookingfile_fh = open("Booking.txt", "r")

    for bookingline in bookingfile_fh.readlines(): # Read the lines
        user_info = bookingline.strip().split(",") # Splits on ',', and stores results in a list of strings
        username = user_info[0] #Reads the first data
        if username == search_booking_input:
            found_user = True
            user_info = bookingline.strip().split(",")
            print(f"Customer name: {user_info[0]}\tCar booked: {user_info[1]}\tBooking initiated date: {user_info[2]}\tCar book starting date: {user_info[4]}\tCar book end date: {user_info[5]}")

    if not found_user:
        print("User not found/ user does not have any booking records (YET).")

    print("\nRedirecting you to previous session.")
    return

# search for a specific customer payment
def search_payment():
    print("Enter a name to search customer payment records.\nName listed below:")
    searchPayment_fh = open("user_details.txt", "r")

    for name_line in searchPayment_fh.readlines():
        all_names = name_line.strip().split(",")
        print(all_names[0])
    
    search_payment_input = input("Enter a name (Case Sensitive): ")
    print("Customer Payment records:")
    found_user = False
    paymentfile_fh = open("customerPayment.txt","r")

    for paymentline in paymentfile_fh.readlines(): # Read the lines
        user_info = paymentline.strip().split(",") # Splits on ',', and stores results in a list of strings
        username = user_info[0] #Reads the first data
        if username == search_payment_input:
            found_user = True
            user_info = paymentline.strip().split(",")
            print(f"Customer name: {user_info[0]}\tCar booked: {user_info[1]}\tCar book starting date: {user_info[2]}\tCar book end date: {user_info[3]}\tDays Booked: {user_info[4]} days\tPayment method: {user_info[5]}\tPayment Total: {user_info[6]}\tPayment date: {user_info[7]}")

    if not found_user:
        print("User not found/ user did not make any payment (YET).")

    print("\nRedirecting you to previous session.")
    return

###
# Search records
def search_records():

    while True:
        print("\n\n==================================================")
        print("What are you searching for?")
        print("1. Customer Bookings")
        print("2. Customer Payment for a specific time duration")
        print("3. Return to previous screen")
        print("==================================================")
    
        search_input = input("\nEnter a number: ")
        if search_input == "1":
            search_bookings()
        elif search_input == "2":
            search_payment()
        elif search_input == "3":
            return
        else:
            print("Enter value between 1 or 3.")
            continue

###
# Return a rented car
def return_rented_car():
    print("\n===========================================================================")
    print("Records of cars rented:")
    #take data from txt file, data inserted through modify_car_details()
    count = 0
    cars_rented_out_fh = open("cars_details.txt", "r")
    for cars_rented_out in cars_rented_out_fh.readlines():
        rented_cars = cars_rented_out.strip().split(",")
        if rented_cars[8] == "rented":
            cars_rented_line = f"Car Plate:{rented_cars[0]} Car brand:{rented_cars[1]} Car name:{rented_cars[2]} Car year:{rented_cars[3]} Car color:{rented_cars[4]} Car max speed:{rented_cars[5]} Car pax:{rented_cars[6]} Car Rental Fee:{rented_cars[7]}"
            print(cars_rented_line)
            count += 1

    if count == 0:
        print("\nNo car currently rented.\n")
        anykey = input("Enter any key to return: ")
        return

    while True:
        return_rented_input = input("\n1. Return a rented car above\n2. Return to previous screen\n\nEnter a choice:")
        if return_rented_input == "1":
            returncar_chosen = input("Choose car to be returned (Car Plate): ")
            print("====================================")
            found_car = False
            #Read a specific line from cars_details.txt
            cars_details_fh = open("cars_details.txt","r")
            for line in cars_details_fh.readlines(): # Read the lines
                car_info = line.strip().split(",") # Splits on ',', and stores results in a list of strings
                carPlate = car_info[0] #Read the first data
                # check condition
                if carPlate == returncar_chosen and car_info[8] == "rented":
                    found_car = True
                    car_info1 = car_info

            if not found_car:
                print(f"Car plate '{returncar_chosen}' not found/not rented. Unable to return car.")
                anykey = input("Enter any key to return: ")

                return

            while found_car == True:
                print(f"Currently returning: {car_info1}")
                print("Are you sure?")
                decision = input("Enter your choice (YES/NO): ")

                if decision == "YES":
                    file_fh = open("cars_details.txt", "r")

                    new_cardetails = "" # Blank file
                    for line in file_fh.readlines():
                        if returncar_chosen in line: 
                            car_chosen_list = line.strip().split(",")                                 
                            car_chosen_list[8] = "available" 
                            new_line = ','.join(car_chosen_list)
                            new_cardetails += new_line + "\n"                                         
                        else:
                            new_line = line
                            new_cardetails += new_line
                    
                    cardetails_fh = open("cars_details.txt", "w")
                    cardetails_fh.write(new_cardetails)
                    cardetails_fh.close()
                    print("Successfully returned!")
                    return
                    
                elif decision == "NO":
                    print("Sending you back to admin panel...")
                    return
                else:
                    print("Invalid input. Case sensitive.")
                    continue

        elif return_rented_input == "2":
            return
        else:
            print("Invalid input.")
            continue

###
#Admin Panel 
def adminPanel():
    while True:
        print("===================================")
        print("1. Add cars to be rented out")
        print("2. Modify car details")
        print("3. Display records")
        print("4. Search records")
        print("5. Return a rented car")
        print("6. Return to login screen")
        print("7. Exit")
        print("===================================")

        admin_input = input("Enter your choice: ")
        if admin_input == "1":
            add_a_car()
        elif admin_input == "2":
            modify_add()
        elif admin_input == "3":
            display_records()
        elif admin_input == "4":
            search_records()    
        elif admin_input == "5":
            return_rented_car()
        elif admin_input == "6":
            return
        elif admin_input == "7":
            exit_panel()
            break
        else:
            print("Enter a value between 1 to 7.")
            continue

###
# Modify Details Menu
def modify_details():
    while True:
        print("\n=================================================")
        print("1. Modify your personal details.")
        print("OR")
        print("2. Return to previous menu.")
        print("=================================================")
    
        modifyDetailsInput = input("\nChoose 1 or 2: ")
        if modifyDetailsInput == "1":
            modify_personal_details()
        elif modifyDetailsInput == "2":
            return
        else:
            print("Invalid input.")
            continue

###
# Modify Personal Details
def modify_personal_details():
    found_user = False
    print("\n===================================")
    print("MODIFYING PERSONAL DETAILS\n")
    current_username = input("Enter your current username: ")
    current_password = input("Enter your current password: ")
    
    userfile_fh = open("user_details.txt","r")
    for line in userfile_fh.readlines(): # Read the lines
        user_info = line.strip().split(",") # Splits on ',', and stores results in a list of strings
        username = user_info[0] #Reads the first data
        password = user_info[1] #Reads the 2nd data
    
        # check if first and second data equal to input username and password
        if username == current_username and password == current_password:
            found_user = True
            user_info1 = user_info
            temp = username
            newUsernameChosen = temp

    if not found_user:
        print("Username invalid. Unable to modify details.")
        anykey = input("Enter any key to return: ")

        return

    while True:
        print("====================================")
        print(f"Currently Modifying: {user_info1}")
        print("Choose a part to modify:")
        print("0. User name\n1. User password\n2. Phone Number\n3. E-mail address\n4. Return to previous screen\n5. Exit\n")
        decision = input("Enter your choice: ")

        try:
            decision = int(decision) # Check integer
        except:
            print("Only Integers are allowed")
            continue
        
        current_username = newUsernameChosen
        if decision in [0,2,3]:
            # get new detail
            newvalue = input(f"Changing '{user_info1[decision]}' to: ")

            templist = []

            file_fh = open("user_details.txt", "r")
            for line in file_fh.readlines():
                decisionline = line.strip().split(",")
                templist.append(decisionline[decision])

            if newvalue in templist:
                print(f"\n'{newvalue}' has been taken. Please use another value.")
                continue
            else:
                file_fh = open("user_details.txt", "r")
                new_userdetails = "" # Blank file
                for line in file_fh.readlines():
                    if current_username in line:
                        user_chosen_list = line.strip().split(",")
                        # Start for loop in range for length of the list
                        for count in range(len(user_chosen_list)):
                            if count == decision:
                                user_chosen_list[count] = newvalue
                                
                        # Join elements in the list with "," and make it a string
                        new_line = ",".join(user_chosen_list)
                        new_userdetails += new_line + "\n"

                    else:
                        new_line = line
                        new_userdetails += new_line
                
                userdetails_fh = open("user_details.txt", "w")
                userdetails_fh.write(new_userdetails)
                userdetails_fh.close()
                print("\nSuccessfully changed!")
                user_info1[decision] = newvalue
                continue
        
        elif decision == 1:
            # get new detail
            newpassword = input(f"Changing '{user_info1[decision]}' to: ")

            while True:
                confirm_new_password = input("Enter new password again: ")
                if confirm_new_password == newpassword:
                    file_fh = open("user_details.txt", "r")
                    new_userdetails = "" # Blank file
                    for line in file_fh.readlines():
                        if current_username in line: 
                            user_chosen_list = line.strip().split(",")                                 
                            for count in range(len(user_chosen_list)):
                                if count == decision:                                 
                                    user_chosen_list[count] = newpassword
                            new_line = ','.join(user_chosen_list)
                            new_userdetails += new_line + "\n"                                         
                        else:
                            new_line = line
                            new_userdetails += new_line

                    userdetails_fh = open("user_details.txt", "w")
                    userdetails_fh.write(new_userdetails)
                    userdetails_fh.close()
                    print("\nSuccessfully changed!")
                    return

                else:
                    print("Incorrect password input.")
                    continue

        elif decision == 4:
            return
        
        elif decision == 5:
            exit_panel()
            break
        
        else:
            print("Enter a value between 0 to 5")
            continue

###
# Display Personal Rental History
def rental_history(customerUsername1):
    found_user = False
    print("Personal rental history:")
    paymentfile_fh = open("customerPayment.txt","r")

    for paymentline in paymentfile_fh.readlines(): # Read the lines
        user_info = paymentline.strip().split(",") # Splits on ',', and stores results in a list of strings
        username = user_info[0] #Reads the first data
        if username == customerUsername1:
            found_user = True
            print(f"Customer name: {user_info[0]}\tCar booked: {user_info[1]}\tCar book starting date: {user_info[2]}\tCar book end date: {user_info[3]}\tDays Booked: {user_info[4]} days\tPayment method: {user_info[5]}\tPayment Total: {user_info[6]}\tPayment date: {user_info[7]}")

    if not found_user:
        print("\nYou do not have any rental history (YET).\nRedirecting you back to the panel.\n")
        return

    anykey = input("Enter any key to be redirected back to the panel: ")
    return

###
# Display Cars Available to be rented
def cars_details():
    print("\n===========================================================================")
    print("Cars Available to be rented:")
    # Take data from txt file, data inserted through modify_car_details()

    rented_car = open("cars_details.txt", "r")
    for cars_to_be_rented in rented_car.readlines():
        available_cars = cars_to_be_rented.strip().split(",")
        # if cars' status is available then print car list
        if available_cars[8] == "available":
            cars_available_line = f" Car Plate: {available_cars[0]} Car Brand: {available_cars[1]} Car Name: {available_cars[2]} Car Year: {available_cars[3]} Car Color: {available_cars[4]} Car Max Speed: {available_cars[5]} Car Pax: {available_cars[6]} Car Rental Fee: {available_cars[7]}"
            print(f"{cars_available_line}\n")

    anykey = input("Enter any key to be redirected back to the panel: ")
    return

###
# Pre-Booking Screen
def select_book_car(customerUsername1):
    while True:
        print("\n===========================================================================")
        print("Pre-Booking Screen:")
        cars_to_be_rented_fh = open("cars_details.txt", "r")
        for cars_to_be_rented in cars_to_be_rented_fh.readlines():
            available_cars = cars_to_be_rented.strip().split(",")
            cars_available_line = f" Car: {available_cars[0]}, {available_cars[1]} {available_cars[2]} Car Rental Fee: {available_cars[7]}"
            print(f"{cars_available_line}\n")

        bookCar_input = input("\n1. Select a car to book\n2. Return to previous screen\n\nEnter a choice:")
        if bookCar_input == "1":
            select_book_car_2(customerUsername1)
        elif bookCar_input == "2":
            return
        else:
            print("Invalid input.")
            continue

###
# Select or Book a car
def select_book_car_2(customerUsername1):
    found_car = False
    while True:
        car_to_book = input("Enter car plate of the car you wish to book: ")
        carbook_fh = open("cars_details.txt","r")
        for line in carbook_fh.readlines(): # Read the lines
            car_info = line.strip().split(",") # Splits on ',', and stores results in a list of strings
            carPlate = car_info[0] #Read the first data 
            if carPlate == car_to_book:
                found_car = True
                car_info_details = f"Car Plate: {car_info[0]} Car Brand: {car_info[1]} Car Name: {car_info[2]} Car Year: {car_info[3]} Car Color: {car_info[4]} Car Max Speed: {car_info[5]} Car Pax: {car_info[6]} Car Rental Fee: {car_info[7]}"
                print(car_info_details)

        if found_car == False:
            print("Car not found.")
            continue

        # limits user to only book the car once at a time
        check_booking = open("Booking.txt",'r')
        for check_booking_lines in check_booking.readlines():
            if car_to_book in check_booking_lines:
                car_booked = check_booking_lines.strip().split(",")
                year, month, day = map(int, car_booked[4].split('-'))
                check_date = datetime.datetime(year, month, day)
                if customerUsername1 == car_booked[0] and car_to_book == car_booked[1] and datetime.datetime.now() <= check_date:
                    print("You have booked this car, please wait until your rental is over to book it again.")
                    anykey = input("Enter any key to select another car: ")
                    return

        # check and informs user that someone else has booked the car so he can make better decisions
        check_booking = open("Booking.txt",'r')
        for check_booking_line in check_booking.readlines():
            if car_to_book in check_booking_line:
                car_is_booked = check_booking_line.strip().split(",") 
                car_booked_date = datetime.datetime.strptime(car_is_booked[4], "%Y-%m-%d") # Changes String into Date format YYYY-MM-DD
                print(f"Someone else has booked this car on {car_is_booked[4]} to {car_is_booked[5]}, you can rent before {car_is_booked[4]} or after {car_is_booked[5]}.")
        break
    
    while True:
        # Confirmation of booking the specific car
        confirm_book_car = input("Is this the car you wish to book? (Y/N): ")                    
        if confirm_book_car == "Y" or confirm_book_car == "y":
            print("The car will no longer remain booked if user has not confirm the payment before the next day\nPlease write the date you want to start your car rental.")
            while True:          
                date = input("Enter date in YYYY-MM-DD(YEAR-MONTH-DAY) format: ")

                # check format and break if its correct and legit
                try:
                    year, month, day = map(int, date.split('-'))
                    starting_date = datetime.datetime(year, month, day)
                except ValueError:
                    print("Enter correct format.")
                    continue

                if starting_date > datetime.datetime.now():
                    break
                else:
                    print("Enter a legit date.")
                    continue
            
            # Input how many days user wish to rent the car
            while True:
                rent_duration = input("How many days do you wish to rent the car?: ")

                try:
                    rent_duration = int(rent_duration) # Check integer
                except ValueError:
                    print("Only integers are allowed.")
                    continue

                if rent_duration > 0:
                    break
                else:
                    print("Enter a value more than 0.")
                    continue
            
            # set format of rent_duration to datetime format 'days'
            days_added = datetime.timedelta(days = rent_duration)
            
            ending_date = starting_date + days_added

            cfmbooking_fh = open("Booking.txt", "r")
            if cfmbooking_fh.read() == "":
                
                while True:
                    confirm_booking = input("Confirm booking?(Y/N)\nChoice: ")
                    if confirm_booking == "Y" or confirm_booking == "y":
                        break
                    elif confirm_booking == "N" or confirm_booking == "n":
                        return
                    else:
                        print("Invalid input.")
                        continue
                username = customerUsername1          
                bookingdetails_fh = open("Booking.txt", "w")
                # set value of payment_timelimit to datetime format '1 day(s)'
                payment_timelimit = datetime.timedelta(days = 1)
                payment_datelimit = datetime.datetime.now().date() + payment_timelimit
                bookingdetails_fh.write(f"{username},{car_to_book},{datetime.datetime.now().date()},{payment_datelimit},{starting_date.date()},{ending_date.date()},pending\n")
                bookingdetails_fh.close()

                print(f"Successfully Booked!")
                return

            else:
                # Check if user's booking interferes with other bookings
                car_book = False
                checkdate_fh = open("Booking.txt", "r")

                if car_to_book in checkdate_fh.read():

                    checkdate_fh = open("Booking.txt", "r")
                    for line in checkdate_fh.readlines():
                        # if car_to_book in line:
                            car_is_booked = line.strip().split(",")

                            # Changes String into Date format YYYY-MM-DD
                            car_booked_date = datetime.datetime.strptime(car_is_booked[4], "%Y-%m-%d")
                            car_booked_end_date = datetime.datetime.strptime(car_is_booked[5], "%Y-%m-%d")
                            

                            if (car_booked_date<=starting_date<=car_booked_end_date) or (car_booked_date<=ending_date<=car_booked_end_date) or (starting_date<=car_booked_date<=ending_date) or (starting_date<=car_booked_end_date<=ending_date):
                                print("Your car booking has interfered with another user's booking. Please choose another date.") 
                                return

                            else:
                                car_book = True
                                
                    
                else:
                    while True:
                        confirm_booking = input("Confirm booking?(Y/N)\nChoice: ")
                        if confirm_booking == "Y" or confirm_booking == "y":
                            username = customerUsername1          
                            bookingdetails_fh = open("Booking.txt", "a")
                            payment_timelimit = datetime.timedelta(days = 1)
                            payment_datelimit = datetime.datetime.now().date() + payment_timelimit
                            bookingdetails_fh.write(f"{username},{car_to_book},{datetime.datetime.now().date()},{payment_datelimit},{starting_date.date()},{ending_date.date()},pending\n")
                            bookingdetails_fh.close()

                            print(f"Successfully Booked!")
                            return

                        elif confirm_booking == 'N' or confirm_booking == 'n':
                            return
                        else:
                            print("Invalid input.")
                            continue

                while car_book == True:
                    confirm_booking = input("Confirm booking?(Y/N)\nChoice: ")
                    if confirm_booking == "Y" or confirm_booking == "y":
                        username = customerUsername1          
                        bookingdetails_fh = open("Booking.txt", "a")
                        payment_timelimit = datetime.timedelta(days = 1)
                        payment_datelimit = datetime.datetime.now().date() + payment_timelimit
                        bookingdetails_fh.write(f"{username},{car_to_book},{datetime.datetime.now().date()},{payment_datelimit},{starting_date.date()},{ending_date.date()},pending\n")
                        bookingdetails_fh.close()

                        print(f"Successfully Booked!")
                        return

                    elif confirm_booking == "N" or confirm_booking == "n":
                        return
                    else:
                        print("Invalid input.")
                        continue
                               
        elif confirm_book_car == "N" or confirm_book_car == "n":
            return
        else:
            print("Invalid input.")
            continue

###
# Customer Payment 
def payment(customerUsername1):
    user_name = customerUsername1
    find_car_booking = open("Booking.txt", "r")

    user_found = False
    for line in find_car_booking.readlines():
        user_info = line.strip().split(",") # Splits on ',', and stores results in a list of strings
        username = user_info[0] #Reads the first data
        if username == user_name and user_info[6] == "pending":
            user_found = True
            user_booking_info = line.strip().split(",")
            print(user_booking_info)
    
    # If username not in booking.txt then print statement
    if not user_found:
        while True:
            print("===================================================")
            print(f"{user_name}, you have no pending bookings to pay!")
            print("===================================================")
            choice = input("1. Return to previous screen\nEnter 1: ")
            if choice == '1':
                return
            else:
                print("Invalid input.")
                continue

    while True:
        decision = input("\n1. Settle payment for a car booking\n2. Return to previous screen\n\nEnter a choice: ")
        if decision == "1":
            car_to_pay = False
            while True:
                choose_a_car = input("Choose a car (car plate) to proceed payment: ")
                choose_a_car = choose_a_car.upper()
                find_car_booking = open("Booking.txt", "r")
                for choose_to_pay in find_car_booking.readlines():
                    booking_info = choose_to_pay.strip().split(",")
                    car_plate_payment = booking_info[1]
                    username = booking_info[0]
                    if car_plate_payment == choose_a_car and username == user_name and booking_info[6] == "pending":
                        car_to_pay = True
                        break

                if not car_to_pay:
                    print("No car found.")
                    continue

                while car_to_pay == True:
                    payment_car_choice = input(f"\n{booking_info}\nIs this the car you would like to proceed payment with?(Y/N): ")
                    # Check user's decision
                    if payment_car_choice == "Y" or payment_car_choice == "y":
                        carsfile_readlines = open("cars_details.txt","r")
                        for line in carsfile_readlines.readlines(): # Read the lines
                            car_info = line.strip().split(",")
                            car_plate = car_info[0]
                            if car_plate == choose_a_car:
                                # Split value of index of booking info by "-" then convert into integer, and assign to three different variables
                                year1, month1, day1 = map(int, booking_info[4].split('-')) 
                                year2, month2, day2 = map(int, booking_info[5].split('-')) 
                                # Convert integer value into date format
                                d1 = datetime.datetime(year1, month1, day1) 
                                d2 = datetime.datetime(year2, month2, day2)
                                # Substraction
                                bookDay = d2 - d1
                                # reads the string in the list: car_info index 7 ignoring the first 2 characters, then convert it into integer
                                totalPrice = bookDay.days * int(car_info[7][2:])
                                print(f"Car Rent Start: {booking_info[4]}\nCar Rent End: {booking_info[5]}\nDays Rented: {bookDay.days} Days\nTotal Price: RM{totalPrice}\n")
                                break

                        confirmation_input = input("Do you want to confirm your payment? (Y/N): ")
                        if confirmation_input == "Y" or confirmation_input == "y":
                            print("====================")
                            print("Payment Method\n\n1. Credit Card\n2. TouchNGO E-Wallet")
                            print("====================")
                            while True:
                                paymentChoice = input("Choose one payment method: ")
                                # try and except is used in every input to avoid invalid input format

                                if paymentChoice == "1":
                                    paymentMethod = "Credit Card"
                                    cc_name = input("Name on card: ")

                                    while True:
                                        cc_num = input("Credit card number: ")
                                        try:
                                            cc_num1 = int(cc_num)
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(cc_num) == 14:
                                            break
                                        else:
                                            print("Card Number Invalid.")
                                            continue

                                    while True:    
                                        cc_expiryMonth = input("Card Expiry Month: ")
                                        try:
                                            cc_expiryMonth1 = int(cc_expiryMonth)  
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(cc_expiryMonth) == 2: 
                                            break
                                        else:
                                            print("Value Invalid.")
                                            continue

                                    while True:          
                                        cc_expiryYear = input("Card Expiry Year: ")

                                        try:  
                                            cc_expiryYear1 = int(cc_expiryYear)
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(cc_expiryYear) == 2:
                                            break
                                        else:
                                            print("Value Invalid.")
                                            continue

                                    while True:    
                                        cc_cvv = input("CVV: ")
                                        try:
                                            cc_cvv1 = int(cc_cvv)
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(cc_cvv) == 3:
                                            break
                                        else:
                                            print("CVV Invalid.")
                                            continue
                                    cc_expiry = str(f"{(cc_expiryMonth)}/{cc_expiryYear}")
                                    print("\n\nProcessing your payment.........\nPayment Done!")


                                elif paymentChoice == "2":
                                    paymentMethod = "TouchNGO E-Wallet"
                                    while True:
                                        tng_id =  input("TnG ID (8 digits): ")
                                        try:
                                            tng_id1 = int(tng_id)
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(tng_id) == 8:
                                            break
                                        else:
                                            print("ID Invalid.")
                                            continue

                                    while True:
                                        tng_pin =  input("TnG Pin (6 digits): ")
                                        try:
                                            tng_pin1 = int(tng_pin)
                                        except ValueError:
                                            print("Invalid Format, Only Integers.")
                                            continue

                                        if len(tng_pin) == 6:
                                            break
                                        else:
                                            print("Pin Invalid.")
                                            continue

                                    print("\n\nProcessing your payment.........\nPayment Done!")
                                else:
                                    print("Invalid Input")
                                    continue

                                userpayment_fh = open("customerPayment.txt", "a")
                                userpayment_fh.write(f"{user_name},{choose_a_car},{booking_info[4]},{booking_info[5]},{bookDay.days},{paymentMethod},RM {totalPrice},{datetime.datetime.now().date()}\n")
                                userpayment_fh.close()

                                edit_payment_status = open("Booking.txt", "r")
                                new_bookingdetails = ""
                                for line in edit_payment_status.readlines():
                                    check_pending = line.strip().split(",")
                                    # Change booking status from pending to paid
                                    if check_pending == booking_info:
                                        check_pending[6] = "paid"
                                        new_line = ','.join(check_pending)
                                        new_bookingdetails += new_line + "\n"
                                        
                                    else:
                                        new_line = ','.join(check_pending)
                                        new_bookingdetails += new_line + "\n"
                                edit_payment_status.close()

                                bookingdetails_fh = open("Booking.txt", "w")
                                bookingdetails_fh.write(new_bookingdetails)
                                bookingdetails_fh.close()

                                return

                        elif confirmation_input == "N" or confirmation_input == "n":
                            return

                        else:
                            print("Invalid input.")
                            continue

                    elif payment_car_choice == "N" or payment_car_choice == "n":
                        print("Redirecting you back to customer panel")
                        return
                    else:
                        print("Invalid input. Enter a correct choice.")
                        continue

        elif decision == '2':
            return
        else:
            print("Invalid input.")
            continue

###
#Registered Customer Panel
def registered_customerPanel(customerUsername1):
    while True:
        print("\nWhat would you like to do today?")
        print("=================================================")
        print("1. Modify personal details")
        print("2. View Personal Rental History")
        print("3. View Detail of Cars to be Rented Out")
        print("4. Select and Book a car for a specific duration")
        print("5. Do payment to confirm Booking")
        print("6. Exit")
        print("=================================================")

        registerCUS_input = input("Enter your choice: ")
        if registerCUS_input == "1":
            modify_details()
        elif registerCUS_input == "2":
            rental_history(customerUsername1)
        elif registerCUS_input == "3":
            cars_details()
        elif registerCUS_input == "4":
            select_book_car(customerUsername1)
        elif registerCUS_input == "5":
            payment(customerUsername1)
        elif registerCUS_input == "6":
            exit_panel()
            break
        else:
            print("Enter a value between 1 to 6.")
            continue

###
#Unregistered User Panel
def unregistered_customerPanel():
    while True:
        print("===================================")
        print("1. View cars available for rent")
        print("2. Register to access other details")
        print("3. Login now if you have an account")
        print("4. Return to login screen")
        print("5. Exit")
        print("===================================")
    
        unregisteredCUS_input = input("Enter your choice: ")
        if unregisteredCUS_input == "1":
            cars_available()
        elif unregisteredCUS_input == "2":
            register()
        elif unregisteredCUS_input == "3":
            customerUsername = userLogin()
            if customerUsername == None:
                return
            else:
                customerUsername1 = customerUsername
                print(f"Welcome {customerUsername1}!")
                registered_customerPanel(customerUsername1)
        elif unregisteredCUS_input == "4":
            return
        elif unregisteredCUS_input == "5":
            exit_panel()
            break
        else:
            print("Enter a value between 1 to 5")
            continue

###
# Exit panel
def exit_panel():
    # print something
    print("\nThank you for coming, See you again and have a great day.")

update_car_status() #Background Checking
update_car_rented() #Background Checking
login() # Start of code