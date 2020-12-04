from Domain.Entity import Entity


class Medicine(Entity):
    # Initialization builtin
    def __init__(self, ID, name, producer, price, prescription, deleteStatus):
        # self.__ID = ID
        super().__init__(ID)
        self.__name = name
        self.__producer = producer
        self.__price = price
        self.__prescription = prescription
        self.__deleteStatus = deleteStatus
    '''
    # Gets the ID of the Medicine
    def getID(self):
        return self.__ID
    '''
    # Gets the Name of the Medicine
    def getName(self):
        return self.__name

    # Gets the Producer of the Medicine
    def getProducer(self):
        return self.__producer

    # Gets the Price of the Medicine
    def getPrice(self):
        return self.__price

    # Gets the Prescription of the Medicine
    def getPrescription(self):
        return self.__prescription

    # Gets the Delete Status of a Client Card
    def getDeleteStatus(self):
        return self.__deleteStatus

    # Sets the Name of the Medicine
    def setName(self, newName):
        self.__name = newName

    # Sets the Producer of the Medicine
    def setProducer(self, newProducer):
        self.__producer = newProducer

    # Sets the Price of the Medicine
    def setPrice(self, newPrice):
        self.__price = newPrice

    # Sets the Prescription of the Medicine
    def setPrescription(self, newPrescription):
        self.__prescription = newPrescription

    # Sets the Delete Status of the Client Card
    def setDeleteStatus(self, newDeleteStatus):
        self.__deleteStatus = newDeleteStatus

    # Equal builtin
    def __eq__(self, other):
        if not isinstance(other, Medicine):
            return False
        return self.getID() == other.getID() \
                and self.getName() == other.getName() \
                and self.getProducer() == other.getProducer() \
                and self.getPrice() == other.getPrice() \
                and self.getPrescription() == other.getPrescription() \
                and self.getDeleteStatus() == other.getDeleteStatus()

    # Not equal builtin
    def __ne__(self, other):
        return not self == other

    # String formating buitlin
    def __str__(self):
        return "{}|{}|{}|{}|{}|{}".format(str(self.getID()),
                                              self.getName(),
                                              self.getProducer(),
                                              float(self.getPrice()),
                                              self.getPrescription(),
                                              self.getDeleteStatus())

    # Returns the string builtin
    def __repr__(self):
        return self.__str__()
