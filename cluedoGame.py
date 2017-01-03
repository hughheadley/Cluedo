def makePersonInfo(personList, playerNames):
    # Return a table of what is known about all persons held by each player.
    # 7 columns, one for each person and one for player names.
    # One row for person names, one for every playe and one more for answers.
    columnCount = len(personList) + 2
    rowCount = len(playerNames) + 3
    # Fill table with 0's to indicate no information.
    personInfo = [[0 for col in range(columnCount)] for row in range(rowCount)]
    # First row is persons names.
    print(personInfo)
    return personInfo        

def playCleudo(playerNames):
    # Play a game of Cluedo and suggest guesses.
    print("Name of those playing are:")
    for name in playerNames:
        print(name)
    numberPlayers = len(playerNames)
    # Create initial information lists.
    personList = ["Green", "Mustard", "Orchid", "Peacock" "Plum", "Scarlet"]
    personInfo = makePersonInfo(personList, playerNames)
    weaponInfo = makeWeaponInfo(numberPlayers)
    roomInfo = makeRoomInfo(numberPlayers)

names = ["Me", "Alona", "Christian"]
playCleudo(names)
