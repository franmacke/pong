from abc import abstractmethod

class Sizable:

    @abstractmethod
    def getHeight(self):
        pass

    @abstractmethod
    def getWidth(self):
        pass