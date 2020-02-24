def main(cash):
    import slots
    print("Casino")
    print("Slots: 'slots'")
    place = input("")
    place = place.lower()
    if place == "slots":
        slots.main(cash)
        return(cash)