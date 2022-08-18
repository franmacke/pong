from src.model.observer.Observable import Observable

class Score(Observable):
    def __init__(self, playerList) -> None:
        self.playerList = playerList
        self.dictScore = self.initScore()
        self.observers = []
        self.maxScore = 2

    def initScore(self) -> dict:
        dict = {}

        for player in self.playerList:
            dict.update({player.id: 0})

        return dict

    def score(self, player):
        self.dictScore.update(
            {player.id: self.dictScore.get(player.id) + 1}
        )
        self.notifyObservers()

    def setScore(self, newScore):
        self.dictScore = newScore

    def addObserver(self, observer):
        self.observers.append(observer)

    def getScoreList(self):
        return self.dictScore

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.getScoreList())

    def getWinner(self):
        for key in self.dictScore:
            if self.dictScore.get(key) == self.maxScore:
                return key
        return None