import socket
import logic.signals as signal


class Client:

    def __init__(self, ip, port, ip_type=socket.AF_INET, sock_type=socket.SOCK_STREAM):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(ip_type, sock_type)

    @staticmethod
    def parse_address(address):
        ip, port = address.split(':')
        return (ip, int(port))

    def connect_to_server(self):
        self.sock.connect((self.ip, self.port))

    def send_str(self, string):
        self.sock.send(string.encode())

    def start_game(self):
        result = self.sock.recv(1024).decode('utf-8')
        start_game_screen = signal.signals[result]
        start_game_screen()