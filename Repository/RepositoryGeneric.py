from Domain.Medicine import Medicine
from Domain.ClientCard import ClientCard
from Domain.Transaction import Transaction
from Repository.DuplicateIDException import DuplicateIDException
import random


class RepositoryGeneric:
    def __init__(self, fileMeds, fileClients, fileTransactions):
        self.__fileMeds = fileMeds
        self.__fileClients = fileClients
        self.__fileTransactions = fileTransactions
        self.__medicines = []
        self.__clientCards = []
        self.__transactions = []
        self.__transactions = self.__readFileTransactions()
        self.__clientCards = self.__readFileCards()
        self.__medicines = self.__readFileMeds()

    # description: reads the list of medicines and then returns it
    def __readFileMeds(self):
        medList = []
        f = open(self.__fileMeds, "r")
        lines = f.readlines()
        for line in lines:
            medString = line[:-1]  # deletes the last char from the string
            components = medString.split("|")
            ID = int(components[0])
            name = components[1]
            producer = components[2]
            price = components[3]
            if components[4] == "True":
                prescription = "True"
            else:
                prescription = "False"
            deleteStatus = components[5]
            medicine = Medicine(ID, name, producer, price, prescription, deleteStatus)
            medList.append(medicine)
        f.close()
        return medList

    # description: writes all the meds to the file
    # input: medList - list, the list of meds
    def __writeFileMeds(self, medList):
        f = open(self.__fileMeds, "w")
        content = ""
        for medicine in medList:
            line = "{}|{}|{}|{}|{}|{}\n".format(medicine.getID(),
                                                medicine.getName(),
                                                medicine.getProducer(),
                                                medicine.getPrice(),
                                                medicine.getPrescription(),
                                                medicine.getDeleteStatus())
            content += line
        f.write(content)
        f.close()

    # description: reads the list of client cards and then returns it
    def __readFileCards(self):
        cardsList = []
        f = open(self.__fileClients, "r")
        lines = f.readlines()
        for line in lines:
            cardString = line[:-1]  # deletes the last char from the string
            components = cardString.split("|")
            ID = int(components[0])
            surname = components[1]
            forename = components[2]
            CNP = components[3]
            birthOfDate = components[4]
            registrationDate = components[5]
            deleteStatus = components[6]
            clientCard = ClientCard(ID, surname, forename, CNP, birthOfDate, registrationDate, deleteStatus)
            cardsList.append(clientCard)
        f.close()
        return cardsList

    # description: writes all the client cards to the file
    # input: cardsList - list, the list of client cards
    def __writeFileCards(self, cardsList):
        f = open(self.__fileClients, "w")
        content = ""
        for clientCard in cardsList:
            line = "{}|{}|{}|{}|{}|{}|{}\n".format(clientCard.getID(),
                                                   clientCard.getSurname(),
                                                   clientCard.getForename(),
                                                   clientCard.getCNP(),
                                                   clientCard.getDateOfBirth(),
                                                   clientCard.getRegistrationDate(),
                                                   clientCard.getDeleteStatus())
            content += line
        f.write(content)
        f.close()

    # description: reads the list of transactions and then returns it
    def __readFileTransactions(self):
        transactionsList = []
        f = open(self.__fileTransactions, "r")
        lines = f.readlines()
        for line in lines:
            transactionString = line[:-1]  # deletes the last char from the string
            components = transactionString.split("|")
            ID = int(components[0])
            medID = components[1]
            cardID = components[2]
            amount = int(components[3])
            date = components[4]
            clock = components[5]
            deleteStatus = components[6]
            clientCard = Transaction(ID, medID, cardID, amount, date, clock, deleteStatus)
            transactionsList.append(clientCard)
        f.close()
        return transactionsList

    # description: writes all the transactions to the file
    # input: transaction - list, the list of transactions
    def __writeFileTransactions(self, transactionsList):
        content = ""
        f = open(self.__fileTransactions, "w")
        for transaction in transactionsList:
            line = "{}|{}|{}|{}|{}|{}|{}\n".format(transaction.getID(),
                                                   transaction.getMedID(),
                                                   transaction.getCardID(),
                                                   transaction.getAmount(),
                                                   transaction.getDate(),
                                                   transaction.getClock(),
                                                   transaction.getDeleteStatus())
            content += line
        f.write(content)
        f.close()

    # description: adds a client card to the list
    # input: clientCard - entity, the client card itself with all of its properties
    def addCard(self, clientCard):
        for card in self.__clientCards:
            if card.getID() == clientCard.getID():
                raise DuplicateIDException("Program: Invalid ID!")
        self.__clientCards.append(clientCard)
        self.__writeFileCards(self.__clientCards)

    # description: removes a client card from the list
    # input: clientCard - entity, the client card itself with all of its properties
    def removeCard(self, clientCard):
        clientCard.setDeleteStatus("Inactive")
        self.__writeFileCards(self.__clientCards)

    # description: removes a client card from the list
    # input: clientCard - entity, the client card itself with all of its properties
    def deleteCard(self, clientCard):
        self.__clientCards.remove(clientCard)
        self.__writeFileCards(self.__clientCards)

    # description: updates the client card with new properties
    # input: clientCard - entity, the client card itself with all of its properties
    def updateCard(self, clientCard):
        for index in range(0, len(self.__clientCards)):
            currentCard = self.__clientCards[index]
            if currentCard.getID() == clientCard.getID():
                self.__clientCards[index] = clientCard
                self.__writeFileCards(self.__clientCards)
                break

    # description: returns all the client cards
    # output: __clientCards - list, the client cards list
    def getAllCards(self):
        return self.__clientCards[:]

    # description: adds a med to the list
    # input: medicine - entity, the medicine itself with all of its properties
    def addMed(self, medicine):
        for med in self.__medicines:
            if med.getID() == medicine.getID():
                raise DuplicateIDException("Program: Invalid ID!")
        self.__medicines.append(medicine)
        self.__writeFileMeds(self.__medicines)

    # description: removes a med from the list
    # input: medicine - entity, the medicine itself with all of its properties
    def removeMed(self, medicine):
        medicine.setDeleteStatus("Inactive")
        self.__writeFileMeds(self.__medicines)

    # description: removes a med from the list
    # input: medicine - entity, the medicine itself with all of its properties
    def deleteMed(self, medicine):
        self.__medicines.remove(medicine)
        self.__writeFileMeds(self.__medicines)

    # description: updates the medicine with new properties
    # input: medicine - entity, the medicine itself with all of its properties
    def updateMed(self, medicine):
        for index in range(0, len(self.__medicines)):
            currentMed = self.__medicines[index]
            if currentMed.getID() == medicine.getID():
                self.__medicines[index] = medicine
                self.__writeFileMeds(self.__medicines)
                break

    # description: returns all the meds
    # output: __medicines - list, the medicines list
    def getAllMeds(self):
        return self.__medicines[:]

    def populateRepository(self, howMany):
        medsList = self.getAllMeds()
        medNamesList = ["Zinnat", "Ambroxol", "Sinupret", "Biorinil", "Azitrox", "Codeina",
                        "Theraflu", "Coldrex", "FluEnd Extreme", "Paracetamol", "Algocalmin",
                        "Nurofen", "Strepsils", "Drill"]
        producerNamesList = ["Biocodex", "Bayer Ph", "ASTA Medica", "Antibiotic CO.",
                             "Cosmo Pharm Inc", "Europharm", "Genepharm S.A.",
                             "Hexal Pharma", "Minden Pharma", "Pharco Pharmaceuticals",
                             "Sintofarm S.A.", "Troyapharm"]
        alreadyIDs = 0
        IDsList = []
        for med in medsList:
            alreadyIDs += 1
            IDsList.append(med.getID())
        ID = 1
        while howMany:
            while True:
                if ID not in IDsList:
                    IDsList.append(ID)
                    break
                else:
                    ID += 1
            rndInt = random.randint(0, len(medNamesList)-1)
            name = medNamesList[rndInt]
            rndInt = random.randint(0, len(producerNamesList)-1)
            producer = producerNamesList[rndInt]
            rndPrice = random.uniform(5.0, 100.0)
            price = float("{0:.2f}".format(rndPrice))
            prescription = random.randint(1, 2)
            if prescription == 1:
                prescription = "True"
            elif prescription == 2:
                prescription = "False"
            newMedicine = Medicine(ID, name, producer, price, prescription, "Active")
            self.addMed(newMedicine)
            howMany -= 1

    # description: adds a transaction to the list
    # input: transaction - entity, the transaction itself with all of its properties
    def addTransaction(self, transaction):
        for tran in self.__transactions:
            if tran.getID() == transaction.getID():
                raise DuplicateIDException("Program: Invalid ID!")
        self.__transactions.append(transaction)
        self.__writeFileTransactions(self.__transactions)

    # description: removes a transaction from the list
    # input: transaction - entity, the transaction itself with all of its properties
    def removeTransaction(self, transaction):
        transaction.setDeleteStatus("Inactive")
        self.__writeFileTransactions(self.__transactions)

    # description: removes a transaction from the list
    # input: transaction - entity, the transaction itself with all of its properties
    def deleteTransaction(self, transaction):
        self.__transactions.remove(transaction)
        self.__writeFileTransactions(self.__transactions)

    # description: updates the transaction with new properties
    # input: transaction - entity, the transaction itself with all of its properties
    def updateTransaction(self, transaction):
        for index in range(0, len(self.__transactions)):
            currentTransaction = self.__transactions[index]
            if currentTransaction.getID() == transaction.getID():
                self.__transactions[index] = transaction
                self.__writeFileTransactions(self.__transactions)
                break

    # description: returns all the transactions
    # output: __clientCards - list, the transactions list
    def getAllTransactions(self):
        return self.__transactions[:]
