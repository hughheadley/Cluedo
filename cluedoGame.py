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

def get_candidate_cards(infoTable, unknownCards):
    # Fill in table with the number of cards which could correspond to each
    #option.
    numberPlayers = len(unknownCards)
    numberCards = len(infoTable[0][:])-1
    candidateTable = [[0 for col in range(numberCards+1)]
                      for row in range(numberPlayers+2)]
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
                candidateTable[player+1][card+1] = unknownCards[player-1]
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
        weights[card] = (solutionCandidates/sumCandidates)
    return weights

def get_option_probabilities(weights):
    # Convert weighted options into probabilities.
    weightsSum = sum(weights)
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
    guess, personInfo, weaponInfo, roomInfo, numberPlayers, unknownCards,
    currentInformation):
    # Find which card the first player would prefer to show.
    # The first player will show whichever card gives the least information.
    # Make copy tables of information.
    personInfoCopy = copy.deepcopy(personInfo)
    weaponInfoCopy = copy.deepcopy(weaponInfo)
    roomInfoCopy = copy.deepcopy(roomInfo)
    # Find modify table as if each card is shown by first possible player.
    whoShowsPerson = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsPerson, personInfoCopy, guess[0], numberPlayers)
    deduce_known_cards(personInfoCopy, numberPlayers, 6)
    whoShowsWeapon = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsWeapon, weaponInfoCopy, guess[1], numberPlayers)
    deduce_known_cards(weaponInfoCopy, numberPlayers, 6)
    whoShowsRoom = find_first_show(personInfoCopy, guess[0], numberPlayers)
    add_card_seen(whoShowsRoom, roomInfoCopy, guess[2], numberPlayers)
    deduce_known_cards(roomInfoCopy, numberPlayers, 9)
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
        print("preferenceIndex", preferenceIndex)
    if(conditionalProb < 0):
        print("Warning conditional prob is less than 0")
        print("candidates table:\n", candidatesTable)
        print("cardIndex", cardIndex)
        print("playerShowing", playerShowing)
        print("preferenceIndex", preferenceIndex)
    return conditionalProb

def get_outcome_probabilities(
    guess, preferences, personInfo, weaponInfo, roomInfo, unknownCards):
    # Find the probability of every possible card shown after guessing.
    # 3 outcomes for every other player and 1 outcome of nobody showing.    
    personCandidates = get_candidate_cards(personInfo, unknownCards)
    weaponCandidates = get_candidate_cards(weaponInfo, unknownCards)
    roomCandidates = get_candidate_cards(roomInfo, unknownCards)
    numberPlayers = len(unknownCards)
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
    print("Probabilities", probabilities)
    return probabilities

def find_best_guess(
    personInfo, weaponInfo, roomInfo, myRoom, numberPlayers, unknownCards):
    # Compute the guess which maximises the expected information gained.
    # Find the current information of the solution cards.
    currentInformation = compute_information(personInfo, weaponInfo, roomInfo,
                                              unknownCards, numberPlayers)
    
    # Until better algorithm is made use a random guess.
    guessPerson = random.randint(0,5)
    guessWeapon = random.randint(0,5)
    roomList = roomInfo[0][1:10]
    guessRoom = roomList.index(myRoom)
    guess = [guessPerson, guessWeapon, guessRoom]
    
    # Find the preference of cards shown to me.
    preferences = card_shown_preference(guess, personInfo, weaponInfo,
                                        roomInfo, numberPlayers, unknownCards,
                                        currentInformation)
    # Find the probability of each outcome of a guess.
    get_outcome_probabilities(guess, preferences, personInfo, weaponInfo,
                              roomInfo, unknownCards)
    return guess

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
                    cardIndex = -1
                    myIndex = 0
                    if cardShown in personList:
                        cardIndex = personList.index(cardShown)
                        add_card_seen(myIndex, personInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    elif cardShown in weaponList:
                        cardIndex = weaponList.index(cardShown)
                        add_card_seen(myIndex, weaponInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    elif cardShown in roomList:
                        cardIndex = roomList.index(cardShown)
                        add_card_seen(myIndex, roomInfo, cardIndex,
                                      numberPlayers)
                        cardInvalid = False
                    else:
                        print("\nWarning, card named " + cardShown +
                              " not found\n")
                    # If something was shown then end answering.
                    questioningActive = False
                # Move to the next person.
            answerIndex = ((answerIndex+1) % numberPlayers)

def me_questioning(
    personInfo, weaponInfo, roomInfo, playerNames, initialCards):
    # Update information and make a guess.
    numberPlayers = len(playerNames)
    unknownCards = [0]*(numberPlayers)
    knownCards = update_information(
        personInfo, weaponInfo, roomInfo, numberPlayers)    
    # Find number of unknown cards.
    for i in range(1, numberPlayers):
        unknownCards[i-1] = initialCards[i-1] - knownCards[i-1]
    # Set solution unknownCards to 1 because only 1 card is ever relevant.
    unknownCards[numberPlayers-1] = 1

    # Make a guess and record answers.
    myRoom = raw_input("\nWhat room am I in?")
    if(not (myRoom in ["0", "None", "none", "No", "no", "N", "n", ""])):
        guess = find_best_guess(personInfo, weaponInfo, roomInfo, myRoom,
                                numberPlayers, unknownCards)
        follow_responses(guess, playerNames, personInfo, weaponInfo, roomInfo)

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
    print_info_table(personInfo, numberPlayers, 6)
    print_info_table(weaponInfo, numberPlayers, 6)
    print_info_table(roomInfo, numberPlayers, 9)
    return cardsKnown

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

def play_cluedo(playerNames):
    # Play a game of Cluedo and suggest guesses.
    print("Names of those playing are:")
    for name in playerNames:
        print(name)
    numberPlayers = len(playerNames)
    initialCards = get_initial_cards(playerNames)
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
                personInfo, weaponInfo, roomInfo)
            if(quitSignal == "quit"):
                gameOver = True
        else:
            me_questioning(
                personInfo, weaponInfo, roomInfo, playerNames, initialCards)
        questionerIndex = ((questionerIndex + 1) % numberPlayers)

names = ["Me", "Alona", "Christian"]
play_cluedo(names)
