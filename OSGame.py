def main(money):
    import RockPaperScissors as rps
    import Casino
    print("What would you like to play?")
    print("Rock Paper Scissors: 'rps'")
    print("Casino Simulator 1970: 'casino'")
    game = input('')
    game = game.lower()
    if game == "rps":
        rps.main()
    if game == "casino":
        Casino.main(money)
        return(money)