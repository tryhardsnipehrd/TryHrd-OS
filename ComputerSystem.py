# My Libraries
import GoodLogin as login
import Calculator as calc
import OSGame
# External libraries
import arcade
import random

bank = {
    "holden":"hi"
}
cash = 1000
login.main(bank)
while True:
    print("Where would you like to go?")
    print("Calculator: 'Calculator'")
    print("Play a game from a list: 'Games'")
    print("Check Current Users: 'Users'")
    print("Log out or make a new account: 'Log Out'")
    place = input("")
    place = place.lower()
    if place == "calculator":
        calc.main()
    elif place == "games":
        OSGame.main(cash)
    elif place == "users":
        print(bank)
    elif place == "log out":
        login.main(bank)
    else:
        break

