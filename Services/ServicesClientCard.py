from Repository.RepositoryGeneric import *


class ServicesClientCard:
    def __init__(self, repositoryGeneric):
        self.__repo = repositoryGeneric
        self.__undoList = []
        self.__redoList = []

    # description: adds a new client card
    # input: ID - int, the ID of the client card
    #        surname - str, the surname of the client
    #        forename - str, the forename of the client
    #        CNP - int, the personal numerical code
    #        dateOfBirth - str, the date of birth
    #        registrationDate - str, the registration date of the client
    #        deleteStatus - str, the delete status of the client
    def addCards(self, ID, surname, forename, CNP, dateOfBirth, registrationDate, deleteStatus):
        clientCard = ClientCard(ID, surname, forename, CNP, dateOfBirth, registrationDate, deleteStatus)
        self.__repo.addCard(clientCard)
        self.__undoList.append(lambda: self.__repo.deleteCard(clientCard))
        self.__redoList.append(lambda: self.__repo.addCard(clientCard))

    # description: modifies a card and updates it
    # input: ID - int, the ID of the medicine
    #        newName - str, the new name of the medicine
    #        newProducer - str, the new name of the producer
    #        newPrice - float, the new price of the med
    #        newPrescription - True if the new med comes with a prescription, False if NOT
    #        newDeleteStatus - True if the client card is available, False if NOT
    def updateCards(self, ID, surname, forename, CNP, dateOfBirth, registrationDate, deleteStatus):
        for card in self.getAllCards():
            if card.getID() == ID:
                cardCopy = card
        clientCard = ClientCard(ID, surname, forename, CNP, dateOfBirth, registrationDate, deleteStatus)
        self.__undoList.append(lambda: self.__repo.updateCard(cardCopy))
        self.__redoList.append(lambda: self.__repo.updateCard(clientCard))
        self.__repo.updateCard(clientCard)

    # description: removes a card
    # input: ID - int, the ID of the card
    def removeCards(self, ID):
        cardsList = self.__repo.getAllCards()
        for card in cardsList:
            if card.getID() == ID:
                cardCopy = card
                self.__undoList.append(lambda: self.__repo.addCard(cardCopy))
                self.__redoList.append(lambda: self.__repo.deleteCard(card))
                self.__repo.deleteCard(card)
                break

    # description: returns all the meds
    def getAllCards(self):
        return self.__repo.getAllCards()

    def doUndoCard(self):
        if len(self.__undoList) == 1:
            self.__redoList.reverse()
        if len(self.__undoList) == 0:
            print("Program: There are no commands to be undone.")
        else:
            op = self.__undoList.pop()
            op()

    def doRedoCard(self):
        if len(self.__redoList) == 0:
            print("Program: There are no commands to be redone.")
        else:
            op = self.__redoList.pop()
            op()

