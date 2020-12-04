from Domain.Entity import Entity


class ClientCard(Entity):
    # Initialization builtin
    def __init__(self, ID, surname, forename, CNP, dateOfBirth, registrationDate, deleteStatus):
        # self.__ID = ID
        super().__init__(ID)
        self.__surname = surname
        self.__forename = forename
        self.__CNP = CNP
        self.__dateOfBirth = str(dateOfBirth)
        self.__registrationDate = registrationDate
        self.__deleteStatus = deleteStatus
    '''
    # Gets the ID of the Client Card
    def getID(self):
        return self.__ID
    '''
    # Gets the Surname of the Client Card
    def getSurname(self):
        return self.__surname

    # Gets the Forename of the Client Card
    def getForename(self):
        return self.__forename

    # Gets the CNP of the Client Card
    def getCNP(self):
        return self.__CNP

    # Gets the Date of birth of the Client Card
    def getDateOfBirth(self):
        return self.__dateOfBirth

    # Gets the Registration date of the Client Card
    def getRegistrationDate(self):
        return self.__registrationDate

    # Gets the Delete Status of a Client Card
    def getDeleteStatus(self):
        return self.__deleteStatus

    # Sets the ID of the Client Card
    def setID(self, newID):
        self.__ID = newID

    # Sets the Surname of the Client Card
    def setSurname(self, newSurname):
        self.__surname = newSurname

    # Sets the Forename of the Client Card
    def setForename(self, newForename):
        self.__forename = newForename

    # Sets the CNP of the Client Card
    def setCNP(self, newCNP):
        self.__CNP = newCNP

    # Sets the Date of birth of the Client Card
    def setDateOfBirth(self, newDateOfBirth):
        self.__dateOfBirth = newDateOfBirth

    # Sets the Registration date of the Client Card
    def setRegistrationDate(self, newRegistrationDate):
        self.__registrationDate = newRegistrationDate

    # Sets the Delete Status of the Client Card
    def setDeleteStatus(self, newDeleteStatus):
        self.__deleteStatus = newDeleteStatus

    # Equal builtin
    def __eq__(self, other):
        if not isinstance(other, ClientCard):
            return False
        return self.getID() == other.getID() \
                and self.getSurname() == other.getSurname() \
                and self.getForename() == other.getForename() \
                and self.getCNP() == other.getCNP() \
                and self.getDateOfBirth() == other.getDateOfBirth() \
                and self.getRegistrationDate() == other.getRegistrationDate() \
                and self.getDeleteStatus() == other.getDeleteStatus()

    # Not equal builtin
    def __ne__(self, other):
        return not self.__eq__(other)

    # String formating buitlin
    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}".format(str(self.getID()),
                                                 self.getSurname(),
                                                 self.getForename(),
                                                 self.getCNP(),
                                                 self.getDateOfBirth(),
                                                 self.getRegistrationDate(),
                                                 self.getDeleteStatus())

    # Returns the string builtin
    def __repr__(self):
        return self.__str__()
