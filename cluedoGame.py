from __future__ import print_function, division
import random
import math
import copy

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

def print_info_table(infoTable, numberPlayers, numberCards):
    # Print an infoTable in a legible form.
    # Find the number of tabs required for each column to remain alligned.
    columnTabs = [0]*(numberCards+1)
    # Find the longest name.
    maxNameLength = 0
    for i in range(numberPlayers+2):
        nameLength = len(infoTable[i][0])
        if(nameLength > maxNameLength):
            maxNameLength = nameLength
    columnTabs[0] = math.ceil(maxNameLength/4)
    # Find the number of tabs to equal each column heading.
    for col in range(1, numberCards+1):
        columnTabs[col] = math.ceil(len(infoTable[0][col])/4)
    for i in range(numberPlayers+2):
        for j in range(numberCards+1):
            print(str(infoTable[i][j]), end='')
            # Compute tabs needed.
            tabs = int(columnTabs[j] - math.ceil(len(str(infoTable[i][j]))/4) + 1)
            for k in range(tabs):
                print("\t", end='')
        print("\n", end='')

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
        startingPlayerName = raw_input("\nWho is first to play?\n")
        if(startingPlayerName in playerNames):
            nameValid = True
            startIndex = playerNames.index(startingPlayerName)
        else:
            print("Cannot find the name " + startingPlayerName)
            print("Choose from:")
            print(playerNames)
    return startIndex

def get_guess(personList, weaponList, room):
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
    # Set the room.
    guess[2] = room
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

def print_many_lines(numLines = 38):
    for i in range(numLines):
        print("")

def check_to_show_card(guess, personInfo, weaponInfo, roomInfo):
    # Check my cards to see what can be shown.
    guessPersonIndex = guess[0]
    guessWeaponIndex = guess[1]
    guessRoomIndex = guess[2]
    answer = "N"
    # Prefer to show weapon then person then room.
    if(weaponInfo[1][guessWeaponIndex+1] == 1):
        print_many_lines()
        print("Show weapon:", weaponInfo[0][guessWeaponIndex+1])
        temp = raw_input("Enter anything to continue")
        answer = "Y"
    elif(personInfo[1][guessPersonIndex+1] == 1):
        print_many_lines()
        print("Show person:", personInfo[0][guessPersonIndex+1])
        temp = raw_input("Enter anything to continue")
        answer = "Y"
    elif(roomInfo[1][guessRoomIndex+1] == 1):
        print_many_lines()
        print("Show room:", roomInfo[0][guessRoomIndex+1])
        temp = raw_input("Enter anything to continue")
        answer = "Y"
    else:
        print("I have nothing to show you")
        print_many_lines()
        temp = raw_input("Enter anything to continue")
    return answer

def follow_answers(
    guess, questionerIndex, playerNames, personList, weaponList, roomList,
    personInfo, weaponInfo, roomInfo):
    # After guess is made check answers given for card indications.
    # If someone has nothing to show then record in into tables.
    guessText = guess_to_text(guess, personList, weaponList, roomList)
    questioner = playerNames[questionerIndex]
    print("\n" + questioner + " has made a guess")
    print(guessText)
    numberPlayers = len(playerNames)
    answerIndex = ((questionerIndex+1) % numberPlayers)
    questioningActive = True
    while(questioningActive):
        # If answering reaches questioner then end answering.
        if(answerIndex == questionerIndex):
            questioningActive = False
        else:
            answererName = playerNames[answerIndex]
            answer = "N"
            if(answerIndex == 0):
                answer = check_to_show_card(guess, personInfo, weaponInfo,
                                            roomInfo)
            else:
                answer = raw_input("Did " + answererName + " show a card?")
            # Note if nothing is shown by somebody.
            if(answer in ["0", "No", "no", "N", "n", ""]):
                record_no_answer(guess, answerIndex, personInfo, weaponInfo,
                                 roomInfo)
                # Move to the next person.
                answerIndex = ((answerIndex+1) % numberPlayers)
            # If something was shown then end answering.
            else:
                questioningActive = False
    return answerIndex

def other_questioning(
    questionerIndex, playerNames, personList, weaponList, roomList, personInfo,
    weaponInfo, roomInfo, memories):
    questioner = playerNames[questionerIndex]
    print("\n" + questioner + " is making a guess")
    inputValid = False
    nonRoomOptions = ["0", "None", "none", "No", "no", "N", "n", ""]
    while(not inputValid):
        room = raw_input("What room is " + questioner + " in?")
        if(room == "quit"):
            return "quit"
        elif(room in nonRoomOptions):
            print("\n" + questioner + " has skipped their turn")
            return "none"
        elif(room in roomList):
            inputValid = True
        else:
            print("That isn't a valid room. Choose one from:")
            print(roomList)
    roomIndex = roomList.index(room)
    guess = get_guess(personList, weaponList, roomIndex)
    # Follow those players giving answers.
    answerIndex = follow_answers(guess, questionerIndex, playerNames,
                                 personList, weaponList, roomList,
                                 personInfo, weaponInfo, roomInfo)
    # Record memory if it was answered not by me.
    validMemory = (answerIndex != 0) and (answerIndex != "none")
    if(validMemory):
        memory = [0]*4
        memory[0] = answerIndex
        memory[1] = guess[0]
        memory[2] = guess[1]
        memory[3] = guess[2]
        memories.append(memory)
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

