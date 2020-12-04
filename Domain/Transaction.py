from Domain.Entity import Entity


class Transaction(Entity):
    # Initialization builtin
    def __init__(self, ID, medID, cardID, amount, date, clock, deleteStatus):
        # self.__ID = ID
        super().__init__(ID)
        self.__medID = medID
        self.__cardID = cardID
        self.__amount = amount
        self.__date = date
        self.__clock = clock
        self.__deleteStatus = deleteStatus
    '''
    # Gets the ID of the transaction
    def getID(self):
        return self.__ID
    '''
    # Gets the Medication's ID from the transaction
    def getMedID(self):
        return self.__medID

    # Gets the Card's ID of the client from the transaction
    def getCardID(self):
        return self.__cardID

    # Gets the amount of meds from the transaction
    def getAmount(self):
        return self.__amount

    # Gets the Date of the transaction
    def getDate(self):
        return self.__date

    # Gets the Clock of the transaction
    def getClock(self):
        return self.__clock

    # Gets the Delete Status of a Client Card
    def getDeleteStatus(self):
        return self.__deleteStatus

    # Sets the Medication's ID from the transaction
    def setMedID(self, MedID):
        self.__medID = MedID

    # Sets the Card's ID of the client from the transaction
    def setCardID(self, CardID):
        self.__cardID = CardID

    # Sets the amount of meds from the transaction
    def setAmount(self, newAmount):
        self.__amount = newAmount

    # Sets the Date of the transaction
    def setDate(self, newDate):
        self.__date = newDate

    # Sets the Clock of the transaction
    def setClock(self, newClock):
        self.__clock = newClock

    # Sets the Delete Status of the Client Card
    def setDeleteStatus(self, newDeleteStatus):
        self.__deleteStatus = newDeleteStatus

    # Equal builtin
    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False
        return self.getID() == other.getID() \
                and self.getMedID() == other.getMedID() \
                and self.getCardID() == other.getCardID() \
                and self.getAmount() == other.getAmount() \
                and self.getDate() == other.getDate() \
                and self.getClock() == other.getClock() \
                and self.getDeleteStatus() == other.getDeleteStatus()

    # Not equal builtin
    def __ne__(self, other):
        return not self == other

    # String formating buitlin
    def __str__(self):
        if self.getID() < 10:
            return "{}  |   {}    |     {}     |    {}   | {} | {} | {}".format(str(self.getID()),
                                                                                    self.getMedID(),
                                                                                    self.getCardID(),
                                                                                    self.getAmount(),
                                                                                    self.getDate(),
                                                                                    self.getClock(),
                                                                                    self.getDeleteStatus())
        else:
            return "{} |   {}    |     {}     |    {}   | {} | {} | {}".format(str(self.getID()),
                                                                                   self.getMedID(),
                                                                                   self.getCardID(),
                                                                                   self.getAmount(),
                                                                                   self.getDate(),
                                                                                   self.getClock(),
                                                                                   self.getDeleteStatus())

    # Returns the string builtin
    def __repr__(self):
        return self.__str__()
