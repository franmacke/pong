from abc import abstractmethod

class Observable:

    @abstractmethod
    def addObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass
