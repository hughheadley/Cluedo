def make_person_info(personList, playerNames):
    # Return a table of what is known about all persons held by each player.
    # 7 columns, one for each person and one for player names.
    # One row for person names, one for every player and one more for solutions.
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
    personInfo[len(playerNames)+1][0] = "Solution"
    return personInfo

def make_weapon_info(weaponList, playerNames):
    # Return a table of what is known about all weapons held by each player.
    # 7 columns, one for each weapon and one for player names.
    # One row for weapon names, one for every player and one more for
    #solutions.
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
    weaponInfo[len(playerNames)+1][0] = "Solution"
    return weaponInfo

def make_room_info(roomList, playerNames):
    # Return a table of what is known about all rooms held by each player.
    # 9 columns, one for each room and one for player names.
    # One row for room names, one for every player and one more for solutions.
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
    roomInfo[len(playerNames)+1][0] = "Solution"
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

def get_starting_index(playerNames):
    nameValid = False
    while(not nameValid):
        startingPlayerName = raw_input("Who is first to play?")
        if(startingPlayerName in playerNames):
            nameValid = True
            startIndex = playerNames.index(startingPlayerName)
        else:
            print("Cannot find the name " + startingPlayerName)
            print("Choose from:")
            print(playerNames)
    return startIndex

def get_guess(personList, weaponList, roomList):
    # Find what player has asked. Return list with person, weapon, room.
    guess = [0]*3 # The indexes of the cards guessed.
    # Find the person.
    inputValid = False
    while(not inputValid):
        person = raw_input("What person was asked?")
        if(person == "quit"):
            return "quit"
        else:
            if(person in personList):
                guess[0] = personList.index(person)
                inputValid = True
            else:
                print("That isn't a valid person. Choose one from:")
                print(personList)
    # Find the weapon.
    inputValid = False
    while(not inputValid):
        weapon = raw_input("What weapon was asked?")
        if(weapon == "quit"):
            return "quit"
        else:
            if(weapon in weaponList):
                guess[1] = weaponList.index(weapon)
                inputValid = True
            else:
                print("That isn't a valid weapon. Choose one from:")
                print(weaponList)
    # Find the room.
    inputValid = False
    while(not inputValid):
        room = raw_input("What room was asked?")
        if(room == "quit"):
            return "quit"
        else:
            if(room in roomList):
                guess[2] = roomList.index(room)
                inputValid = True
            else:
                print("That isn't a valid room. Choose one from:")
                print(roomList)
    return guess

def guess_to_text(guess, personList, weaponList, roomList):
    guessText = ["","",""]
    guessText[0] = personList[guess[0]]
    guessText[1] = weaponList[guess[1]]
    guessText[2] = roomList[guess[2]]
    return guessText

def record_no_answer(guess, answerIndex, personInfo, weaponInfo, roomInfo):
    # Mark player's info to show that they didn't have any cards guessed.
    personInfo[answerIndex+1][guess[0]+1] = -1
    weaponInfo[answerIndex+1][guess[1]+1] = -1
    roomInfo[answerIndex+1][guess[2]+1] = -1

def follow_answers(
    guess, questionerIndex, playerNames, personList, weaponList, roomList,
    personInfo, weaponInfo, roomInfo):
    # After guess is made check answers given for card indications.
    # If someone has nothing to show then record in into tables.
    guessText = guess_to_text(guess, personList, weaponList, roomList)
    questioner = playerNames[questionerIndex]
    print(questioner + " has made a guess")
    print(guessText)
    numberPlayers = len(playerNames)
    answerIndex = ((questionerIndex+1) % numberPlayers)
    questioningActive = True
    while(questioningActive):
        # If answering reaches questioner then end answering.
        if(answerIndex == questionerIndex):
            questioningActive = False
        else:
            # If it is not me to answer then note if nothing is shown.
            answererName = playerNames[answerIndex]
            answer = raw_input("Did " + answererName + " show a card?")
            if(answer in ["0", "No", "no", "N", "n", ""]):
                record_no_answer(
                    guess, answerIndex, personInfo, weaponInfo, roomInfo)
            # If something was shown then end answering.
            else:
                questioningActive = False
            # Move to the next person.
            answerIndex = ((answerIndex+1) % numberPlayers)

