def await_user_confirmation():
    option = input("Would you like to continue (Y/n)? ")
    
    if option.strip().lower() != "y" and option.strip().lower() != "yes":
        print("Exiting program...")
        exit(0)
    