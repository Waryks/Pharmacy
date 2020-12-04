from Repository.RepositoryGeneric import *


class ServicesTransaction:
    def __init__(self, repositoryGeneric):
        self.__repo = repositoryGeneric
        self.__undoList = []
        self.__redoList = []

    # description: adds a new transaction
    # input: ID - int, the ID of the transaction
    #        medID - int, the ID of the med
    #        cardID - int, the ID of the client card
    #        amount - int, the amount of meds sold
    #        date - str, the release date of the med
    #        clock - str, the exact time the med was released
    #        deleteStatus - str, True if available, False if NOT
    def addTransactions(self, ID, medID, cardID, amount, date, clock, deleteStatus):
        transaction = Transaction(ID, medID, cardID, amount, date, clock, deleteStatus)
        self.__repo.addTransaction(transaction)
        self.__undoList.append(lambda: self.__repo.deleteTransaction(transaction))
        self.__redoList.append(lambda: self.__repo.addTransaction(transaction))
        # self.__redoList.reverse()

    # description: modifies a transaction and updates it
    # input: ID - int, the ID of the transaction
    #        newMedID - int, the new ID of the med
    #        newCardID - int, the new ID of the client card
    #        newAmount - int, the new amount of meds sold
    #        newDate - str, the new release date of the med
    #        newClock - str, the new exact time the med was released
    #        newDeleteStatus - str, True if available, False if not
    def updateTransactions(self, ID, medID, newCardID, newAmount, newDate, newClock, newDeleteStatus):
        for trans in self.getAllTransactions():
            if trans.getID() == ID:
                transCopy = trans
        transaction = Transaction(ID, medID, newCardID, newAmount, newDate, newClock, newDeleteStatus)
        self.__undoList.append(lambda: self.__repo.updateTransaction(transCopy))
        self.__redoList.append(lambda: self.__repo.updateTransaction(transaction))
        # self.__redoList.reverse()
        self.__repo.updateTransaction(transaction)

    # description: removes a transaction
    # input: ID - int, the ID of the transaction
    def removeTransactions(self, ID):
        transactionsList = self.__repo.getAllTransactions()
        for transaction in transactionsList:
            if transaction.getID() == ID:
                transCopy = transaction
                self.__undoList.append(lambda: self.__repo.addTransaction(transCopy))
                self.__redoList.append(lambda: self.__repo.deleteTransaction(transaction))
                # self.__redoList.reverse()
                self.__repo.deleteTransaction(transaction)
                break

    # description: returns all the transactions
    def getAllTransactions(self):
        return self.__repo.getAllTransactions()

    def apllyMedsDiscount(self):
        transactionsList = self.__repo.getAllTransactions()
        medsList = self.__repo.getAllMeds()
        listOfDiscounts = []
        for transaction in transactionsList:
            currentMedID = transaction.getMedID()
            medicationsList = medsList
            for med in medicationsList:
                if str(med.getID()) == str(currentMedID):
                    discount = 0
                    percentage = "0%"
                    if transaction.getCardID() != "0":
                        if med.getPrescription() == "True":
                            discount = 1 / 10
                            percentage = "10%"
                        elif med.getPrescription() == "False":
                            discount = 3 / 20
                            percentage = "15%"
                    medPrice = float(med.getPrice())
                    newMedPrice = float(medPrice - medPrice * discount)
                    newMedPrice = float("{0:.2f}".format(newMedPrice))
                    listOfDiscounts.append([transaction.getID(), medPrice, newMedPrice, percentage])
                    break
        return listOfDiscounts

    def searchMed(self, lowerKeyWord):
        medsList = self.__repo.getAllMeds()
        listOfMatchingMeds = []
        for med in medsList:
            wordsList = [str(med.getID()).lower(),
                         med.getName().lower(),
                         med.getProducer().lower(),
                         str(med.getPrice()).lower(),
                         str(med.getPrescription()).lower()]
            matching = [s for s in wordsList if lowerKeyWord in s]
            if len(matching) and med.getDeleteStatus() == "Active":
                listOfMatchingMeds.append(med)
        return listOfMatchingMeds

    def searchClientRecursive(self, lowerKeyWord, length, listOfMatchingClients, clientsList):
        if length == 0:
            return listOfMatchingClients
        else:
            wordsList = [clientsList[length - 1].getSurname().lower(),
                         clientsList[length - 1].getForename().lower()]
            matching = [s for s in wordsList if lowerKeyWord in s]
            if len(matching) and clientsList[length - 1].getDeleteStatus() == "Active":
                listOfMatchingClients.append(clientsList[length - 1])
            return self.searchClientRecursive(lowerKeyWord, length - 1, listOfMatchingClients, clientsList)

    def applyMedsSort(self):

        def sortBySecond(val):
            return val[1]

        medsList = self.__repo.getAllMeds()
        transactionsList = self.__repo.getAllTransactions()
        medsAmount = []
        index = 1
        for _ in medsList:
            medsAmount.append([index, 0])
            index += 1
        for transaction in transactionsList:
            crtTransactionMedID = str(transaction.getMedID())
            for med in medsList:
                if str(med.getID()) == str(crtTransactionMedID):
                    for index in range(0, len(medsAmount)):
                        if str(medsAmount[index][0]) == crtTransactionMedID:
                            medsAmount[index][1] += transaction.getAmount()
                            break
                    break
        medsAmount = sorted(medsAmount, key=lambda meds: sortBySecond(meds), reverse=True)
        return medsAmount

    def applyCardsSort(self):

        def sortBySecond(val):
            return val[1]

        cardsList = self.__repo.getAllCards()
        transactionsList = self.__repo.getAllTransactions()
        discountsList = []
        indexesList = []
        index = 1
        for _ in cardsList:
            discountsList.append(0)
            indexesList.append(index)
            index += 1
        for transaction in transactionsList:
            for client in cardsList:
                if str(client.getID()) == str(transaction.getCardID()):
                    for index in range(len(indexesList)):
                        if str(indexesList[index]) == str(client.getID()):
                            discountsList[index] += 1
                            break
                    break
        zippedList = list(zip(indexesList, discountsList))
        zippedList = sorted(zippedList, key=lambda element: sortBySecond(element), reverse=True)
        return zippedList

    # desc: undoes a transaction
    def doUndoTransaction(self):
        if len(self.__undoList) == 1:
            self.__redoList.reverse()
        if len(self.__undoList) == 0:
            print("Program: There are no commands to be undone.")
        else:
            op = self.__undoList.pop()
            op()

    # desc: redoes a transaction
    def doRedoTransaction(self):
        if len(self.__redoList) == 0:
            print("Program: There are no commands to be redone.")
        else:
            op = self.__redoList.pop()
            op()

    # Desccription: Does binary search for a cars with a given id
    # Input: objectsList, list of objects
    #        left: int, initial position of the objects list
    #        right: int, final position of the objects list
    #        ID: int, given ID to be searched for
    # Output: Returns the position of the object if founded or -1 if there is no object with this ID
    def binarySearch(self, objectsList, left, right, ID):
        if right >= left:
            midPoz = left + (right - left) // 2
            # print(midPoz)
            # print("if", objectsList[midPoz].getID(), "==", ID)
            if str(objectsList[midPoz].getID()) == str(ID):
                return midPoz
            elif str(objectsList[midPoz].getID()) > str(ID):
                return self.binarySearch(objectsList, left, midPoz - 1, ID)
            else:  # int(objectsList[midPoz].getID()) < int(ID):
                return self.binarySearch(objectsList, midPoz + 1, right, ID)
        else:
            return -1
