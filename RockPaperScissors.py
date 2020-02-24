def main():
    import random
    rps = ["rock", "paper", "scissors"]
    
    print("What do you choose?")
    rps2 = random.choice(rps)
    arg = input("")
    arg = arg.lower()
    print(f"I chose {rps2} and you chose {arg}")
    if arg == "scissors":
        if rps2 == "scissors":
            print("We tied...")
        elif rps2 == "paper":
            print("Y-You beat me...")
        elif rps2 == "rock":
            print("I win again!!!")