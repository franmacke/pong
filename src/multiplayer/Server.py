
import socket
import _thread
import pickle
from src.model.ball.Ball import Ball
from src.model.player.Player import Player
from src.model.position.Position import Position
from src.model.game.Game import Game

import pygame

MAX_BYTES = 2048

class Server:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ""
        self.port = 5555
        self.addr = (self.address, self.port)
        self.game = None
        self.connected = 0
        self.clock = pygame.time.Clock()

    def setupGame(self):
        self.game = Game()
        self.game.initialize()

    def start(self):
        self.setupGame()
        self.bind()
        self.socket.listen(2)
        print("Waiting for a connection, Server Started")

    def update(self):
        self.game.update()

    def bind(self):
        try:
            self.socket.bind(self.addr)
        except socket.error as error:
            print(str(error))

    def sendGameData(self, playerNumber):
        playerRequesting = self.game.getPlayer(playerNumber)
        playerOpponent = None
        ball = self.game.getBall()

        if playerNumber == 1:
            playerOpponent = self.game.getPlayer(0)
        else:
            playerOpponent = self.game.getPlayer(1)

        score = self.game.getScoreManager()

        return pickle.dumps([playerRequesting, playerOpponent, ball, score])

    def threadedClient(self, connection, playerNumber):
        # Conexion inicial
        connection.send(self.sendGameData(playerNumber))

        while True:
            try:
                playerData = pickle.loads(connection.recv(MAX_BYTES * 10000))
                player = self.game.getPlayer(playerNumber)
                player.setPosition(playerData.getPosition())

                if not playerData:
                    print("Disconnected")
                    break

                connection.sendall(self.sendGameData(playerNumber))
            except:
                break
        
        self.connected -= 1
        print("Lost connection")
        connection.close()

    def loop(self):
        self.start()

        while True:
            conn, addr = self.socket.accept()
            print("Connected to:", addr)

            _thread.start_new_thread(self.threadedClient, (conn, self.connected))
            self.connected += 1

            if (self.connected == 2):
                self.startGame()


    def startGame(self):
        while self.connected == 2 or self.game.detectWinner():
            self.clock.tick(60)
            self.update()