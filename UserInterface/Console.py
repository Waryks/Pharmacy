import datetime
import copy


class Console:

    def __init__(self, medService, cardService, transactionService):
        self.__medService = medService
        self.__cardService = cardService
        self.__transactionService = transactionService
        self.__listOfMeds = self.__medService.getAllMeds()
        self.__listOfCards = self.__cardService.getAllCards()
        self.__listOfTransactions = self.__transactionService.getAllTransactions()

    # description: shows the menu
    def __showMenu(self):
        print("-------------- MENU ----------------------------------------------")
        print("")
        print(" 1: CRUD medicine.")
        print(" 2: CRUD client card.")
        print(" 3: CRUD transaction.")
        print(" 4: Search for a med or a client.")
        print(" 5: Show all the transactions from a time period.")
        print(" 6: Descending sorting for meds by sold amounts.")
        print(" 7: Descending sorting for client cards by discounted prices.")
        print(" 8: Delete all the transactions from a time period.")
        print(" 9: Apply a price increase to all the meds that have a lower price than a given value.")
        # print("10:#Undo.")
        # print("11:#Redo.")
        print("10: All permutations for a given object.")
        print("11: Binary search for an object in an objects list.")
        print("12: Exit.")
        print("")

    # description: shows the lists in the menu
    def __showListsInMenu(self):
        medsList = self.__medService.getAllMeds()
        cardsList = self.__cardService.getAllCards()
        transactionsList = self.__transactionService.getAllTransactions()
        # self.__listOfMeds = sorted(medsList, key=lambda med: med.getID())
        self.__listOfMeds = self.mySelectionSort(medsList, keyOption=lambda med: med.getID())
        self.__listOfCards = sorted(cardsList, key=lambda card: card.getID())
        self.__listOfTransactions = sorted(transactionsList, key=lambda transaction: transaction.getID())
        print("------------- THE MEDICINES LIST -----------------------------------")
        print("")
        print("ID | Name | Producer | Price | Prescription | Status")
        self.__showList(self.__listOfMeds)
        print("")
        print("------------ THE CLINET CARDS LIST ---------------------------------")
        print("")
        print("ID | Surname | Forename | CNP | Birthday | Registration | Status")
        self.__showList(self.__listOfCards)
        print("")
        print("------------ THE TRANSACTIONS LIST ---------------------------------")
        print("")
        print("ID | Med ID | Client ID | Amount |    Date    | Clock | Status")
        self.__showList(self.__listOfTransactions)
        print("")

    # description: Shows the list of objects
    def __showList(self, objects):
        objects = self.mySelectionSort(objects, keyOption=lambda objct: objct.getID())
        for obj in objects:
            if obj.getDeleteStatus() == "Active":
                print(obj)

    # description: runs the console
    def runConsole(self):
        while True:
            self.__checkForDelete()
            self.__listOfMeds = self.__medService.getAllMeds()
            self.__listOfCards = self.__cardService.getAllCards()
            self.__listOfTransactions = self.__transactionService.getAllTransactions()
            self.__showListsInMenu()
            self.__showMenu()
            print("Program: Give an option from the list above.")
            option = input("User: ")
            if option == "1":
                self.__showMedicines()
            elif option == "2":
                self.__showClientCards()
            elif option == "3":
                self.__showTransactions()
            elif option == "4":
                self.__searchFunction()
            elif option == "5":
                self.__handleShowTimePeriod()
            elif option == "6":
                self.__handleMedSort()
            elif option == "7":
                self.__handleCardSort()
            elif option == "8":
                self.__handleDeleteTimePeriod()
            elif option == "9":
                self.__handleApplyIncrease()
            elif option == "10":
                self.__handleObjectPermutations()
            # elif option == "10":
            #     self.__handleUndo()
            elif option == "11":
                self.__showBinarySearch()
            # elif option == "11":
            #     self.__handleRedo()
            elif option == "12":
                break
            elif option == "init@root11/-populate":  # STILL TESTING!!!
                print("@root11: You have accessed a secret option!")
                print("@root11: Please proceed by inserting a number")
                print("         that represents how many random meds")
                print("         would you like to add to your meds list.")
                print("Caution! This might crash your laptop! (OWN RISK)")
                howMany = int(input("User: "))
                print("@root11: Please wait until all the files are added!")
                self.__medService.populateTheRepository(howMany)
            else:
                print("Program: Give a valid option number!")

    # description: shows the medicines menu
    def __showMedicines(self):
        while True:
            self.__listOfMeds = self.__medService.getAllMeds()
            self.__showMenuMedicines()
            print("Program: Give an option from the list above.")
            option = input("User: ")
            if option == "1":
                self.__handleMedicinesAdd()
            elif option == "2":
                self.__handleMedicinesDel()
            elif option == "3":
                self.__handleMedicinesUpdate()
            elif option == "4":
                self.__handleUndoMed()
            elif option == "5":
                self.__handleRedoMed()
            elif option == "a":
                print("------------------------------------------------------------------")
                print("Program: The list of medicines is:")
                print("")
                if not self.__listOfMeds:
                    print("EMPTY")
                else:
                    self.__showList(self.__listOfMeds)
                print("")
            elif option == "b":
                break
            else:
                print("Program: Give a valid option number!")

    # description: shows the menu for medicines
    def __showMenuMedicines(self):
        print("-------------- MEDICINES -----------------------------------------")
        print("")
        print("Program: Choose an option to proceed!")
        print("")
        print(" 1: Add Medicine.")
        print(" 2: Delete Medicine.")
        print(" 3: Update Medicine.")
        print(" 4: Undo.")
        print(" 5: Redo.")
        print(" a. Show all Medicines.")
        print(" b. Go back.")
        print("")

    # description: adds a medicine
    def __handleMedicinesAdd(self):
        foundError = False
        try:
            while True:
                foundDuplicate = False
                negative = False
                null = False
                medID = int(input("Program: Med's ID = "))
                if medID < 0:
                    negative = True
                    print("Program: Error! The ID cannot be negative.")
                if medID == 0:
                    null = True
                    print("Program: Error! The ID cannot be null.")
                for med in self.__listOfMeds:
                    if med.getID() == medID:
                        print("Program: Error! Invalid ID.")
                        foundDuplicate = True
                if not foundDuplicate and not negative and not null:
                    break
            while True:
                medName = input("Program: Med's Name = ")
                if medName != "":
                    break
                else:
                    print("Program: Error! Blank spaces are not accepted!")
            while True:
                medProducer = input("Program: Med's Producer = ")
                if medProducer != "":
                    break
                else:
                    print("Program: Error! Blank spaces are not accepted!")
            medPrice = float(input("Program: Med's Price = "))
            medPrescription = input("Program: Med's Prescription (True or False) = ")
            if medPrescription not in ["True", "False"]:
                print("Program: The prescription can only be True or False")
                return
            self.__medService.addMeds(
                medID,
                medName,
                medProducer,
                medPrice,
                medPrescription,
                "Active"
            )
        except ValueError as ve:
            print("------------------------------------------------------------------")
            print("ERRORS ->", ve)
            foundError = True
            print("")
        if not foundError:
            print("Program: The medicine has been added!")

    # description: deletes a medicine
    def __handleMedicinesDel(self):  # NEEDS UPDATE TO STATUS
        try:
            foundID = False
            medID = int(input("Program: The med's ID you want to remove = "))
            for med in self.__listOfMeds:
                if med.getID() == medID:
                    foundID = True
            if not foundID:
                print("Program: Error! The ID does not exist!")
            else:
                self.__medService.removeMeds(medID)
                print("Program: The medicine has been removed!")
        except ValueError:
            print("Program: The ID does not exist!")

    # description: updates a medicine
    def __handleMedicinesUpdate(self):
        medID = int(input("Program: The med's ID you want to update = "))
        foundID = False
        for med in self.__listOfMeds:
            if med.getID() == medID:
                foundID = True
        if not foundID:
            print("Program: Error! The ID does not exist!")
        else:
            for med in self.__listOfMeds:
                if med.getID() == medID:
                    medName = med.getName()
                    medProducer = med.getProducer()
                    medPrice = med.getPrice()
                    medPrescription = med.getPrescription()
                    medDeleteStatus = med.getDeleteStatus()
            newMedName = input("Program: New Med's Name = ")
            if newMedName == "":
                newMedName = medName
            newMedProducer = input("Program: New Med's Producer = ")
            if newMedProducer == "":
                newMedProducer = medProducer
            newMedPrice = input("Program: New Med's Price = ")
            if newMedPrice == "":
                newMedPrice = float(medPrice)
            while True:
                newMedPrescription = input("Program: New Med's Prescription (True or False) = ")
                if newMedPrescription == "":
                    newMedPrescription = medPrescription
                    break
                elif newMedPrescription not in ["True", "False"]:
                    print("Program: Incorrect Value! Try again!")
                else:
                    break
            while True:
                newMedDeleteStatus = input("Program: New Med's Status (Active or Inactive) = ")
                if newMedDeleteStatus == "":
                    newMedDeleteStatus = medDeleteStatus
                    break
                elif newMedDeleteStatus not in ["Active", "Inactive"]:
                    print("Program: Incorrect Value! Try again!")
                else:
                    break
            self.__medService.updateMeds(medID, newMedName, newMedProducer,
                                         newMedPrice, newMedPrescription, newMedDeleteStatus)
            print("Program: The medicine has been updated!")

    # description: shows the list of client cards
    def __showClientCards(self):
        while True:
            self.__listOfCards = self.__cardService.getAllCards()
            self.__showMenuClientCards()
            print("Program: Give an option from the list above.")
            option = input("User: ")
            if option == "1":
                self.__handleClientCardsAdd()
            elif option == "2":
                self.__handleClientsCardsDel()
            elif option == "3":
                self.__handleClientsCardsUpdate()
            elif option == "4":
                self.__handleUndoCard()
            elif option == "5":
                self.__handleRedoCard()
            elif option == "a":
                print("------------------------------------------------------------------")
                print("Program: The list of cards is:")
                print("")
                if not self.__listOfCards:
                    print("EMPTY")
                else:
                    self.__showList(self.__cardService.getAllCards())
                print("")
            elif option == "b":
                break
            else:
                print("Program: Give a valid option number!")

    # description: shows the menu of client cards
    def __showMenuClientCards(self):
        print("-------------- CLIENT CARDS --------------------------------------")
        print("")
        print("Program: Choose an option to proceed!")
        print("")
        print(" 1: Add a Client Card.")
        print(" 2: Delete a Client Card.")
        print(" 3: Update a Client Card.")
        print(" 4: Undo.")
        print(" 5: Redo.")
        print(" a. Show all Client Cards.")
        print(" b. Go back.")
        print("")

    # description: adds a client card
    def __handleClientCardsAdd(self):
        foundError = False
        try:
            while True:
                foundDuplicate = False
                negative = False
                null = False
                cardID = int(input("Program: Card's ID = "))
                if cardID < 0:
                    negative = True
                    print("Program: Error! The ID cannot be negative.")
                if cardID == 0:
                    null = True
                    print("Program: Error! The ID cannot be null.")
                for card in self.__listOfCards:
                    if card.getID() == cardID:
                        print("Program: Error! Invalid ID.")
                        foundDuplicate = True
                if not foundDuplicate and not negative and not null:
                    break
            while True:
                cardSurname = input("Program: Client's Surname = ")
                if cardSurname != "":
                    break
                else:
                    print("Program: Error! Blank spaces are not accepted")
            while True:
                cardForename = input("Program: Client's Forename = ")
                if cardForename != "":
                    break
                else:
                    print("Program: Error! Blank spaces are not accepted")
            while True:
                cardCNP = input("Program: Client's CNP = ")
                if cardCNP != "":
                    if len(cardCNP) == 13:
                        break
                    else:
                        print("Program: Error! Invalid CNP. It needs to have 13 digits.")
                else:
                    print("Program: Error! Blank spaces are not accepted")

            while True:
                cardDateOfBirth = input("Program: Client's Date Of Birth = ")
                if cardDateOfBirth != "":
                    try:
                        datetime.datetime.strptime(cardDateOfBirth, "%d.%m.%Y")
                        break
                    except ValueError:
                        print("Program: Error! Wrong date format!")
                        print("Program: Correct format is <Day.Month.Year>")
                else:
                    print("Program: Error! Blank spaces are not accepted")

            while True:
                cardRegistrationDate = input("Program: Client's Registration Date = ")
                if cardRegistrationDate != "":
                    try:
                        datetime.datetime.strptime(cardRegistrationDate, "%d.%m.%Y")
                        break
                    except ValueError:
                        print("Program: Error! Wrong date format!")
                        print("Program: Correct format is <Day.Month.Year>")
                else:
                    print("Program: Error! Blank spaces are not accepted")

            self.__cardService.addCards(
                cardID,
                cardSurname,
                cardForename,
                cardCNP,
                cardDateOfBirth,
                cardRegistrationDate,
                "Active"
            )
        except ValueError as ve:
            print("------------------------------------------------------------------")
            print("ERRORS ->", ve)
            foundError = True
            print("")
        if not foundError:
            print("Program: The client card has been added!")

    # description: deletes a card
    def __handleClientsCardsDel(self):  # NEEDS UPDATE TO STATUS
        try:
            foundID = False
            cardID = int(input("Program: The card's ID you want to remove = "))
            for card in self.__listOfCards:
                if card.getID() == cardID:
                    foundID = True
            if not foundID:
                print("Program: Error! The ID does not exist!")
            else:
                self.__cardService.removeCards(cardID)
                print("Program: The client card has been removed!")
        except ValueError:
            print("Program: The ID does not exist!")

    # description: updates a card
    def __handleClientsCardsUpdate(self):
        cardID = int(input("Program: The client card's ID you want to update = "))
        foundID = False
        for card in self.__listOfCards:
            if card.getID() == cardID:
                foundID = True
        if not foundID:
            print("Program: Error! The ID does not exist!")
        else:
            for card in self.__listOfCards:
                if card.getID() == cardID:
                    cardSurname = card.getSurname()
                    cardForename = card.getForename()
                    cardCNP = card.getCNP()
                    cardDateOfBirth = card.getDateOfBirth()
                    cardRegistrationDate = card.getRegistrationDate()
                    cardDeleteStatus = card.getDeleteStatus()
            newcardSurname = input("Program: New Card's client Surame = ")
            if newcardSurname == "":
                newcardSurname = cardSurname
            newcardForename = input("Program: New Card's client Forename = ")
            if newcardForename == "":
                newcardForename = cardForename

            while True:
                newcardCNP = input("Program: New Card's client CNP = ")
                if newcardCNP == "":
                    newcardCNP = cardCNP
                    break
                else:
                    if len(newcardCNP) == 13:
                        break
                    else:
                        print("Program: Error! Invalid CNP. It needs to have 13 digits.")

            while True:
                try:
                    newcardDateOfBirth = input("Program: New date of birth of the client = ")
                    if newcardDateOfBirth == "":
                        newcardDateOfBirth = cardDateOfBirth
                        break
                    datetime.datetime.strptime(newcardDateOfBirth, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Program: Error! Wrong date format!")
                    print("Program: Correct format is <Day.Month.Year>")

            while True:
                try:
                    newcardRegistrationDate = input("Program: New registration date for the client = ")
                    if newcardRegistrationDate == "":
                        newcardRegistrationDate = cardRegistrationDate
                        break
                    datetime.datetime.strptime(newcardRegistrationDate, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Program: Error! Wrong date format!")
                    print("Program: Correct format is <Day.Month.Year>")

            while True:
                newCardDeleteStatus = input("Program: New Card's Status (Active or Inactive) = ")
                if newCardDeleteStatus == "":
                    newCardDeleteStatus = cardDeleteStatus
                    break
                elif newCardDeleteStatus not in ["Active", "Inactive"]:
                    print("Program: Incorrect Value! Try again!")
                else:
                    break

            self.__cardService.updateCards(cardID,
                                           newcardSurname,
                                           newcardForename,
                                           newcardCNP,
                                           newcardDateOfBirth,
                                           newcardRegistrationDate,
                                           newCardDeleteStatus)
            print("Program: The client card has been updated!")

    # description: shows the transactions
    def __showTransactions(self):
        while True:
            self.__listOfTransactions = self.__transactionService.getAllTransactions()
            self.__showMenuTransactions()
            print("Program: Give an option from the list above.")
            option = input("User: ")
            if option == "1":
                self.__handleTransactionsAdd()
            elif option == "2":
                self.__handleTransactionsDel()
            elif option == "3":
                self.__handleTransactionsUpdate()
            elif option == "4":
                self.__discountForMeds()
            elif option == "5":
                self.__handleUndoTransaction()
            elif option == "6":
                self.__handleRedoTransaction()
            elif option == "a":
                print("------------------------------------------------------------------")
                print("Program: The list of transactions is:")
                print("")
                if not self.__listOfTransactions:
                    print("EMPTY")
                else:
                    print("ID | Med ID | Client ID | Amount |    Date    | Clock | Status")
                    self.__showList(self.__transactionService.getAllTransactions())
                print("")
            elif option == "b":
                break
            else:
                print("Program: Give a valid option number!")

    # description: shows the menu for transactions
    def __showMenuTransactions(self):
        print("-------------- TRANSACTIONS --------------------------------------")
        print("")
        print("Program: Choose an option to proceed!")
        print("")
        print(" 1: Add a Transaction.")
        print(" 2: Delete a Transaction.")
        print(" 3: Update a Transaction.")
        print(" 4: Show the payments and the given discounts")
        print(" 5: Undo.")
        print(" 6: Redo.")
        print(" a. Show all Transactions.")
        print(" b. Go back.")
        print("")

    # description: adds a transaction
    def __handleTransactionsAdd(self):
        foundError = False
        try:
            while True:
                foundDuplicate = False
                negative = False
                null = False
                transactionID = int(input("Program: Transaction's ID = "))
                if transactionID < 0:
                    negative = True
                    print("Program: Error! The ID cannot be negative.")
                if transactionID == 0:
                    null = True
                    print("Program: Error! The ID cannot be null.")
                for transaction in self.__listOfTransactions:
                    if transaction.getID() == transactionID:
                        print("Program: Error! Invalid ID.")
                        foundDuplicate = True
                if not foundDuplicate and not negative and not null:
                    break
            while True:
                foundID = False
                medID = int(input("Program: Medication's ID = "))
                for med in self.__listOfMeds:
                    if med.getID() == medID:
                        foundID = True
                if foundID:
                    break
                else:
                    print("Program: Error! This medicine ID does not exist.")
            while True:
                foundID = False
                cardID = int(input("Program: Card's ID = "))
                for card in self.__listOfCards:
                    if card.getID() == cardID:
                        foundID = True
                if foundID or cardID == 0:
                    break
                else:
                    print("Program: Error! This card ID does not exist.")
            while True:
                amount = int(input("Program: The amount of meds = "))
                if amount > 0:
                    break
                print("Program: Error! The amount cannot be negative or 0!")
            while True:
                try:
                    date = input("Program: The date of the transaction = ")
                    datetime.datetime.strptime(date, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Program: Error! Wrong date format!")
                    print("Program: Correct format is <Day.Month.Year>")
            while True:
                try:
                    clock = input("Program: The exact time = ")
                    datetime.datetime.strptime(clock, "%H:%M")
                    break
                except ValueError:
                    print("Program: Error! Wrong clock format!")
                    print("Program: Correct format is <Hour:Minutes>")
            self.__transactionService.addTransactions(
                transactionID,
                medID,
                cardID,
                amount,
                date,
                clock,
                "Active"
            )
        except ValueError as ve:
            print("------------------------------------------------------------------")
            print("ERRORS ->", ve)
            foundError = True
            print("")
        if not foundError:
            print("Program: The transaction has been added!")

    # description: deletes a transaction
    def __handleTransactionsDel(self):  # NEEDS UPDATE TO STATUS
        try:
            foundID = False
            transactionID = int(input("Program: The transaction's ID you want to remove = "))
            for transaction in self.__listOfTransactions:
                if transaction.getID() == transactionID:
                    foundID = True
            if not foundID:
                print("Program: Error! The ID does not exist!")
            else:
                self.__transactionService.removeTransactions(transactionID)
                print("Program: The transaction has been removed!")
        except ValueError:
            print("Program: The ID does not exist!")

    # description: updates a transaction
    def __handleTransactionsUpdate(self):
        transactionID = int(input("Program: The transaction's ID you want to update = "))
        foundID = False
        for transaction in self.__listOfTransactions:
            if transaction.getID() == transactionID:
                foundID = True
        if not foundID:
            print("Program: Error! The ID does not exist!")
        else:
            for trans in self.__listOfTransactions:
                if trans.getID() == transactionID:
                    medID = trans.getMedID()
                    cardID = trans.getCardID()
                    medsAmount = trans.getAmount()
                    transactionDate = trans.getDate()
                    transactionClock = trans.getClock()
                    transactionDeleteStatus = trans.getDeleteStatus()
            while True:
                newMedID = input("Program: New Med's ID = ")
                if newMedID == "":
                    newMedID = medID
                    break
                else:
                    foundID = False
                    for med in self.__listOfMeds:
                        if str(med.getID()) == str(newMedID):
                            foundID = True
                    if not foundID:
                        print("Program: Error! The ID does not exist!")
                    else:
                        break
            while True:
                newCardID = input("Program: New Client Card's ID = ")
                if newCardID == "" or newCardID == "0":
                    newCardID = cardID
                    break
                else:
                    foundID = False
                    for card in self.__listOfCards:
                        if str(card.getID()) == str(newCardID):
                            foundID = True
                    if not foundID:
                        print("Program: Error! The ID does not exist!")
                    else:
                        break

            while True:
                newMedsAmount = input("Program: New amount of medications = ")
                if newMedsAmount == "":
                    try:
                        newMedsAmount = int(medsAmount)
                        break
                    except ValueError:
                        print("Program: ERROR! The amount has to be an integer")
                try:
                    if int(newMedsAmount) > 0:
                        break
                    print("Program: Error! The amount cannot be negative or 0!")
                except ValueError:
                    print("Program: ERROR! The amount has to be an integer")

            while True:
                try:
                    newTransactionDate = input("Program: New transaction date = ")
                    if newTransactionDate == "":
                        newTransactionDate = transactionDate
                        break
                    datetime.datetime.strptime(newTransactionDate, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Program: Error! Wrong date format!")
                    print("Program: Correct format is <Day.Month.Year>")

            while True:
                try:
                    newTransactionClock = input("Program: New transaction clock = ")
                    if newTransactionClock == "":
                        newTransactionClock = transactionClock
                        break
                    datetime.datetime.strptime(newTransactionClock, "%H:%M")
                    break
                except ValueError:
                    print("Program: Error! Wrong clock format!")
                    print("Program: Correct format is <Hour:Minutes>")

            while True:
                newTransactionDeleteStatus = input("Program: New Transaction's Status (Active or Inactive) = ")
                if newTransactionDeleteStatus == "":
                    newTransactionDeleteStatus = transactionDeleteStatus
                    break
                elif newTransactionDeleteStatus not in ["Active", "Inactive"]:
                    print("Program: Incorrect Value! Try again!")
                else:
                    break

            self.__transactionService.updateTransactions(transactionID,
                                                         newMedID,
                                                         newCardID,
                                                         newMedsAmount,
                                                         newTransactionDate,
                                                         newTransactionClock,
                                                         newTransactionDeleteStatus)
            print("Program: The transaction has been updated!")

    # description: applies an increase to meds prices
    def __handleApplyIncrease(self):
        print("Program: Give a price limit!")
        while True:
            try:
                value = float(input("User: "))
                break
            except ValueError:
                print("Program: Only float types can be inserted")
        print("Program: Give a percentage!")
        percentageString = input("User: ")
        percentageSplitList = percentageString.split("%")
        percentage = int(percentageSplitList[0])
        self.__medService.apllyPriceIncreaseToMeds(value, percentage)
        print("Program: Price increase has been applied!")
        print("Program: The medicines list with the price increase is:")
        print("")
        self.__showList(self.__medService.getAllMeds())
        print("")

    # description: applies discount for meds
    def __discountForMeds(self):
        listOfDiscounts = self.__transactionService.apllyMedsDiscount()
        for index in range(len(listOfDiscounts)):
            print("Transaction", listOfDiscounts[index][0],
                  ", Initial Price:", listOfDiscounts[index][1],
                  ", New Price:", listOfDiscounts[index][2],
                  ", Discount:", listOfDiscounts[index][3])
        print("\n")

    # description: searches key words in lists
    def __searchFunction(self):
        while True:
            print("----------------- FULL TEXT SEARCH -----------------------------------")
            print("")
            print(" 1: Find a specific item.")
            print(" 2: Go back.")
            print("")
            print("Program: Give an option number!")
            try:
                clientsList = []
                option = int(input("User: "))
                if option == 1:
                    print("Program: Insert a key word!")
                    keyWord = input("User: ")
                    lowerKeyWord = keyWord.lower()
                    print("Program: Applying full text search...\n")

                    print("# The meds with the key word '" + keyWord + "' are:\n")
                    listOfMatchingMeds = self.__transactionService.searchMed(lowerKeyWord)
                    if len(listOfMatchingMeds) == 0:
                        print("> No meds found with the inserted keyword! <")
                    else:
                        for element in range(len(listOfMatchingMeds)):
                            print(listOfMatchingMeds[element])

                    print("\n# The clients with the key word '" + keyWord + "' are:\n")
                    for client in self.__cardService.getAllCards():
                        clientsList.append(client)
                    listOfMatchingClients = self.__transactionService.searchClientRecursive(lowerKeyWord,
                                                                                            len(clientsList),
                                                                                            [],
                                                                                            clientsList)
                    if len(listOfMatchingClients) == 0:
                        print("> No clients found with the inserted keyword! <\n")
                    else:
                        for element in range(len(listOfMatchingClients)):
                            print(listOfMatchingClients[element])
                    print("")
                elif option == 2:
                    break
                else:
                    print("Program: Give a valid option number!")
            except ValueError:
                print("Program: Give a valid option!")

    # description: sorts the medicines
    def __handleMedSort(self):
        medsAmount = self.__transactionService.applyMedsSort()
        medsList = self.__medService.getAllMeds()
        print("\nThe sorted list of medicines by sold amounts is:\n")
        for index in range(len(medsAmount)):
            for med in medsList:
                if medsAmount[index][0] == med.getID():
                    print(med, " |  with", medsAmount[index][1], "sells.")
                    break
        print("\n")

    # description: sorts the cards
    def __handleCardSort(self):
        discountsList = self.__transactionService.applyCardsSort()
        cardsList = self.__cardService.getAllCards()
        print("\nThe sorted list of client cards by discounted prices is:\n")
        for index in range(len(discountsList)):
            for client in cardsList:
                if discountsList[index][0] == client.getID():
                    print(client, " | with", discountsList[index][1], "used discounts.")
                    break
        print("\n")

    # description: shows the transactions from a time period
    def __handleShowTimePeriod(self):
        transactionsList = self.__listOfTransactions
        print("Program: Enter the start date. (%d.%m.%y)")
        day0 = input("User: ")
        print("Program: Enter the end date. (%d.%m.%y)")
        dayZ = input("User: ")
        print("\nID | Med ID | Client ID | Amount |    Date    | Clock")
        dateObject0 = datetime.datetime.strptime(day0, "%d.%m.%Y")
        dateObjectZ = datetime.datetime.strptime(dayZ, "%d.%m.%Y")
        datesList = []
        for transaction in transactionsList:
            currentDate = datetime.datetime.strptime(transaction.getDate(), "%d.%m.%Y")
            datesList.append(currentDate)
            if dateObjectZ >= currentDate >= dateObject0 and transaction.getDeleteStatus() == "Active":
                print(transaction)
        print("\n")

    # description: deletes the transactions from a time period
    def __handleDeleteTimePeriod(self):
        transactionsList = self.__listOfTransactions
        print("Program: Enter the start date. (%d.%m.%y)")
        day0 = input("User: ")
        print("Program: Enter the end date. (%d.%m.%y)")
        dayZ = input("User: ")
        dateObject0 = datetime.datetime.strptime(day0, "%d.%m.%Y")
        dateObjectZ = datetime.datetime.strptime(dayZ, "%d.%m.%Y")
        for transaction in transactionsList:
            currentDate = datetime.datetime.strptime(transaction.getDate(), "%d.%m.%Y")
            if dateObjectZ >= currentDate >= dateObject0:
                self.__transactionService.removeTransactions(transaction.getID())
        print("\n")

    # desc: checks if any statuses have changed to Inactive
    def __checkForDelete(self):
        medsList = self.__listOfMeds
        transactionsList = self.__listOfTransactions
        cardsList = self.__listOfCards
        for transaction in transactionsList:
            medNotValid = False
            for med in medsList:
                if str(med.getID()) == str(transaction.getMedID()) and \
                        str(med.getDeleteStatus()) == "Inactive":
                    transaction.setDeleteStatus("Inactive")
                    medNotValid = True
                    break
            if not medNotValid:
                for client in cardsList:
                    if str(client.getID()) == str(transaction.getCardID()) and \
                            str(client.getDeleteStatus()) == "Inactive":
                        transaction.setCardID(0)
                        break

    def __handleUndoTransaction(self):
        self.__transactionService.doUndoTransaction()

    def __handleRedoTransaction(self):
        self.__transactionService.doRedoTransaction()

    def __handleUndoCard(self):
        self.__cardService.doUndoCard()

    def __handleRedoCard(self):
        self.__cardService.doRedoCard()

    def __handleUndoMed(self):
        self.__medService.doUndoMed()

    def __handleRedoMed(self):
        self.__medService.doRedoMed()

    # def __handlePermuteObjects(self, IDsList, listLength, permutedList):
    #     return self.__transactionService.permuteObjects(IDsList, listLength, permutedList)

    # does the permutations for different objects
    def __handleObjectPermutations(self):
        while True:
            print("1. Show all permutations for the meds.")
            print("2. Show all permutations for the clients.")
            print("3. Show all permutations for the transactions.")
            print("")
            print("Program: Give an option from the above list.")
            op = int(input("User: "))
            if op == 1:
                '''
                IDsList = []
                for index in range(1, len(self.__listOfMeds) + 1):
                    IDsList.append(index)
                self.__transactionService.permute(IDsList, 0, len(IDsList))
                '''
                self.circularPermutations(self.__listOfMeds,
                                          len(self.__listOfMeds))
            elif op == 2:
                '''
                IDsList = []
                for index in range(1, len(self.__listOfCards) + 1):
                    IDsList.append(index)
                self.__transactionService.permute(IDsList, 0, len(IDsList))
                '''
                self.circularPermutations(self.__listOfCards,
                                          len(self.__listOfCards))
            elif op == 3:
                '''
                IDsList = []
                for index in range(1, len(self.__listOfTransactions) + 1):
                    IDsList.append(index)
                self.__transactionService.permute(IDsList, 0, len(IDsList))
                '''
                self.circularPermutations(self.__listOfTransactions,
                                          len(self.__listOfTransactions))
            else:
                print("Program: Error! Give a valid option number.")

    # desc: my own selection sort function
    def mySelectionSort(self, listOfObjects, keyOption=None, reverseStatus=False):
        returnList = listOfObjects[:]
        for i in range(0, len(listOfObjects) - 1):
            for j in range(i + 1, len(listOfObjects)):
                e1 = returnList[i]
                e2 = returnList[j]
                if keyOption is not None:
                    e1 = keyOption(e1)
                    e2 = keyOption(e2)
                comparison = e1 > e2
                if reverseStatus is True:
                    comparison = not comparison
                if comparison is True:
                    aux = returnList[i]
                    returnList[i] = returnList[j]
                    returnList[j] = aux
        return returnList

    # desc: shows the binary search menu
    def __showBinarySearch(self):
        while True:
            print("1. Search by ID for a med.")
            print("2. Search by ID for a client card.")
            print("3. Search by ID for a transaction.")
            print("b. Back.")
            print("")
            print("Program: Give an option from the above list.")
            op = input("User: ")
            if op == "1":
                self.__handleBinarySearch(self.__listOfMeds)
            elif op == "2":
                self.__handleBinarySearch(self.__listOfCards)
            elif op == "3":
                self.__handleBinarySearch(self.__listOfTransactions)
            elif op == "b":
                break

    # desc: shows the elements from a list
    # input: objectsList - list of objects
    def showElementsFromList(self, objectsList):
        length = len(objectsList)
        for index2 in range(0, length):
            print(objectsList[index2], end=" ")
            print("")
        print("")

    # desc: swaps all the elements of a list to the left with a position
    # input: objectsList - list of objects
    def swapElements(self, objectsList):
        length = len(objectsList)
        firstObject = objectsList[0]
        for index2 in range(1, length):
            objectsList[index2 - 1] = objectsList[index2]
        objectsList[length - 1] = firstObject

    # desc: does circular permutations to an objectsList
    # input: objectsList - list of objects
    #        listLength - length of the list
    def circularPermutations(self, objectsList, listLength):
        if listLength == 0:
            return
        else:
            self.swapElements(objectsList)
            self.showElementsFromList(objectsList)
            self.circularPermutations(objectsList, listLength - 1)

    # Desc: Handles binary search for an object
    # input: objectsList - list of objects
    def __handleBinarySearch(self, objectsList):
        objectsList = sorted(objectsList, key=lambda objct: objct.getID())
        print(objectsList)
        while True:
            try:
                print("Program: Insert an ID.")
                ID = int(input("User: "))
                '''
                while True:
                    try:
                        ID = int(input("User: "))
                        foundID = False
                        for obj in objectsList:
                            if obj.getID() == ID:
                                foundID = True
                        if foundID:
                            break
                    except ValueError:
                        print("Program: Error! Only integeres are allowed")
                '''
                if isinstance(ID, int):
                    break
            except ValueError:
                print("Program: Error! ID must be int!")
        position = self.__transactionService.binarySearch(objectsList, 0, len(objectsList) - 1, ID)
        if position == -1:
            print("Program: There is no object with the given ID in list")
        else:
            print("The object is situated at position:", position)
