import itertools
from random import randint 
import random
import operator
from operator import itemgetter 
import os

still = True
debug = False
run = False

while still == True:
    run = False 
    print("")
    print ("**********")
    print ("q = quit")
    print ("r = run")
    print ("d = debug")
    print ("**********")
    _in = input(":")
    if _in == "q":
        break
    if _in == "d":
        if debug == True:
            debug = False
            print("Debug: False")
        else:
            debug = True
            print("Debug: True")
    if _in == "r":
        run = True
    if _in == "cs":
        #clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

    if run == True:
        appearedCards = []
        appearedHands = []
        PlayerAppCards = []
        O1AppCards = []
        O2AppCards = []
        O3AppCards = []
        currentHand = []
        currentCard = []
        suits = ["S", "H", "C", "D"]
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        YorN = False
        suitAns = False
        curValue = 0
        runNums = 300
        maxNumOfPlayers = 4
        enterCards = False


        numOfPlayers = 0
        print("How Many Times To Run?")
        times = input(":")
        while times.isdigit() == False:
            times = input(":")
        runNums = int(times)
        print("Enter num of Players 1-4")
        while numOfPlayers <= 0 or numOfPlayers > maxNumOfPlayers:
            numOfPlayers = int(input(":"))





        def AddCardsToHand(hand, target):
            for card in hand:
                target.append(card)


        def createCardHand(card):
            card = [random.choice(values), random.choice(suits)]  
            for cards in appearedCards:
                if card[0] == cards[0] and card[1] == cards[1]:
                    card = [random.choice(values), random.choice(suits)]
            appearedCards.append(card)
            return card

        def createCard(card):
            card = [random.choice(values), random.choice(suits)]  
            for cards in appearedCards:
                if card[0] == cards[0] and card[1] == cards[1]:
                    card = [random.choice(values), random.choice(suits)]
            return card
            
        def checkSuit(suit, ans):
            Str = False
            ans = False
            while ans == False or Str == False:
                if suit.isdigit():
                    Str = False
                else:
                    Str = True
                if suit == "H":
                    ans = True
                elif suit == "D":
                    ans = True
                elif suit == "C":
                    ans = True
                elif suit == "S":
                    ans = True
                else:
                    print("INVALID")
                    suit = str(input(":"))
            return suit


        def checkValue(cardValue):
            print("Choose card num")
            cardValue = int(input(":"))
            while cardValue <= 1 or cardValue >= 15:
                cardValue = int(input(":"))

        def checkforpair(hand, pairs):
            NumOfPairs = 0
            for card in hand:
                for cards in hand:
                    if card[1] != cards[1]:
                        if card[0] == cards[0]:
                            NumOfPairs += 1
            if NumOfPairs >= pairs:
                return True

        def howManyPairs(hand):
            numOfPair = 0
            for card in hand:
                for cards in hand:
                        if card[1] != cards[1]:
                            if card[0] == cards[0]:
                                numOfPair += 1
                            
            if numOfPair >= 2:
                if (numOfPair % 2) == 0:
                    return numOfPair
                elif numOfPair == 1: 
                    return numOfPair
                else:
                    return numOfPair -1 
        def checkflush(hand):
            numOfStraights = 0
            heartTotal = 0
            spadesTotal = 0
            clubsTotal = 0
            diamondsTotal = 0
            for card in hand:
                if card[1] == "H":
                    heartTotal += 1
                elif card[1] == "S":
                    spadesTotal +=1
                elif card[1] == "D":
                    diamondsTotal +=1
                elif card[1] == "C":
                    clubsTotal +=1
            if heartTotal >= 5 or clubsTotal >= 5 or diamondsTotal >= 5 or spadesTotal >= 5:
                numOfStraights += 1
                return numOfStraights


        def find3Pairs(hand):
            num = 0
            for card in hand:
                for cards in hand:
                    if cards != card:
                        for evcard in hand:
                            if card != cards:
                                if card != evcard:
                                    if cards != evcard:
                                        if card[0] == cards[0] and card[0] == evcard[0] and cards[0] == evcard[0]:
                                            num = 1          
            return num
                

        def find4Pairs(hand):
            num = 0
            for card in hand:
                for cards in hand:
                    for evcard in hand:
                        for fincards in hand:
                            if card != fincards and cards != fincards and evcard != fincards and card != cards and card != evcard and cards != evcard:
                                if card[0] == cards[0] == evcard[0] == fincards[0]: #and card[0] == evcard[0] and cards[0] == evcard[0] and fincards[0] == evcard[0] and  fincards[0] == card and fincards[0] == cards[0]:
                                    num = 1       
            return num
                            
        def findAllPairs(hand):
            appeareed = False
            appearedPairs = []
            appearedCard = []
            Pairs = []
            curPair = []
            for card in hand:
                appeareed = False
                for cards in hand:
                    if card != cards:
                        if card[0] == cards[0]:
                            curPair = [card, cards]
                            appearedPairs.append(curPair)
                            for cards in appearedCard:
                                for card in curPair:
                                    if card == cards:
                                        appeareed = True
                            if appeareed != True:
                                Pairs.append(curPair)
                                for card in curPair:
                                    appearedCard.append(card)
                                appearedPairs.append(curPair)
            if len(Pairs) >= 1:
                return Pairs 
            else:
                return Pairs
                                    


        def findAllThreePairs(hand):
            appeareed = False
            appearedPairs = []
            appearedCard = []
            Pairs = []
            curPair = []
            for card in hand:
                appeareed = False
                for cards in hand:
                    if card != cards:
                        for evcard in hand:
                            if card != evcard:
                                if cards != evcard:
                                    if card[0] == cards[0] == evcard[0]:
                                        curPair = [card, cards, evcard]
                                        appearedPairs.append(curPair)
                                        for cards in appearedCard:
                                            for card in curPair:
                                                if card == cards:
                                                    appeareed = True
                                        if appeareed != True:
                                            Pairs.append(curPair)
                                            for card in curPair:
                                                appearedCard.append(card)
                                            appearedPairs.append(curPair)
            if len(Pairs) >= 1:
                return Pairs 
            else:
                return Pairs

        def findFull(threePairs, twoPairs):
            if threePairs >= 1 and  twoPairs >= 2:
                return 1
            else:
                return 0 
        
            
        def getInpCard(card):
            print("Choose card num")
            card = [int(input(":"))]
            while card[0] <= 1 or card[0] >= 15:
                card[0] = int(input(":"))
                if isinstance(card, str):
                    card[0] = int(input(":"))
            print("Enter suit")
            curSuit = input(":")
            checkSuit(curSuit, suitAns)
            card = [card[0], curSuit]
            appearedCards.append(playerCard1)
            return card

        def getStraight(hand):
            Values = []
            finalVals = []
            nextVal = 0
            numOfSame = 0
            maxValue = 0
            curValue = 0
            prevSame = False
            i = 0
            for card in hand:
                Values.append(card[0])
            finalVals = sorted(Values)
            for i in range(len(finalVals) - 1):
                if(finalVals[i] == finalVals[i + 1]):
                    numOfSame = numOfSame
                    prevSame = True
                elif prevSame == True and finalVals[i - 1] == (finalVals[i + 1] - 1) or prevSame == True and finalVals[i] == (finalVals[1 + 1] - 1) or  prevSame == True and finalVals[i - 2] == (finalVals[i + 1] - 1) or prevSame == True and finalVals[i - 3] == (finalVals[i + 1] - 1):
                    numOfSame += 1 
                    curValue += 1
                    if maxValue <= curValue:
                        maxValue = curValue
                    prevSame = False
                elif finalVals[i] == (finalVals[i + 1] - 1):
                    numOfSame += 1 
                    curValue += 1
                    if maxValue <= curValue:
                        maxValue = curValue
                    prevSame = False
                elif finalVals[i] != (finalVals[i + 1] - 1):
                    numOfSame = 0
                    curValue = 0
                    prevSame = False
            if maxValue >= 4:
                return 1 
            else: 
                return 0


        def getStraightFlush(hand):
            Values = []
            finalVals = []
            nextVal = 0
            numOfSame = 0
            maxValue = 0
            curValue = 0
            i = 0
            prevSame = False
            for card in hand:
                Values.append(card)
            finalVals = sorted(Values, key= itemgetter(0))
            for i in range(len(finalVals) - 1):
                if(finalVals[i][0] == finalVals[i + 1][0]):
                    numOfSame = numOfSame
                    prevSame = True
                elif prevSame == True and (finalVals[i - 1][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 1][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i][0] == (finalVals[i + 1][0] - 1) and finalVals[i][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i - 2][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 2][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i - 3][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 3][1] == finalVals[i + 1][1]):         
                    numOfSame += 1
                    curValue += 1
                    if maxValue <= curValue:
                        maxValue = curValue
                    prevSame = False
                elif finalVals[i][0] == (finalVals[i + 1][0] - 1) and finalVals[i][1] == finalVals[i + 1][1]:
                
                    numOfSame += 1
                    curValue += 1
                    if maxValue <= curValue:
                        maxValue = curValue
                    prevSame = False
                elif finalVals[i][0] != (finalVals[i + 1][0] - 1) or finalVals[i][1] != finalVals[i + 1][1]:
                
                    numOfSame = 0
                    curValue = 0
                    prevSame = False
            if maxValue >= 4:
                return 1 
            else: 
                return 0

        def FindRoyalFlush(hand):
            Values = []
            finalVals = []
            nextVal = 0
            numOfSame = 0
            maxValue = 0
            curValue = 0
            i = 0
            prevSame = False
            for cards in hand:
                if cards[0] == 10:
                    for card in hand:
                        Values.append(card)
                    finalVals = sorted(Values, key= itemgetter(0))
                    for i in range(len(finalVals) - 1):
                        if(finalVals[i][0] == finalVals[i + 1][0]):
                            numOfSame = numOfSame
                            prevSame = True
                        elif prevSame == True and (finalVals[i - 1][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 1][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i][0] == (finalVals[i + 1][0] - 1) and finalVals[i][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i - 2][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 2][1] == finalVals[i + 1][1]) or prevSame == True and (finalVals[i - 3][0] == (finalVals[i + 1][0] - 1) and finalVals[i - 3][1] == finalVals[i + 1][1]):         
                            numOfSame += 1
                            curValue += 1
                            if maxValue <= curValue:
                                maxValue = curValue
                            prevSame = False
                        elif finalVals[i][0] == (finalVals[i + 1][0] - 1) and finalVals[i][1] == finalVals[i + 1][1]:
                        
                            numOfSame += 1
                            curValue += 1
                            if maxValue <= curValue:
                                maxValue = curValue
                            prevSame = False
                        elif finalVals[i][0] != (finalVals[i + 1][0] - 1) or finalVals[i][1] != finalVals[i + 1][1]:
                        
                            numOfSame = 0
                            curValue = 0
                            prevSame = False
            if maxValue >= 4:
                return 1 
            else: 
                return 0


        playerCard1 = []
        playerCard2 = []
        playerCard3 = []
        playerCard4 = []
        playerCard5 = []




        playerCard1 = createCardHand(playerCard1)
        playerCard2 = createCardHand(playerCard2)
        playerCard3 = createCardHand(playerCard3)
        playerCard4 = createCardHand(playerCard4)
        playerCard5 = createCardHand(playerCard5)

        print("Enter Own Card")
        fin = input(":")
        still = False
        Str = False
        Val = 0
        while still == False or Str == False :
            if fin.isdigit():
                print("INVALID")
                print("Enter own card")
                fin = input(":")
            else:
                Str = True
            if fin == "Y":
                still = True
                YorN = True
            elif fin == "N":
                still = True
                YorN = False

            else:
                print("INVALID")
                print("Enter own card")
                fin = input(":")


        if YorN == True:
            playerCard1 = getInpCard(playerCard1)
            playerCard2 = getInpCard(playerCard2)
            playerCard3 = getInpCard(playerCard3)
            playerCard4 = getInpCard(playerCard4)
            playerCard5 = getInpCard(playerCard5)

        totalPairs = 0
        total2Pairs = 0
        total3Pairs = 0
        total4Pairs = 0
        totalFlush = 0
        totalHouse = 0
        totalStraights = 0
        totalStraightFlush = 0
        totalRoyalFlush = 0


        O1totalPairs = 0
        O1total2Pairs = 0
        O1total3Pairs = 0
        O1total4Pairs = 0
        O1totalFlush = 0
        O1totalHouse = 0
        O1totalStraights = 0
        O1totalStraightFlush = 0
        O1totalRoyalFlush = 0

        O2totalPairs = 0
        O2total2Pairs = 0
        O2total3Pairs = 0
        O2total4Pairs = 0
        O2totalFlush = 0
        O2totalHouse = 0
        O2totalStraights = 0
        O2totalStraightFlush = 0
        O2totalRoyalFlush = 0

        O3totalPairs = 0
        O3total2Pairs = 0
        O3total3Pairs = 0
        O3total4Pairs = 0
        O3totalFlush = 0
        O3totalHouse = 0
        O3totalStraights = 0
        O3totalStraightFlush = 0
        O3totalRoyalFlush = 0

        myTotalVictories = 0
        O1TotalVictories = 0
        O2TotalVictories = 0
        O3TotalVictories = 0
        MyDraws = 0
        TotalDraws = 0

        myCurBestHand = 0
        O1CurBestHand = 0
        O2CurBestHand = 0
        O3CurBestHand = 0



        PlayerHand = [playerCard1, playerCard2, playerCard3, playerCard4, playerCard5]
        print(PlayerHand)
        O1Hand = []
        O2Hand = []
        O3Hand = []

        for i in range(runNums): #182
            appearedCards.clear()
            PlayerAppCards.clear()
            O1AppCards.clear()
            O2AppCards.clear()
            O3AppCards.clear()

            if numOfPlayers >= 2:
                O1Card1 = []
                O1Card2 = []
                O1Card3 = []
                O1Card4 = []
                O1Card5 = []
                O1Card1 = createCardHand(O1Card1)
                O1Card2 = createCardHand(O1Card2)
                O1Card3 = createCardHand(O1Card3)
                O1Card4 = createCardHand(O1Card4)
                O1Card5 = createCardHand(O1Card5)
                O1Hand = [O1Card1, O1Card2, O1Card3, O1Card4, O1Card5]
                AddCardsToHand(O1Hand, appearedCards)
                AddCardsToHand(O1Hand, O1AppCards)
            if numOfPlayers >= 3:
                O2Card1 = []
                O2Card2 = []
                O2Card3 = []
                O2Card4 = []
                O2Card5 = []
                O2Card1 = createCardHand(O2Card1)
                O2Card2 = createCardHand(O2Card2)
                O2Card3 = createCardHand(O2Card3)
                O2Card4 = createCardHand(O2Card4)
                O2Card5 = createCardHand(O2Card5)
                O2Hand = [O2Card1, O2Card2, O2Card3, O2Card4, O2Card5]
                AddCardsToHand(O2Hand, appearedCards)
                AddCardsToHand(O2Hand, O2AppCards)
            if numOfPlayers == 4:
                O3Card1 = []
                O3Card2 = []
                O3Card3 = []
                O3Card4 = []
                O3Card5 = []
                O3Card1 = createCardHand(O3Card1)
                O3Card2 = createCardHand(O3Card2)
                O3Card3 = createCardHand(O3Card3)
                O3Card4 = createCardHand(O3Card4)
                O3Card5 = createCardHand(O3Card5)
                O3Hand = [O3Card1, O3Card2, O3Card3, O3Card4, O3Card5]
                AddCardsToHand(O3Hand, appearedCards)
                AddCardsToHand(O3Hand, O3AppCards)
            AddCardsToHand(PlayerHand, appearedCards)
            AddCardsToHand(PlayerHand, PlayerAppCards)
            currentHand.clear()

            
            for i in range(4):
                currentCard.clear()
                card=[]
                card = createCardHand(card)
                PlayerAppCards.append(card)
                O1AppCards.append(card)
                O2AppCards.append(card)
                O3AppCards.append(card)
            if debug == True:
                if numOfPlayers >= 2:
                    print("O1:")
                    print(O1AppCards)
                if numOfPlayers >= 3:
                    print("O2:")
                    print(O2AppCards)
                if numOfPlayers >= 4:
                    print("O3:")
                    print(O3AppCards)
                print("Player:")
                print(PlayerAppCards)

            myAllPairNums = 0
            myTwoPairNums = 0
            myPairNums = 0
            myThreePairNum = 0
            myFourPairNum = 0
            myFlushNum = 0
            myFullHouseNum = 0
            myStraightNum = 0
            myStraightFlushNum = 0
            myRoyalFlushNum = 0
            myPairs = []

            myPairs = findAllPairs(PlayerAppCards)
            myThreePairNum = findAllThreePairs(PlayerAppCards)
            myThreePairNum = find3Pairs(PlayerAppCards)
            myFourPairNum = find4Pairs(PlayerAppCards)
            myAllPairNums = len(findAllPairs(PlayerAppCards))
            if debug == True:
                print ("AllPairNums - " +str(myAllPairNums))
            if myAllPairNums != 0:
                myPairNums = 1

            if myAllPairNums == 2:
                myTwoPairNums = 1
            elif myAllPairNums == 3:
                myTwoPairNums = 1
            elif myAllPairNums == 4:
                myTwoPairNums = 1
            elif myAllPairNums == 0: 
                myPairNums = 0
                myTwoPairNums = 0

            if myAllPairNums != 0:
                totalPairs += myPairNums
                total2Pairs += myTwoPairNums
                total3Pairs += myThreePairNum
                total4Pairs += myFourPairNum
                if debug == True:
                    print("Pairs - "+str(myPairNums))
                    print("2Pairs - "+str(myTwoPairNums))
                    print("Three of a kind - "+str(myThreePairNum))
                    print("Four of a kind - "+str(myFourPairNum))
            else:
                if debug == True:
                    print("Pairs - 0")
                    print("2Pairs - 0")
                    print("Three of a kind - 0")
                    print("Four of a kind - 0")

            myStraightNum = getStraight(PlayerAppCards)
            if(debug == True):
                print("Straights - " +str(myStraightNum))
            totalStraights += myStraightNum

            myFlushNum = checkflush(PlayerAppCards)
            if myFlushNum == None:
                myFlushNum = 0
            totalFlush += myFlushNum
            if debug == True:
                print("Flushes - " +str(myFlushNum))
                
        
            myFullHouseNum = findFull(myThreePairNum, myAllPairNums)
            totalHouse +=myFullHouseNum
            if debug == True:
                print ("Full houses - " +str(myFullHouseNum))

            myStraightFlushNum = getStraightFlush(PlayerAppCards)
            if debug == True:
                print("Straight Flushes - " +str(myStraightFlushNum))
            totalStraightFlush += myStraightFlushNum

            
            myRoyalFlushNum = FindRoyalFlush(PlayerAppCards)
            if debug == True:
                print("Royal Flushes - " +str(myRoyalFlushNum))
            totalRoyalFlush += myRoyalFlushNum

            myCurBestHand = 0
            if myPairNums == 1:
                myCurBestHand = 1
            if myTwoPairNums == 1:
                myCurBestHand = 2
            if myThreePairNum == 1:
                myCurBestHand = 3
            if  myStraightNum == 1:
                myCurBestHand == 4
            if myFlushNum == 1:
                myCurBestHand = 5
            if myFullHouseNum == 1:
                myCurBestHand = 6
            if myFourPairNum == 1:
                myCurBestHand = 7
            if myStraightFlushNum == 1:
                myCurBestHand = 8
            if myRoyalFlushNum == 1:
                myCurBestHand = 9
            if debug == True:
                print("Best Hand Value - " +str(myCurBestHand))

            if(numOfPlayers >= 2):     
                O1AllPairNums = 0
                O1TwoPairNums = 0
                O1PairNums = 0
                O1ThreePairNum = 0
                O1FourPairNum = 0
                O1FlushNum = 0
                O1FullHouseNum = 0
                O1StraightNum = 0
                O1StraightFlushNum = 0
                O1RoyalFlushNum = 0
                O1Pairs = []

                O1Pairs = findAllPairs(O1AppCards)
                O1ThreePairNum = findAllThreePairs(O1AppCards)
                O1ThreePairNum = find3Pairs(O1AppCards)
                O1FourPairNum = find4Pairs(O1AppCards)
                O1AllPairNums = len(findAllPairs(O1AppCards))
                #print ("AllPairNums - " +str(O1AllPairNums))
                if O1AllPairNums != 0:
                    O1PairNums = 1

                if O1AllPairNums == 2:
                    O1TwoPairNums = 1
                elif O1AllPairNums == 3:
                    O1TwoPairNums = 1
                elif O1AllPairNums == 4:
                    O1TwoPairNums = 1
                elif O1AllPairNums == 0: 
                    O1PairNums = 0
                    O1TwoPairNums = 0

                if O1AllPairNums != 0:
                    O1totalPairs += O1PairNums
                    O1total2Pairs += O1TwoPairNums
                    O1total3Pairs += O1ThreePairNum
                    O1total4Pairs += O1FourPairNum
                    #print("O1 Pairs - "+str(O1PairNums))
                    #print("O1 2Pairs - "+str(O1TwoPairNums))
                    #print("O1 Three of a kind - "+str(O1ThreePairNum))
                    #print("O1 Four of a kind - "+str(O1FourPairNum))
                #else:
                # print("O1 Pairs - 0")
                    #print("O1 2Pairs - 0")
                    #print("O1 Three of a kind - 0")
                    #print("O1 Four of a kind - 0")

                O1StraightNum = getStraight(O1AppCards)
                #print("O1 Straights - " +str(O1StraightNum))
                O1totalStraights += O1StraightNum

                O1FlushNum = checkflush(O1AppCards)
                if O1FlushNum == None:
                    O1FlushNum = 0
                O1totalFlush += O1FlushNum
                #print("O1 FLushes - " +str(O1FlushNum))
                    
            
                O1FullHouseNum = findFull(O1ThreePairNum, O1AllPairNums)
                O1totalHouse += O1FullHouseNum
                #print ("O1 Full houses - " +str(O1FullHouseNum))

                O1StraightFlushNum = getStraightFlush(O1AppCards)
                #print("O1 Straight Flushes - " +str(O1StraightFlushNum))
                O1totalStraightFlush += O1StraightFlushNum

                
                O1RoyalFlushNum = FindRoyalFlush(O1AppCards)
                #print("O1 Royal Flushes - " +str(O1RoyalFlushNum))
                O1totalRoyalFlush += O1RoyalFlushNum

                O1CurBestHand = 0
                if O1PairNums == 1:
                    O1CurBestHand = 1
                if O1TwoPairNums == 1:
                    O1CurBestHand = 2
                if O1ThreePairNum == 1:
                    O1CurBestHand = 3
                if  O1StraightNum == 1:
                    O1CurBestHand == 4
                if O1FlushNum == 1:
                    O1CurBestHand = 5
                if O1FullHouseNum == 1:
                    O1CurBestHand = 6
                if O1FourPairNum == 1:
                    O1CurBestHand = 7
                if O1StraightFlushNum == 1:
                    O1CurBestHand = 8
                if O1RoyalFlushNum == 1:
                    O1CurBestHand = 9
                if debug ==  True:
                    print("O1 Best Hand - " +str(O1CurBestHand))
                
            if(numOfPlayers >= 3):     
                O2AllPairNums = 0
                O2TwoPairNums = 0
                O2PairNums = 0
                O2ThreePairNum = 0
                O2FourPairNum = 0
                O2FlushNum = 0
                O2FullHouseNum = 0
                O2StraightNum = 0
                O2StraightFlushNum = 0
                O2RoyalFlushNum = 0
                O2Pairs = []

                O2Pairs = findAllPairs(O2AppCards)
                O2ThreePairNum = findAllThreePairs(O2AppCards)
                O2ThreePairNum = find3Pairs(O2AppCards)
                O2FourPairNum = find4Pairs(O2AppCards)
                O2AllPairNums = len(findAllPairs(O2AppCards))
                #print ("AllPairNums - " +str(O2AllPairNums))
                if O2AllPairNums != 0:
                    O2PairNums = 1

                if O2AllPairNums == 2:
                    O2TwoPairNums = 1
                elif O2AllPairNums == 3:
                    O2TwoPairNums = 1
                elif O2AllPairNums == 4:
                    O2TwoPairNums = 1
                elif O2AllPairNums == 0: 
                    O2PairNums = 0
                    O2TwoPairNums = 0

                if O2AllPairNums != 0:
                    O2totalPairs += O2PairNums
                    O2total2Pairs += O2TwoPairNums
                    O2total3Pairs += O2ThreePairNum
                    O2total4Pairs += O2FourPairNum
                #   print("O2 Pairs - "+str(O2PairNums))
                #  print("O2 2Pairs - "+str(O2TwoPairNums))
                # print("O2 Three of a kind - "+str(O2ThreePairNum))
                    #print("O2 Four of a kind - "+str(O2FourPairNum))
                #else:
                #   print("O2 Pairs - 0")
                #  print("O2 2Pairs - 0")
                # print("O2 Three of a kind - 0")
                    #print("O2 Four of a kind - 0")

                O2StraightNum = getStraight(O2AppCards)
                #print("O2 Straights - " +str(O2StraightNum))
                O2totalStraights += O2StraightNum

                O2FlushNum = checkflush(O2AppCards)
                if O2FlushNum == None:
                    O2FlushNum = 0
                O2totalFlush += O2FlushNum
                #print("O2 FLushes - " +str(O2FlushNum))
                    
            
                O2FullHouseNum = findFull(O2ThreePairNum, O2AllPairNums)
                O2totalHouse += O2FullHouseNum
                #print ("O2 Full houses - " +str(O2FullHouseNum))

                O2StraightFlushNum = getStraightFlush(O2AppCards)
                #print("O2 Straight Flushes - " +str(O2StraightFlushNum))
                O2totalStraightFlush += O2StraightFlushNum

                
                O2RoyalFlushNum = FindRoyalFlush(O2AppCards)
                #print("O2 Royal Flushes - " +str(O2RoyalFlushNum))
                O2totalRoyalFlush += O2RoyalFlushNum

                O2CurBestHand = 0
                if O2PairNums == 1:
                    O2CurBestHand = 1
                if O2TwoPairNums == 1:
                    O2CurBestHand = 2
                if O2ThreePairNum == 1:
                    O2CurBestHand = 3
                if  O2StraightNum == 1:
                    O2CurBestHand == 4
                if O2FlushNum == 1:
                    O2CurBestHand = 5
                if O2FullHouseNum == 1:
                    O2CurBestHand = 6
                if O2FourPairNum == 1:
                    O2CurBestHand = 7
                if O2StraightFlushNum == 1:
                    O2CurBestHand = 8
                if O2RoyalFlushNum == 1:
                    O2CurBestHand = 9
                if debug == True:
                    print("O2 Best Hand - " +str(O2CurBestHand))

                        
            if(numOfPlayers >= 4):     
                O3AllPairNums = 0
                O3TwoPairNums = 0
                O3PairNums = 0
                O3ThreePairNum = 0
                O3FourPairNum = 0
                O3FlushNum = 0
                O3FullHouseNum = 0
                O3StraightNum = 0
                O3StraightFlushNum = 0
                O3RoyalFlushNum = 0
                O3Pairs = []

                O3Pairs = findAllPairs(O3AppCards)
                O3ThreePairNum = findAllThreePairs(O3AppCards)
                O3ThreePairNum = find3Pairs(O3AppCards)
                O3FourPairNum = find4Pairs(O3AppCards)
                O3AllPairNums = len(findAllPairs(O3AppCards))
                #print ("AllPairNums - " +str(O3AllPairNums))
                if O3AllPairNums != 0:
                    O3PairNums = 1

                if O3AllPairNums == 2:
                    O3TwoPairNums = 1
                elif O3AllPairNums == 3:
                    O3TwoPairNums = 1
                elif O3AllPairNums == 4:
                    O3TwoPairNums = 1
                elif O3AllPairNums == 0: 
                    O3PairNums = 0
                    O3TwoPairNums = 0

                if O3AllPairNums != 0:
                    O3totalPairs += O3PairNums
                    O3total2Pairs += O3TwoPairNums
                    O3total3Pairs += O3ThreePairNum
                    O3total4Pairs += O3FourPairNum
                #   print("O3 Pairs - "+str(O3PairNums))
                #  print("O3 2Pairs - "+str(O3TwoPairNums))
                # print("O3 Three of a kind - "+str(O3ThreePairNum))
                    #print("O3 Four of a kind - "+str(O3FourPairNum))
                #else:
                #   print("O3 Pairs - 0")
                #  print("O3 2Pairs - 0")
                # print("O3 Three of a kind - 0")
                    #print("O3 Four of a kind - 0")

                O3StraightNum = getStraight(O3AppCards)
                #print("O3 Straights - " +str(O3StraightNum))
                O3totalStraights += O3StraightNum

                O3FlushNum = checkflush(O3AppCards)
                if O3FlushNum == None:
                    O3FlushNum = 0
                O3totalFlush += O3FlushNum
                #print("O3 FLushes - " +str(O3FlushNum))
                    
            
                O3FullHouseNum = findFull(O3ThreePairNum, O3AllPairNums)
                O3totalHouse += O3FullHouseNum
                #print ("O3 Full houses - " +str(O3FullHouseNum))

                O3StraightFlushNum = getStraightFlush(O3AppCards)
                #print("O3 Straight Flushes - " +str(O3StraightFlushNum))
                O3totalStraightFlush += O3StraightFlushNum

                
                O3RoyalFlushNum = FindRoyalFlush(O3AppCards)
                #print("O3 Royal Flushes - " +str(O3RoyalFlushNum))
                O3totalRoyalFlush += O3RoyalFlushNum

                O3CurBestHand = 0
                if O3PairNums == 1:
                    O3CurBestHand = 1
                if O3TwoPairNums == 1:
                    O3CurBestHand = 2
                if O3ThreePairNum == 1:
                    O3CurBestHand = 3
                if  O3StraightNum == 1:
                    O3CurBestHand == 4
                if O3FlushNum == 1:
                    O3CurBestHand = 5
                if O3FullHouseNum == 1:
                    O3CurBestHand = 6
                if O3FourPairNum == 1:
                    O3CurBestHand = 7
                if O3StraightFlushNum == 1:
                    O3CurBestHand = 8
                if O3RoyalFlushNum == 1:
                    O3CurBestHand = 9
                if debug == True:
                    print("O3 Best Hand - " +str(O3CurBestHand))
            

            if numOfPlayers == 2:
                allVals  = {"O1" : O1CurBestHand, "Player" : myCurBestHand}
                winnner = max(allVals, key=allVals.get)
                topVal = allVals.get(winnner)
                if O1CurBestHand != myCurBestHand:
                    if debug == True:
                        print(winnner)
                elif O1CurBestHand == myCurBestHand:
                    winnner = "None"
                    if debug == True:
                        print(winnner)

                if winnner == "O1":
                    O1TotalVictories += 1
                elif winnner == "Player":
                    myTotalVictories += 1
                elif winnner == "None":
                    TotalDraws += 1
                    if topVal == allVals.get("Player"):
                        MyDraws += 1

            if numOfPlayers == 3:
                allVals  = {"O2" : O2CurBestHand, "O1" : O1CurBestHand, "Player" : myCurBestHand}
                vals = {}
                winnner = max(allVals, key=allVals.get)
                topVal = allVals.get(winnner)
                exclude_keys = [winnner]
                vals = {k: allVals[k] for k in set(list(allVals.keys())) - set(exclude_keys)}
                Vals = list(vals.values())
                for v in Vals:
                    if allVals.get(winnner) == v:
                        winnner = "None"
                if debug == True:
                    print(winnner)
                

                if winnner == "O1":
                    O1TotalVictories += 1
                elif winnner == "Player":
                    myTotalVictories += 1
                elif winnner == "O2":
                    O2TotalVictories += 1
                elif winnner == "None":
                    TotalDraws += 1
                    if topVal == allVals.get("Player"):
                        MyDraws += 1

            if numOfPlayers == 4:
                allVals  = {"O3": O3CurBestHand, "O2" : O2CurBestHand, "O1" : O1CurBestHand, "Player" : myCurBestHand}
                vals = {}
                winnner = max(allVals, key=allVals.get)
                topVal = allVals.get(winnner)
                exclude_keys = [winnner]
                vals = {k: allVals[k] for k in set(list(allVals.keys())) - set(exclude_keys)}
                Vals = list(vals.values())
                for v in Vals:
                    if allVals.get(winnner) == v:
                        winnner = "None"
                if debug == True:
                    print(winnner)
                

                if winnner == "O1":
                    O1TotalVictories += 1
                elif winnner == "Player":
                    myTotalVictories += 1
                elif winnner == "O2":
                    O2TotalVictories += 1
                elif winnner == "O3":
                    O3TotalVictories += 1
                elif winnner == "None":
                    TotalDraws += 1
                    if topVal == allVals.get("Player"):
                        MyDraws += 1
                    
                    
                    



        
        percOfPairs = totalPairs / runNums * 100
        percOf2Pairs = total2Pairs / runNums * 100
        percOf3Pairs = total3Pairs / runNums * 100
        percOf4Pairs = total4Pairs / runNums * 100
        percOfFlushes = totalFlush / runNums * 100
        percofHouses = totalHouse / runNums * 100
        percOfStraights = totalStraights / runNums * 100
        percOfStrFlush = totalStraightFlush / runNums * 100
        percOfRoyalFlush = totalRoyalFlush / runNums * 100
        percOfMyWins = myTotalVictories / runNums * 100
        percOfO1Wins = O1TotalVictories / runNums * 100
        percOfO2Wins = O2TotalVictories / runNums * 100
        percOfO3Wins = O3TotalVictories / runNums * 100
        percOfTotalDraws = TotalDraws / runNums * 100
        percOfMyDraws = MyDraws / runNums * 100

        if numOfPlayers >= 2:
            percOfO1Pairs = O1totalPairs / runNums * 100
            percOfO12Pairs = O1total2Pairs / runNums * 100
            percOfO13Pairs = O1total3Pairs / runNums * 100
            percOfO14Pairs = O1total4Pairs / runNums * 100
            percOfO1Flushes = O1totalFlush / runNums * 100
            percOfO1StraightFlush = O1totalStraightFlush / runNums * 100
            percOfO1Houses = O1totalHouse / runNums * 100
            percOfO1Straights = O1totalStraights / runNums * 100
            percOfO1Royal = O1totalRoyalFlush / runNums * 100

        if numOfPlayers >= 3:
            percOfO2Pairs = O2totalPairs / runNums * 100
            percOfO22Pairs = O2total2Pairs / runNums * 100
            percOfO23Pairs = O2total3Pairs / runNums * 100
            percOfO24Pairs = O2total4Pairs / runNums * 100
            percOfO2Flushes = O2totalFlush / runNums * 100
            percOfO2StraightFlush = O2totalStraightFlush / runNums * 100
            percOfO2Houses = O2totalHouse / runNums * 100
            percOfO2Straights = O2totalStraights / runNums * 100
            percOfO2Royal = O2totalRoyalFlush / runNums * 100

        if numOfPlayers >= 4:
            percOfO3Pairs = O3totalPairs / runNums * 100
            percOfO32Pairs = O3total2Pairs / runNums * 100
            percOfO33Pairs = O3total3Pairs / runNums * 100
            percOfO34Pairs = O3total4Pairs / runNums * 100
            percOfO3Flushes = O3totalFlush / runNums * 100
            percOfO3StraightFlush = O3totalStraightFlush / runNums * 100
            percOfO3Houses = O3totalHouse / runNums * 100
            percOfO3Straights = O3totalStraights / runNums * 100
            percOfO3Royal = O3totalRoyalFlush / runNums * 100


        print("")
        print("Player:")
        print("Pairs - "+str(totalPairs) +" - " +str(percOfPairs) +"%")
        print("2Pairs - "+str(total2Pairs) +" - " +str(percOf2Pairs) +"%")
        print("3Pairs - "+str(total3Pairs) +" - " +str(percOf3Pairs) +"%")
        print("Straights - " +str(totalStraights) +" - " + str(percOfStraights) +"%")
        print("Flushes - " +str(totalFlush) +" - " +str(percOfFlushes) +"%")
        print("Houses - " +str(totalHouse) +" - " + str(percofHouses) +"%")
        print("4Pairs - "+str(total4Pairs) +" - " +str(percOf4Pairs) +"%")
        print("Straight Flushes - "+str(totalStraightFlush) +" - " +str(percOfStrFlush) +"%")
        print("Royal Flushes - "+str(totalRoyalFlush) +" - " +str(percOfRoyalFlush) +"%")
        print("")
        if numOfPlayers >= 2 and debug == True:
            print("O1:")
            print("Pairs - "+str(O1totalPairs) +" - " +str(percOfO1Pairs) +"%")
            print("2Pairs - "+str(O1total2Pairs) +" - " +str(percOfO12Pairs) +"%")
            print("3Pairs - "+str(O1total3Pairs) +" - " +str(percOfO13Pairs) +"%")
            print("Straights - " +str(O1totalStraights) +" - " + str(percOfO1Straights) +"%")
            print("Flushes - " +str(O1totalFlush) +" - " +str(percOfO1Flushes) +"%")
            print("Houses - " +str(O1totalHouse) +" - " + str(percOfO1Houses) +"%")
            print("4Pairs - "+str(O1total4Pairs) +" - " +str(percOfO14Pairs) +"%")
            print("Straight Flushes - "+str(O1totalStraightFlush) +" - " +str(percOfO1StraightFlush) +"%")
            print("Royal Flushes - "+str(O1totalRoyalFlush) +" - " +str(percOfO1Royal) +"%")
            print("")
        if numOfPlayers >= 3 and debug == True:
            print("O2:")
            print("Pairs - "+str(O2totalPairs) +" - " +str(percOfO2Pairs) +"%")
            print("2Pairs - "+str(O2total2Pairs) +" - " +str(percOfO22Pairs) +"%")
            print("3Pairs - "+str(O2total3Pairs) +" - " +str(percOfO23Pairs) +"%")
            print("Straights - " +str(O2totalStraights) +" - " + str(percOfO2Straights) +"%")
            print("Flushes - " +str(O2totalFlush) +" - " +str(percOfO2Flushes) +"%")
            print("Houses - " +str(O2totalHouse) +" - " + str(percOfO2Houses) +"%")
            print("4Pairs - "+str(O2total4Pairs) +" - " +str(percOfO24Pairs) +"%")
            print("Straight Flushes - "+str(O2totalStraightFlush) +" - " +str(percOfO2StraightFlush) +"%")
            print("Royal Flushes - "+str(O2totalRoyalFlush) +" - " +str(percOfO2Royal) +"%")
            print("")
        if numOfPlayers >= 4 and debug == True:
            print("O3:")
            print("Pairs - "+str(O3totalPairs) +" - " +str(percOfO3Pairs) +"%")
            print("2Pairs - "+str(O3total2Pairs) +" - " +str(percOfO32Pairs) +"%")
            print("3Pairs - "+str(O3total3Pairs) +" - " +str(percOfO33Pairs) +"%")
            print("Straights - " +str(O3totalStraights) +" - " + str(percOfO3Straights) +"%")
            print("Flushes - " +str(O3totalFlush) +" - " +str(percOfO3Flushes) +"%")
            print("Houses - " +str(O3totalHouse) +" - " + str(percOfO3Houses) +"%")
            print("4Pairs - "+str(O3total4Pairs) +" - " +str(percOfO34Pairs) +"%")
            print("Straight Flushes - "+str(O3totalStraightFlush) +" - " +str(percOfO3StraightFlush) +"%")
            print("Royal Flushes - "+str(O3totalRoyalFlush) +" - " +str(percOfO3Royal) +"%")
            print("")
        if numOfPlayers >= 2:
            print("My Wins " +str(myTotalVictories) + " - " +str(percOfMyWins) + "%")
        if numOfPlayers >= 3:
            print("My Draws " +str(MyDraws) + " - " +str(percOfMyDraws) + "%")
        if debug == True:
            if numOfPlayers >= 2:
                print("O1 Wins " +str(O1TotalVictories) + " - " +str(percOfO1Wins) + "%")
            if numOfPlayers >= 3:
                print("O2 Wins " +str(O2TotalVictories) + " - " +str(percOfO2Wins) + "%")
            if numOfPlayers >= 4:
                print("O3 Wins " +str(O3TotalVictories) + " - " +str(percOfO3Wins) + "%")
        if numOfPlayers >= 2:
            print("Draws " +str(TotalDraws) + " - " +str(percOfTotalDraws) + "%")
        if debug == False and numOfPlayers >= 2:
            print("Show Hands?")
            _input = input(":")
            while _input != "Yes" and _input != "No":
                _input = input(":")
            if _input == "Yes":
                if numOfPlayers >= 2:
                    print("O1:")
                    print("Pairs - "+str(O1totalPairs) +" - " +str(percOfO1Pairs) +"%")
                    print("2Pairs - "+str(O1total2Pairs) +" - " +str(percOfO12Pairs) +"%")
                    print("3Pairs - "+str(O1total3Pairs) +" - " +str(percOfO13Pairs) +"%")
                    print("Straights - " +str(O1totalStraights) +" - " + str(percOfO1Straights) +"%")
                    print("Flushes - " +str(O1totalFlush) +" - " +str(percOfO1Flushes) +"%")
                    print("Houses - " +str(O1totalHouse) +" - " + str(percOfO1Houses) +"%")
                    print("4Pairs - "+str(O1total4Pairs) +" - " +str(percOfO14Pairs) +"%")
                    print("Straight Flushes - "+str(O1totalStraightFlush) +" - " +str(percOfO1StraightFlush) +"%")
                    print("Royal Flushes - "+str(O1totalRoyalFlush) +" - " +str(percOfO1Royal) +"%")
                    print("")
                if numOfPlayers >= 3:
                    print("O2:")
                    print("Pairs - "+str(O2totalPairs) +" - " +str(percOfO2Pairs) +"%")
                    print("2Pairs - "+str(O2total2Pairs) +" - " +str(percOfO22Pairs) +"%")
                    print("3Pairs - "+str(O2total3Pairs) +" - " +str(percOfO23Pairs) +"%")
                    print("Straights - " +str(O2totalStraights) +" - " + str(percOfO2Straights) +"%")
                    print("Flushes - " +str(O2totalFlush) +" - " +str(percOfO2Flushes) +"%")
                    print("Houses - " +str(O2totalHouse) +" - " + str(percOfO2Houses) +"%")
                    print("4Pairs - "+str(O2total4Pairs) +" - " +str(percOfO24Pairs) +"%")
                    print("Straight Flushes - "+str(O2totalStraightFlush) +" - " +str(percOfO2StraightFlush) +"%")
                    print("Royal Flushes - "+str(O2totalRoyalFlush) +" - " +str(percOfO2Royal) +"%")
                    print("")
                if numOfPlayers >= 4:
                    print("O3:")
                    print("Pairs - "+str(O3totalPairs) +" - " +str(percOfO3Pairs) +"%")
                    print("2Pairs - "+str(O3total2Pairs) +" - " +str(percOfO32Pairs) +"%")
                    print("3Pairs - "+str(O3total3Pairs) +" - " +str(percOfO33Pairs) +"%")
                    print("Straights - " +str(O3totalStraights) +" - " + str(percOfO3Straights) +"%")
                    print("Flushes - " +str(O3totalFlush) +" - " +str(percOfO3Flushes) +"%")
                    print("Houses - " +str(O3totalHouse) +" - " + str(percOfO3Houses) +"%")
                    print("4Pairs - "+str(O3total4Pairs) +" - " +str(percOfO34Pairs) +"%")
                    print("Straight Flushes - "+str(O3totalStraightFlush) +" - " +str(percOfO3StraightFlush) +"%")
                    print("Royal Flushes - "+str(O3totalRoyalFlush) +" - " +str(percOfO3Royal) +"%")
                    print("")
            