def get_candidate_cards(infoTable, unknownCards):
    # Fill in table with the number of cards which could correspond to each
    #option.
    numberPlayers = len(unknownCards)-1
    numberCards = len(infoTable[0][:])-1
    candidateTable = [[0 for col in range(numberCards+1)]
                      for row in range(numberPlayers+2)]
    # Put titles into candidateTable.
    candidateTable[0][:] = infoTable[0][:]
    candidateTable[:][0] = infoTable[:][0]
    # Calculate candidate cards for players.
    for player in range(numberPlayers+1):
        for card in range(numberCards):
            if(infoTable[player+1][card+1] == -1):
                # If card is known to not be owned then there are no cards.
                candidateTable[player+1][card+1] = 0
            elif(infoTable[player+1][card+1] == 1):
                # If card is known to be owned then there is one card.
                candidateTable[player+1][card+1] = 1
            else:
                # If card is not known about then it could be any of this
                #player's unknown cards.
                candidateTable[player+1][card+1] = unknownCards[player]
    return candidateTable

def get_option_weights(candidateTable, numberPlayers):
    # Compute a list with the weights of each card as the solution.
    numberCards = len(candidateTable[0][:])-1
    weights = [0.0]*numberCards
    for card in range(numberCards):
        solutionCandidates = candidateTable[numberPlayers+1][card+1]
        sumCandidates = 0
        for player in range(numberPlayers+1):
            sumCandidates += candidateTable[player+1][card+1]
        if(sumCandidates==0):
            # sumCandidates==0 only occurs when examining an impossible
            #outcome of questioning.
            # This only happens when card is not the solution. Therefore
            #weight is 0.
            weights[card] = 0
        else:
            weights[card] = (solutionCandidates/sumCandidates)
    return weights

def get_option_probabilities(weights):
    # Convert weighted options into probabilities.
    weightsSum = sum(weights)
    if(weightsSum == 0):
        # If weightsSum is zero then no options are possible, this is
        #due to an impossible outcome of the questioning being
        #considered.
        probabilities = [0]*len(weights)
    else:
        probabilities = [(weight/weightsSum) for weight in weights]
    return probabilities

def distribution_information(probabilities):
    # Compute the information of a discrete distribution.
    informationSum = 0
    for i in range(len(probabilities)):
        if(probabilities[i] > 0):
            informationSum += -1*(probabilities[i]*math.log(probabilities[i]))
    return informationSum

def compute_information(
    personInfo, weaponInfo, roomInfo, unknownCards, numberPlayers):
    # Compute the information of the distribution of the game's solution.
    # Higher information indicates that less is known about the solution.
    # Compute table of candidate cards.
    personCandidates = get_candidate_cards(personInfo, unknownCards)
    # Compute weights list of possible solutions.
    personWeights = get_option_weights(personCandidates, numberPlayers)
    # Compute probability of possible solutions.
    personProbs = get_option_probabilities(personWeights)
    # Compute information.
    personInformation = distribution_information(personProbs)
    
    # Repeat computation for weapon.
    weaponCandidates = get_candidate_cards(weaponInfo, unknownCards)
    # Compute weights list of possible solutions.
    weaponWeights = get_option_weights(weaponCandidates, numberPlayers)
    # Compute probability of possible solutions.
    weaponProbs = get_option_probabilities(weaponWeights)
    # Compute information.
    weaponInformation = distribution_information(weaponProbs)
    
    # Repeat computation for room.
    roomCandidates = get_candidate_cards(roomInfo, unknownCards)
    # Compute weights list of possible solutions.
    roomWeights = get_option_weights(roomCandidates, numberPlayers)
    # Compute probability of possible solutions.
    roomProbs = get_option_probabilities(roomWeights)
    # Compute information.
    roomInformation = distribution_information(roomProbs)
    
    totalInformation = personInformation + weaponInformation + roomInformation
    return totalInformation

