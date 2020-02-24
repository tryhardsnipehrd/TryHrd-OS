def main(place):
    
    create = True
    while create:
        print("Do you have an account? Y/N")
        confirm = input("")
        confirm = confirm.lower()
        if confirm != "y":
            # Creates a Username and password
            print("What would you like your Username to be?")
            username = input()
            print("What would you like your password to be?")
            password = input()
            # Tells the Username and password
            print("Your Username is:")
            print(username)
            print("Your Password is:")
            print(password)
            # Adds the Pair to the "bank" dictionary, linked together
            place[username] = password
            log_in = True
            while log_in:
                # Starts the login Sequence
                print("Login Sequence initiated...")
                print("What is your username?")
                username2 = input()
                # Sees if the Username is valid
                if username2 in place:
                    password_attempt = True
                    while password_attempt:
                        # Gets the password
                        print("What is your password?")
                        password2 = input()
                        # Checks if the password matches the username
                        if password2 == place.get(username2):
                            print("Login succesful")
                            break

                        if password2 != place.get(username2):
                            print("")
                    # Asks if user wants to make a new account.
                    print("Would you like to create a new account? Y/N")
                    confirm = input()
                    if confirm == "Y":
                        password_attempt = False
                        log_in = False

                    elif confirm == "y":
                        log_in = False
                        password_attempt = False

                    else:            
                        create = False
                        log_in = False
                        break
        else:
            log_in = True
            while log_in:
                # Starts the login Sequence
                print("Login Sequence initiated...")
                print("What is your username?")
                username2 = input()
                # Sees if the Username is valid
                if username2 in place:
                    password_attempt = True
                    while password_attempt:
                    # Gets the password
                        print("What is your password?")
                        password2 = input()
                        # Checks if the password matches the username
                        if password2 == place.get(username2):
                            print("Login succesful")
                            break

                        if password2 != place.get(username2):
                            print("")
                    # Asks if user wants to make a new account.
                    print("Would you like to create a new account? Y/N")
                    confirm = input()
                    if confirm == "Y":
                        password_attempt = False
                        log_in = False

                    elif confirm == "y":
                        log_in = False
                        password_attempt = False

                    else:            
                        create = False
                        log_in = False
                        break