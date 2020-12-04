from Repository.RepositoryGeneric import *


class ServicesMedicine:
    def __init__(self, repositoryGeneric, medValidator):
        self.__repo = repositoryGeneric
        self.__validator = medValidator
        self.__undoList = []
        self.__redoList = []

    # description: adds a new medicine
    # input: ID - int, the ID of the medicine
    #        name - str, the name of the medicine
    #        producer - str, the name of the producer
    #        price - float, the price of the med
    #        prescription - True if the med requires a prescription, False if NOT
    #        deleteStatus - True if it is available, False if NOT
    def addMeds(self, ID, name, producer, price, prescription, deleteStatus):
        medicine = Medicine(ID, name, producer, price, prescription, deleteStatus)
        self.__repo.addMed(medicine)
        self.__undoList.append(lambda: self.__repo.deleteMed(medicine))
        self.__redoList.append(lambda: self.__repo.addMed(medicine))

    # description: modifies a car and updates it
    # input: ID - int, the ID of the medicine
    #        newName - str, the new name of the medicine
    #        newProducer - str, the new name of the producer
    #        newPrice - float, the new price of the med
    #        newPrescription - True if the new med comes with a prescription, False if NOT
    #        newDeleteStatus - True if it is available, False if NOT
    def updateMeds(self, ID, newName, newProducer, newPrice, newPrescription, newDeleteStatus):
        for med in self.getAllMeds():
            if med.getID() == ID:
                medCopy = med
        medicine = Medicine(ID, newName, newProducer, newPrice, newPrescription, newDeleteStatus)
        self.__undoList.append(lambda: self.__repo.updateMed(medCopy))
        self.__redoList.append(lambda: self.__repo.updateMed(medicine))
        self.__repo.updateMed(medicine)

    # description: removes a med
    # input: ID - int, the ID of the med
    def removeMeds(self, ID):
        medList = self.__repo.getAllMeds()
        for med in medList:
            if med.getID() == ID:
                medCopy = med
                self.__undoList.append(lambda: self.__repo.addMed(medCopy))
                self.__redoList.append(lambda: self.__repo.deleteMed(med))
                self.__repo.deleteMed(med)
                break

    # description: returns all the meds
    def getAllMeds(self):
        return self.__repo.getAllMeds()

    # populates the repository
    def populateTheRepository(self, howMany):
        self.__repo.populateRepository(howMany)

    # desc: applies an increase to meds
    # input: value - the minimum value
    #        percentage - the increase percentage
    def apllyPriceIncreaseToMeds(self, value, percentage):
        medsList = self.__repo.getAllMeds()
        medsList = list(filter(lambda x: float(x.getPrice()) > value, medsList))
        for med in medsList:
            medID = med.getID()
            medName = med.getName()
            medProducer = med.getProducer()
            medPrice = float(med.getPrice())
            medPrescription = med.getPrescription()
            deleteStatus = med.getDeleteStatus()
            newMedPrice = medPrice + medPrice * percentage / 100
            self.updateMeds(medID, medName, medProducer, "{0:.2f}".format(newMedPrice), medPrescription, deleteStatus)

    # desc: undoes the command for the med
    def doUndoMed(self):
        if len(self.__undoList) == 1:
            self.__redoList.reverse()
        if len(self.__undoList) == 0:
            print("Program: There are no commands to be undone.")
        else:
            op = self.__undoList.pop()
            op()

    # desc: redoes the command for the med
    def doRedoMed(self):
        if len(self.__redoList) == 0:
            print("Program: There are no commands to be redone.")
        else:
            op = self.__redoList.pop()
            op()