def rank_informations(
    personCardInformation, weaponCardInformation, roomCardInformation):
    # Sort card type by the information it gives.
    cardType = ["person", "weapon", "room"]
    informations = [personCardInformation, weaponCardInformation,
                    roomCardInformation]
    # High information means that less is known, the player showing cards
    #prefers to show one with a high information.
    preference = [""]*3
    for i in range(3):
        # Find highest info.
        maxInfo = max(informations)
        # Find index of largest info.
        maxIndex = informations.index(maxInfo)
        # Put this into preferenceTemp in order.
        preference[i] = cardType[maxIndex]
        # Replace max with a negative number.
        # Information is always non-negative.
        informations[maxIndex] = -1
    return preference

def find_first_show(infoTable, cardIndex, numberPlayers):
    # Find which player can first show card.
    # Check if I have card.
    if(infoTable[1][cardIndex+1] == 1):
        firstShow = 0
        return firstShow
    # Search other players for someone who can show.
    for player in range(1, numberPlayers):
        if(infoTable[player+1][cardIndex+1] != -1):
            # If player isn't known to not have card then they can show.
            firstShow = player
            return firstShow
    # If noboy was found then card is the solution.
    firstShow = numberPlayers
    return firstShow

def card_shown_preference(
    guess, personInfo, weaponInfo, roomInfo, numberPlayers, unknownCards):
    # Find which card the first player would prefer to show.
    # The first player will show whichever card gives the least information.
    # Make copy tables of information.
    personInfoCopy = copy.deepcopy(personInfo)
    weaponInfoCopy = copy.deepcopy(weaponInfo)
    roomInfoCopy = copy.deepcopy(roomInfo)
    
    # Find modify table as if each card is shown by first possible player.
    whoShowsPerson = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsPerson, personInfoCopy, guess[0], numberPlayers)
    update_info_table(personInfoCopy, numberPlayers, 6)
    whoShowsWeapon = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsWeapon, weaponInfoCopy, guess[1], numberPlayers)
    update_info_table(weaponInfoCopy, numberPlayers, 6)
    whoShowsRoom = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsRoom, roomInfoCopy, guess[2], numberPlayers)
    update_info_table(roomInfoCopy, numberPlayers, 9)

    # Find information after each possible card shown.
    personCardInformation = compute_information(personInfoCopy, weaponInfo,
                                                roomInfo, unknownCards,
                                                numberPlayers)
    weaponCardInformation = compute_information(personInfo, weaponInfoCopy,
                                                roomInfo, unknownCards,
                                                numberPlayers)
    roomCardInformation = compute_information(personInfo, weaponInfo,
                                                roomInfoCopy, unknownCards,
                                                numberPlayers)
    cardPreference = rank_informations(
    personCardInformation, weaponCardInformation, roomCardInformation)
    return cardPreference

def get_conditional_prob(
    candidatesTable, playerShowing, cardIndex, prefModifier, numberPlayers,
    numberCards, unknownCards):
    # Calculate the chance of playerShowing showing the card cardIndex
    #given that nobody before them showed anything.
    # showingCards is the number of cards held by the player showing
    #which could be the card asked.
    showingCards = candidatesTable[playerShowing+1][cardIndex+1]
    # solutionCards are the number of cards in the solution which could
    #be the card asked.
    solutionCards = candidatesTable[numberPlayers+1][cardIndex+1]
    # allPlayersCards are the number of cards not belonging to the
    #solution which could be the card asked.
    allPlayersCards = 0
    for player in range(playerShowing, numberPlayers):
        allPlayersCards += candidatesTable[player+1][cardIndex+1]
    # remainingPlayerCards are the number of cards belonging to those
    #players after the one showing.
    remainingPlayerCards = (allPlayersCards - showingCards)
    # Subtract a modifier according to how many preferences have passed.
    # If 2 preferences have passed then 2 cards must belong to the
    #remaining players.
    if(remainingPlayerCards < prefModifier):
        modifiedRemaining = 0
    else:
        modifiedRemaining = remainingPlayerCards - prefModifier
    realTotalCandidates = (showingCards + modifiedRemaining
                           + solutionCards)
    ##realTotalCandidates = allPlayersCandidates - candidatesAdjustment
    ##denominator = max(realTotalCandidates, playerShowingCandidates)
    if(realTotalCandidates > 0):
        conditionalProb = (showingCards/realTotalCandidates)
    else:
        # If there are no candidates then I have the card.
        conditionalProb = 0
    if(conditionalProb > 1):
        print("Warning conditional prob is greater than 1")
        print("candidates table:\n", candidatesTable)
        print("cardIndex", cardIndex)
        print("playerShowing", playerShowing)
        print("prefModifier", prefModifier)
    if(conditionalProb < 0):
        print("Warning conditional prob is less than 0")
        print("candidates table:\n", candidatesTable)
        print("cardIndex", cardIndex)
        print("playerShowing", playerShowing)
        print("prefModifier", prefModifier)
    return conditionalProb