def other_questioning(
    questionerIndex, playerNames, personList, weaponList, roomList, personInfo,
    weaponInfo, roomInfo):
        questioner = playerNames[questionerIndex]
        print("\n" + questioner + " is making a guess")
        guess = get_guess(personList, weaponList, roomList)
        # Check for the quit signal.
        if(guess == "quit"):
            return "quit"
        # Follow those players giving answers.
        follow_answers(guess, questionerIndex, playerNames, personList,
                     weaponList, roomList, personInfo, weaponInfo, roomInfo)
        return 0

def deduce_known_cards(infoTable, numberPlayers, numberCards):
    # Use deduction to find any known cards.
    improvements = False
    for card in range(0, numberCards):
        # Sum up all info values for this card.
        infoSum = 0
        for player in range(0, numberPlayers+1):
            infoSum += infoTable[player+1][card+1]
        # If all but one entries are -1 then card owner is known.
        if(infoSum == (-1*numberPlayers)):
            # An improvement in knowledge is made.
            improvements = True
            # Find who has card.
            cardOwner = 0
            for player in range(0, numberPlayers+1):
                if(infoTable[player+1][card+1] != -1):
                    cardOwner = player
                    add_card_seen(
                        cardOwner, infoTable, card, numberPlayers)
    return improvements

def count_known_cards(infoTable, numberPlayers, numberCards):
    # Count the number of cards known to be held by each player.
    cardsKnown = [0] * (numberPlayers+1)
    for player in range(0, numberPlayers+1):
        for card in range(0, numberCards):
            if(infoTable[player+1][card+1] == 1):
                cardsKnown[player] += 1
    return cardsKnown

def check_solution_cards(infoTable, numberPlayers, numberCards):
    # If a solution card is known then other cards are not the solution.
    # Search for a known solution.
    for card in range(0, numberCards):
        if(infoTable[numberPlayers+1][card+1] == 1):
            for nonSolution in range(0, numberCards):
                # For all cards that are not the solution set their information
                #equal to -1.
                if(nonSolution != card):
                    infoTable[numberPlayers+1][nonSolution+1] = -1

def update_info_table(infoTable, numberPlayers, numberCards):
    # Fill in missing information which is obvious from what is already known.
    # Return the number of cards of this types known to be held by each player.
    # Check if any cards' owners are known by deduction.
    improvements = deduce_known_cards(infoTable, numberPlayers, numberCards)
    # If a solution card is known then others of that type are known to be not
    #the solution.
    check_solution_cards(infoTable, numberPlayers, numberCards)
    return improvements

def update_information(personInfo, weaponInfo, roomInfo, numberPlayers):
    improvements = True
    while(improvements):
        # Repeat this check until no improvements in knowledge are made.
        personImprovements = update_info_table(personInfo, numberPlayers, 6)
        weaponImprovements = update_info_table(weaponInfo, numberPlayers, 6)
        roomImprovements = update_info_table(roomInfo, numberPlayers, 9)
        improvements = (personImprovements or weaponImprovements or
                        roomImprovements)

    cardsKnown = [0] * (numberPlayers+1)
    personCardsKnown = count_known_cards(personInfo, numberPlayers, 6)
    weaponCardsKnown = count_known_cards(weaponInfo, numberPlayers, 6)
    roomCardsKnown = count_known_cards(roomInfo, numberPlayers, 9)
    for player in range(0, numberPlayers+1):
        cardsKnown[player] = (personCardsKnown[player] +
                              weaponCardsKnown[player] +
                              roomCardsKnown[player])
    print("Updated info table")
    print(personInfo)
    print(weaponInfo)
    print(roomInfo)
    return cardsKnown

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

    # Begin the questioning.
    startIndex = get_starting_index(playerNames)
    gameOver = False
    questionerIndex = startIndex
    while(not gameOver):
        if(questionerIndex != 0):
            # If questioner is not me then record what is asked.
            quitSignal = other_questioning(
                questionerIndex, playerNames, personList, weaponList, roomList,
                personInfo,weaponInfo, roomInfo)
            if(quitSignal == "quit"):
                gameOver = True
        else:
            # If questioner is me then update info and compute best guess.
            update_information(personInfo, weaponInfo, roomInfo, numberPlayers)
        questionerIndex = ((questionerIndex + 1) % numberPlayers)
        
names = ["Me", "Alona", "Christian"]
play_cluedo(names)
