class Entity:
    def __init__(self, ID):
        if not isinstance(ID, int):
            raise ValueError("Program: Error! Invalid ID.")
        self.__ID = ID

    def getID(self):
        return self.__ID