def get_outcome_probabilities(
    guess, preferences, personInfo, weaponInfo, roomInfo, unknownCards):
    # Find the probability of every possible card shown after guessing.
    # 3 outcomes for every other player and 1 outcome of nobody showing.    
    personCandidates = get_candidate_cards(personInfo, unknownCards)
    weaponCandidates = get_candidate_cards(weaponInfo, unknownCards)
    roomCandidates = get_candidate_cards(roomInfo, unknownCards)
    numberPlayers = len(unknownCards)-1
    numberOutcomes = (3*numberPlayers)-2
    # conditionalProbs is the probability of an outcome given than all
    #prior outcomes have not happened.
    conditionalProbs = [0]*numberOutcomes
    preferenceModifiers = [0]*3
    for player in range(1, numberPlayers):
        preferenceModifiers = [0]*3
        for cardType in range(3):
            if(preferences[cardType] == "person"):
                candidatesTable = personCandidates
                cardIndex = guess[0]
                numberCards = 6
                # If I don't have this card then increase
                #preferenceModifiers.
                if(personInfo[1][guess[0]+1] == -1):
                    for i in range(cardType+1, 3):
                        preferenceModifiers[i] += 1
            elif(preferences[cardType] == "weapon"):
                candidatesTable = weaponCandidates
                cardIndex = guess[1]
                numberCards = 6
                # If I don't have this card then increase
                #preferenceModifiers.
                if(weaponInfo[1][guess[1]+1] == -1):
                    for i in range(cardType+1, 3):
                        preferenceModifiers[i] += 1
            else:
                candidatesTable = roomCandidates
                cardIndex = guess[2]
                numberCards = 9
                # If I don't have this card then increase
                #preferenceModifiers.
                if(roomInfo[1][guess[2]+1] == -1):
                    for i in range(cardType+1, 3):
                        preferenceModifiers[i] += 1
            preferenceIndex = cardType
            outcomeIndex = 3*(player-1) + cardType
            prefModifier = preferenceModifiers[cardType]
            conditionalProbs[outcomeIndex] = get_conditional_prob(candidatesTable, player,
                                                    cardIndex, prefModifier,
                                                    numberPlayers, numberCards,
                                                    unknownCards)
    # The conditional probability of nobody showing is 1.
    conditionalProbs[numberOutcomes-1] = 1.0
    # Find actual probabilities from conditional probabilities.
    probabilities = [0]*numberOutcomes
    cumulativeProb = 0
    for i in range(0, numberOutcomes):
        probabilities[i] = (1-cumulativeProb)*conditionalProbs[i]
        cumulativeProb += probabilities[i]
    return probabilities

def get_outcome_informations(
    guess, preferences, personInfo, weaponInfo, roomInfo, numberPlayers,
    unknownCards):
    # Compute the information after every outcome of cards shown.
    numberOutcomes = (3*numberPlayers)-2
    # conditionalProbs is the probability of an outcome given than all
    #prior outcomes have not happened.
    outcomeInformations = [0]*numberOutcomes
    # Make tables with all information from previous cards not shown.
    personUnshownInfo = copy.deepcopy(personInfo)
    weaponUnshownInfo = copy.deepcopy(weaponInfo)
    roomUnshownInfo = copy.deepcopy(roomInfo)

    # For each outcome find information after card shown.
    for player in range(1, numberPlayers):
        for cardType in range(3):
            outcomeIndex = 3*(player-1) + cardType
            # Make tables with info from all previous players not
            #showing anything.
            currentPersonInfo = copy.deepcopy(personUnshownInfo)
            currentWeaponInfo = copy.deepcopy(weaponUnshownInfo)
            currentRoomInfo = copy.deepcopy(roomUnshownInfo)
            # Update table for case of showing this card type.
            if(preferences[cardType] == "person"):
                add_card_seen(player, currentPersonInfo, guess[0],
                              numberPlayers)
            elif(preferences[cardType] == "weapon"):
                add_card_seen(player, currentWeaponInfo, guess[1],
                              numberPlayers)
            else:
                add_card_seen(player, currentRoomInfo, guess[2], numberPlayers)
            # Deduce information from this card shown.
            update_information(currentPersonInfo, currentWeaponInfo,
                               currentRoomInfo, numberPlayers)
            # Find information of updated tables.
            newInformation = compute_information(currentPersonInfo,
                                                     currentWeaponInfo,
                                                     currentRoomInfo,
                                                     unknownCards,
                                                     numberPlayers)
            outcomeInformations[outcomeIndex] = newInformation
        # Update information tables as if player didn't show anything.
        record_no_answer(guess, player, personUnshownInfo, weaponUnshownInfo,
                         roomUnshownInfo)
    # Find the final information if nobody showed anything.
    update_information(personUnshownInfo, weaponUnshownInfo, roomUnshownInfo,
                       numberPlayers)
    newInformation = compute_information(personUnshownInfo, weaponUnshownInfo,
                                         roomUnshownInfo, unknownCards,
                                         numberPlayers)
    outcomeInformations[numberOutcomes-1] = newInformation
    return outcomeInformations

