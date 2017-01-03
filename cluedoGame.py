def make_person_info(personList, playerNames):
    # Return a table of what is known about all persons held by each player.
    # 7 columns, one for each person and one for player names.
    # One row for person names, one for every player and one more for answers.
    columnCount = len(personList) + 1
    rowCount = len(playerNames) + 2
    # Fill table with 0's to indicate no information.
    personInfo = [[0 for col in range(columnCount)] for row in range(rowCount)]
    # First row is persons names.
    columnTitles = [""] + personList
    personInfo[0][:] = columnTitles
    # Second row is my cards, set all to -1 (not having the card).
    personInfo[1][:] = [-1 for person in range(columnCount)]
    # First column is player names.
    for i in range(1, 1+len(playerNames)):
        personInfo[i][0] = playerNames[i-1]
    personInfo[len(playerNames)+1][0] = "Answer"
    return personInfo

def make_weapon_info(weaponList, playerNames):
    # Return a table of what is known about all weapons held by each player.
    # 7 columns, one for each weapon and one for player names.
    # One row for weapon names, one for every player and one more for answers.
    columnCount = len(weaponList) + 1
    rowCount = len(playerNames) + 2
    # Fill table with 0's to indicate no information.
    weaponInfo = [[0 for col in range(columnCount)] for row in range(rowCount)]
    # First row is weapon names.
    columnTitles = [""] + weaponList
    weaponInfo[0][:] = columnTitles
    # Second row is my cards, set all to -1 (not having the card).
    weaponInfo[1][:] = [-1 for weapon in range(columnCount)]
    # First column is player names.
    for i in range(1, 1+len(playerNames)):
        weaponInfo[i][0] = playerNames[i-1]
    weaponInfo[len(playerNames)+1][0] = "Answer"
    return weaponInfo

def make_room_info(roomList, playerNames):
    # Return a table of what is known about all rooms held by each player.
    # 9 columns, one for each room and one for player names.
    # One row for room names, one for every player and one more for answers.
    columnCount = len(roomList) + 1
    rowCount = len(playerNames) + 2
    # Fill table with 0's to indicate no information.
    roomInfo = [[0 for col in range(columnCount)] for row in range(rowCount)]
    # First row is room names.
    columnTitles = [""] + roomList
    roomInfo[0][:] = columnTitles
    # Second row is my cards, set all to -1 (not having the card).
    roomInfo[1][:] = [-1 for room in range(columnCount)]
    # First column is player names.
    for i in range(1, 1+len(playerNames)):
        roomInfo[i][0] = playerNames[i-1]
    roomInfo[len(playerNames)+1][0] = "Answer"
    return roomInfo

def add_card_seen(shownBy, infoTable, cardIndex, numberPlayers):
    # Update information table with new seen card.
    # shownBy is the index of the person showing the cards as in the
    #playerNames list.
    # cardIndex is the index of the card in the person/weapon/room list.
    # Put 1 in table to indicate who has card.
    infoTable[shownBy+1][cardIndex+1] = 1
    # Put -1 in table to indicate who doesn't have card.
    for player in range(0, numberPlayers + 1):
        if(player != shownBy):
            infoTable[player+1][cardIndex+1] = -1

def get_my_cards(
    personList, weaponList, roomList, personInfo, weaponInfo, roomInfo,
    numberPlayers):
    cardShown = ""
    while cardShown is not "0":
        cardShown = raw_input("\nTell me my next card \n")
        cardIndex = -1
        myIndex = 0
        if cardShown in personList:
            cardIndex = personList.index(cardShown)
            add_card_seen(myIndex, personInfo, cardIndex, numberPlayers)
        elif cardShown in weaponList:
            cardIndex = weaponList.index(cardShown)
            add_card_seen(myIndex, weaponInfo, cardIndex, numberPlayers)
        elif cardShown in roomList:
            cardIndex = roomList.index(cardShown)
            add_card_seen(myIndex, roomInfo, cardIndex, numberPlayers)
        else:
            if(cardShown != "0"):
                print("\nWarning, card named " + cardShown + " not found\n")

def play_cluedo(playerNames):
    # Play a game of Cluedo and suggest guesses.
    print("Name of those playing are:")
    for name in playerNames:
        print(name)
    numberPlayers = len(playerNames)
    # Create initial information lists.
    personList = ["Green", "Mustard", "Orchid", "Peacock", "Plum", "Scarlet"]
    personInfo = make_person_info(personList, playerNames)
    weaponList = ["Candlestick", "Dagger", "Lead pipe", "Revolver", "Rope",
                  "Wrench"]
    weaponInfo = make_weapon_info(weaponList, playerNames)
    roomList = ["Ballroom", "Billiard", "Conservatory", "Dining", "Hall",
                "Kitchen", "Library", "Lounge", "Study"]
    roomInfo = make_room_info(roomList, playerNames)

    # Add my cards to the tables of information.
    get_my_cards(
        personList, weaponList, roomList, personInfo, weaponInfo, roomInfo,
        numberPlayers)

names = ["Me", "Alona", "Christian"]
play_cluedo(names)
