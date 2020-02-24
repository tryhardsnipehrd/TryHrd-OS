def main(money):
    slot1 = {"Heart", "Diamond", "Spade", "Club"}
    slot2 = {"Heart", "Diamond", "Spade", "Club"}
    slot3 = {"Heart", "Diamond", "Spade", "Club"}
    print(f"How much would you like to bet? You have ${money} remaining")
    amount = int(input(""))
    money = money - amount
    print(money)

    return(money)