def average_information(probabilities, informations):
    # Average the information over all outcomes.
    numberOutcomes = len(probabilities)
    informationSum = 0
    for outcome in range(numberOutcomes):
        informationSum += (probabilities[outcome] * informations[outcome])
    return informationSum

def evaluate_guess(
    guess, personInfo, weaponInfo, roomInfo, numberPlayers, unknownCards):
    # Compute the expected information from all possible outcomes of
    #questioning.
    # Find the preference of cards shown to me.
    preferences = card_shown_preference(guess, personInfo, weaponInfo,
                                        roomInfo, numberPlayers, unknownCards)
    # Find the probability of each outcome of a guess.
    probabilities = get_outcome_probabilities(guess, preferences, personInfo,
                                              weaponInfo, roomInfo,
                                              unknownCards)
    # Find the information under each outcome.
    informations = get_outcome_informations(guess, preferences, personInfo,
                                            weaponInfo, roomInfo,
                                            numberPlayers, unknownCards)
    # Average the information over all outcomes.
    expectedInformation = average_information(probabilities, informations)
    return expectedInformation

def find_best_guess(
    personInfo, weaponInfo, roomInfo, myRoom, numberPlayers, unknownCards):
    # Compute the guess which maximises the expected information gained.
    # Find the current information of the solution cards.
    currentInformation = compute_information(personInfo, weaponInfo, roomInfo,
                                              unknownCards, numberPlayers)
    # Loop through all possible guesses. Find guess giving lowest
    #information.
    bestGuesses = []
    bestGuessPerformance = 100
    roomList = roomInfo[0][1:10]
    guessRoom = roomList.index(myRoom)
    for person in range(6):
        for weapon in range(6):
            guessPerson = person
            guessWeapon = weapon
            guess = [guessPerson, guessWeapon, guessRoom]
            performance = evaluate_guess(guess, personInfo, weaponInfo,
                                        roomInfo, numberPlayers, unknownCards)
            if(performance < bestGuessPerformance):
                # If this is better than all previous guesses then remove
                #previous guesses and append current guess.
                bestGuesses = []
                bestGuesses.append(guess)
                bestGuessPerformance = performance
            elif(performance == bestGuessPerformance):
                # If this is as good as the best found so far then
                #append this guess as an option to ask.
                bestGuesses.append(guess)
    # Choose randomly from all bestGuesses options.
    numberOptions = len(bestGuesses)
    randomInt = random.randint(0, numberOptions-1)
    bestGuess = bestGuesses[randomInt]
    return bestGuess

