import pickle
import socket

MAX_BYTES = 2048

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.8"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connection = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(MAX_BYTES))
        except:
            return False

    def getConnection(self):
        return self.connection

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(MAX_BYTES * 10000))
        except socket.error as e:
            print(e)