def follow_responses(guess, playerNames, personInfo, weaponInfo, roomInfo):
    # After I make a guess check responses given for card indications.
    # If someone has nothing to show then record into tables.
    personList = personInfo[0][1:7]
    weaponList = weaponInfo[0][1:7]
    roomList = roomInfo[0][1:10]
    guessText = guess_to_text(guess, personList, weaponList, roomList)
    questionerIndex = 0
    print("I have made a guess")
    print(guessText)
    numberPlayers = len(playerNames)
    answerIndex = 1
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
            else:
                cardInvalid = True
                while cardInvalid:
                    cardShown = raw_input("What card was shown?")
                    if cardShown in personList:
                        cardIndex = personList.index(cardShown)
                        add_card_seen(answerIndex, personInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    elif cardShown in weaponList:
                        cardIndex = weaponList.index(cardShown)
                        add_card_seen(answerIndex, weaponInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    elif cardShown in roomList:
                        cardIndex = roomList.index(cardShown)
                        add_card_seen(answerIndex, roomInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    else:
                        print("\nWarning, card named " + cardShown +
                              " not found\n")
                    # If something was shown then end answering.
                    questioningActive = False
                # Move to the next person.
            answerIndex = ((answerIndex+1) % numberPlayers)

def use_memories(personInfo, weaponInfo, roomInfo, memories, numberPlayers):
    memoryCount = len(memories)
    # Use previously answered questions to discover extra cards.
    print("All memories", memories)
    for i in range(memoryCount):
        answerIndex = memories[i][0]
        person = memories[i][1]
        weapon = memories[i][2]
        room = memories[i][3]
        if(personInfo[answerIndex+1][person+1] == -1):
            personOwned = 0
        else:
            personOwned = 1
        if(weaponInfo[answerIndex+1][weapon+1] == -1):
            weaponOwned = 0
        else:
            weaponOwned = 1
        if(roomInfo[answerIndex+1][room+1] == -1):
            roomOwned = 0
        else:
            roomOwned = 1
        # If two of the three cards are not owned then the third must have
        #been shown.
        if((personOwned + weaponOwned) == 0):
            add_card_seen(answerIndex, roomInfo, room, numberPlayers)
        elif((personOwned + roomOwned) == 0):
            add_card_seen(answerIndex, weaponInfo, weapon, numberPlayers)
        elif((roomOwned + weaponOwned) == 0):
            add_card_seen(answerIndex, personInfo, person, numberPlayers)
        print("personOwned",personOwned)
        print("weaponOwned",weaponOwned)
        print("roomOwned",roomOwned)
        print(personInfo)
        print(weaponInfo)
        print(roomInfo)

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
    return cardsKnown

def get_my_room(questionMessage, roomList, nonRoomOptions):
    nameValid = False
    while(not nameValid):
        myRoom = raw_input(questionMessage)
        isRoom = myRoom in roomList
        isNonRoom = myRoom in nonRoomOptions
        if(isRoom):
            nameValid = True
        elif(isNonRoom):
            nameValid = True
            myRoom = "none"
        else:
            print("Cannot find the name " + myRoom)
            print("Choose from:")
            print(roomList)
    return myRoom

def show_room_preference(roomInfo, unknownCards):
    # Show the order of rooms which are best to go to.
    numberPlayers = len(unknownCards)-1
    roomCandidates = get_candidate_cards(roomInfo, unknownCards)
    # Compute weights list of possible solutions.
    roomWeights = get_option_weights(roomCandidates, numberPlayers)
    # Compute probability of possible solutions.
    roomProbs = get_option_probabilities(roomWeights)
    roomList = roomInfo[0][1:10]
    
    # Sort a list of rooms by decreasing probability.
    tempRooms = [0]*9
    roomProbsTemp = [0]*9
    for i in range(9):
        maxProb = max(roomProbs)
        bestRoomIndex = roomProbs.index(maxProb)
        tempRooms[i] = roomList[bestRoomIndex]
        roomProbsTemp[i] = round(roomProbs[bestRoomIndex], 2)
        # Prevent this room from being the max again
        roomProbs[bestRoomIndex] = -1
    print(tempRooms)
    print(roomProbsTemp)

def get_rooms_in_reach(myRoom, roll, roomList, roomTravelDistance):
    # Return a list of indices of rooms which can be reached with this
    #dice roll.
    roomIndex = roomList.index(myRoom)
    reachableRooms = []
    for i in range(len(roomList)):
        if(roomTravelDistance[roomIndex][i] <= roll):
            # Append the index of a room if it can be reached.
            reachableRooms.append(i)
    return reachableRooms

def get_room_performance(
    guessRoom, personInfo, weaponInfo, roomInfo, numberPlayers, unknownCards):
    bestGuessPerformance = 100
    for person in range(6):
        for weapon in range(6):
            guessPerson = person
            guessWeapon = weapon
            guess = [guessPerson, guessWeapon, guessRoom]
            performance = evaluate_guess(guess, personInfo, weaponInfo,
                                         roomInfo, numberPlayers,
                                         unknownCards)
            if(performance < bestGuessPerformance):
                bestGuess = guess
                bestGuessPerformance = performance
    return bestGuessPerformance

def find_indirect_route(
    currentRoom, reachableRooms, personInfo, weaponInfo, roomInfo,
    unknownCards, effectiveDistance):
    # Move towards the best room, move to a closer room if possible.
    roomPerformances = []
    # Find performance of every room.
    for room in range(9):
        performance = get_room_performance(room, personInfo, weaponInfo,
                                           roomInfo, numberPlayers,
                                           unknownCards)
        roomPerformances.append(performance)
        
    # Find the closest of the rooms with best performance.
    bestPerformance = min(roomPerformances)
    shortestTravel = 100
    bestPerformers = []
    closestBestRoom = currentRoom
    for room in range(9):
        isBestPerformance = (roomPerformances[room] == bestPerformance)
        isCloser = (effectiveDistance[currentRoom][room] < shortestTravel)
        if(isBestPerformance and isCloser):
            closestBestRoom = room
            shortestTravel = effectiveDistance[currentRoom][room]

    # Check if I can move to any room that is closer to the closest
    #best room.
    travelFromCurrent = effectiveDistance[currentRoom][closestRoom]
    closerRoomPossible = False
    closerRoom = "none"
    for i in range(len(reachableRooms)):
        room = reachableRooms[i]
        travelFromRoom = effectiveDistance[room][closestRoom]
        if(travelFromRoom < travelFromCurrent):
            closerRoomPossible = True
            closerRoom = room
    if(closerRoom == "None"):
        # If all reachable rooms are farther from the closestBestRoom
        #then ask to move towards it through the corridor.
        print("Move towards " , closestBestRoom)
    print("find_indirect_route returns ", closerRoom)
    return closerRoom

def decide_room_movement(
    currentInformation, reachableRooms, personInfo, weaponInfo, roomInfo,
    unknownCards, numberPlayers):
    roomList = roomInfo[0][1:10]
    moveToRoom = 5
    # Considering possible information gain choose a room to move to.
    print("I can reach rooms")
    for i in range(len(reachableRooms)):
        print(roomList[reachableRooms[i]])
    # For all reachable rooms check the information that can be gained
    #from asking a question in that room.
    roomPerformances = []
    for i in range(len(reachableRooms)):
        guessRoom = reachableRooms[i]
        performance = get_room_performance(guessRoom, personInfo, weaponInfo,
                                    roomInfo, numberPlayers, unknownCards)
        roomPerformances.append(performance)
    # If any of the reachable rooms create information then go to best.
    bestPerformance = min(roomPerformances)
    if(bestPerformance < currentInformation):
        # The best room allows to get information better than current.
        reachableRoomIndex = roomPerformances.index(bestPerformance)
        moveToRoomIndex = reachableRooms[reachableRoomIndex]
        moveToRoom = roomList[moveToRoomIndex]
    else:
        moveToRoomIndex = find_indirect_route(currentRoom, reachableRooms,
                                         personInfo, weaponInfo, roomInfo,
                                         unknownCards, effectiveDistance)
        moveToRoom = roomList[moveToRoomIndex]
    print("decide_room_movement returns ", moveToRoom)
    return moveToRoom

def make_movement(
    personInfo, weaponInfo, roomInfo, currentInformation, unknownCards,
    roomEffectiveDistance, roomTravelDistance):
    # Decide which room to move to next.
    roomList = roomInfo[0][1:10]
    numberPlayers = len(unknownCards)-1
    show_room_preference(roomInfo, unknownCards)
    questionMessage = "\nWhat room am I in?"
    nonRoomOptions = ["0", "None", "none", "No", "no", "N", "n", ""]
    myRoom = get_my_room(questionMessage, roomList, nonRoomOptions)
    roll = 0
    if(myRoom == "none"):
        # If in corridor try to move to the room I was previously going
        #towards.
        print("Keep moving towards the room I was trying to get to")
        corridorInput = raw_input("Am I still in the corridor?")
        inCorridorEntries = ["y", "Y", "yes", "Yes", "1"]
        if not(corridorInput in inCorridorEntries):
            # Check if I rolled enough to get to target room.
            questionMessage = "\nWhat room am I in now?"
            newRoom = get_my_room(questionMessage, roomList, nonRoomOptions)
        else:
            # Skip this turn to ask a question.
            newRoom = "none"
    else:
        rollString = raw_input("How much did I roll?\n")
        roll = int(rollString)
        reachableRooms = get_rooms_in_reach(myRoom, roll, roomList,
                                            roomTravelDistance)
        newRoom = decide_room_movement(currentInformation, reachableRooms,
                                       personInfo, weaponInfo, roomInfo,
                                       unknownCards, numberPlayers)
    # Announce where I'm moving.
    if(newRoom != "none"):
        print("\nMove to", newRoom, "\n")
    return newRoom

def make_accusation(personInfo, weaponInfo, roomInfo, numberPlayers):
    # Find the solution and announce it.
    solutionPersonInfo = personInfo[numberPlayers+1][:]
    # The correct person has an info value of 1.
    personIndex = solutionPersonInfo.index(1)
    print("The killer was", personInfo[0][personIndex])
          
    solutionWeaponInfo = weaponInfo[numberPlayers+1][:]
    # The correct weapon has an info value of 1.
    weaponIndex = solutionWeaponInfo.index(1)
    print("with the", weaponInfo[0][weaponIndex])
          
    solutionRoomInfo = roomInfo[numberPlayers+1][:]
    # The correct person has an info value of 1.
    roomIndex = solutionRoomInfo.index(1)
    print("in the", roomInfo[0][roomIndex])
    temp = raw_input("Was I correct?")

def me_questioning(
    personInfo, weaponInfo, roomInfo, playerNames, initialCards, memories,
    useMemory):
    # Update information and make a guess.
    numberPlayers = len(playerNames)
    unknownCards = [0]*(numberPlayers+1)
    if(useMemory):
        use_memories(personInfo, weaponInfo, roomInfo, memories, numberPlayers)
    knownCards = update_information(
        personInfo, weaponInfo, roomInfo, numberPlayers)    
    # Find number of unknown cards.
    for i in range(numberPlayers):
        unknownCards[i] = initialCards[i] - knownCards[i]
    # Set solution unknownCards to 1 because only 1 card is ever relevant.
    unknownCards[numberPlayers] = 1
    
    # Compare current information with uninformed information level.
    uninformed = (2 * math.log(6)) + math.log(9)    
    currentInformation = compute_information(personInfo, weaponInfo, roomInfo,
                                              unknownCards, numberPlayers)
    percentComplete = int(100 * (1 - (currentInformation / uninformed)))
    print("\n\nCurrently", percentComplete, "percent complete\n")
    if(currentInformation == 0):
        make_accusation(personInfo, weaponInfo, roomInfo, numberPlayers)

    # Decide which room to go to.
    roomList = roomInfo[0][1:10]
    questionMessage = "\nWhat room am I in?"
    nonRoomOptions = ["0", "None", "none", "No", "no", "N", "n", ""]
    #myRoom = get_my_room(questionMessage, roomList, nonRoomOptions)
    myRoom = make_movement(personInfo, weaponInfo, roomInfo,
                           currentInformation, unknownCards,
                           roomEffectiveDistance, roomTravelDistance)
    
    # Make a guess and record answers.
    if(myRoom != "none"):
        guess = find_best_guess(personInfo, weaponInfo, roomInfo,
                                myRoom, numberPlayers, unknownCards)
        follow_responses(guess, playerNames, personInfo, weaponInfo, roomInfo)

def get_initial_cards(playerNames):
    # Get the initial number of cards that each person has.
    numberPlayers = len(playerNames)
    # Check if cards can be equally dealt.
    if((18/numberPlayers) == int(18/numberPlayers)):
        # All players have the same number of cards.
        initialCards = [int(18/numberPlayers)]*numberPlayers
    else:
        # Deal out cards.
        initialCards = [0]*numberPlayers
        startDealName = raw_input("Who was dealt to first?\n")
        startDealIndex = playerNames.index(startDealName)
        for i in range(18):
            initialCards[(startDealIndex+i)%numberPlayers] += 1
    return initialCards

def play_cluedo(
    playerNames, personList, weaponList, roomList, expectedDistance,
    travelDistance, useMemory=False):
    # Play a game of Cluedo and suggest guesses.
    print("Names of those playing are:")
    for name in playerNames:
        print(name)
    numberPlayers = len(playerNames)
    initialCards = get_initial_cards(playerNames)
    # Create initial information lists.
    personInfo = make_person_info(personList, playerNames)
    weaponInfo = make_weapon_info(weaponList, playerNames)
    roomInfo = make_room_info(roomList, playerNames)

    # Add my cards to the tables of information.
    get_my_cards(personList, weaponList, roomList, personInfo, weaponInfo,
                 roomInfo, numberPlayers)
    memories = []

    # Begin the questioning.
    startIndex = get_starting_index(playerNames)
    gameOver = False
    questionerIndex = startIndex
    while(not gameOver):
        if(questionerIndex != 0):
            # If questioner is not me then record what is asked.
            quitSignal = other_questioning(questionerIndex, playerNames,
                                           personList, weaponList, roomList,
                                           personInfo, weaponInfo, roomInfo,
                                           memories)
            if(quitSignal == "quit"):
                gameOver = True
        else:
            print(personInfo)
            print(weaponInfo)
            print(roomInfo)
            me_questioning(personInfo, weaponInfo, roomInfo, playerNames,
                           initialCards, memories, useMemory)
        questionerIndex = ((questionerIndex + 1) % numberPlayers)

names = ["Ellie", "Alona", "Christian"]
personList = ["Green", "Mustard", "Orchid", "Peacock", "Plum", "Scarlet"]
weaponList = ["Candlestick", "Dagger", "Lead pipe", "Revolver", "Rope",
              "Wrench"]
roomList = ["Ballroom", "Billiard", "Conservatory", "Dining", "Hall",
            "Kitchen", "Library", "Lounge", "Study"]
roomEffectiveDistance = [[0,6,5,7,15,7,12,12,14],[6,0,6,14,15,17,4,13,16],
                         [5,6,0,11,15,19,17,0,19],[7,14,11,0,8,11,14,4,17],
                         [15,15,15,8,0,17,7,8,10],[7,17,19,11,17,0,14,19,0],
                         [12,4,17,14,7,14,0,14,7],[12,13,0,4,8,19,14,0,17],
                         [14,16,19,17,10,0,7,17,0]]
roomTravelDistance = [[0,6,5,7,15,7,12,15,17],[6,0,6,14,15,17,4,22,15],
                      [5,6,0,18,19,19,13,0,19],[7,14,18,0,8,11,14,4,17],
                      [15,15,19,8,0,19,7,8,10],[7,17,19,11,19,0,23,19,0],
                      [12,4,13,14,7,23,0,14,7],[15,22,0,4,8,19,14,0,17],
                      [17,15,19,17,10,0,7,17,0]]
useMemory = True
play_cluedo(names, personList, weaponList, roomList, roomEffectiveDistance,
            roomTravelDistance, useMemory)
