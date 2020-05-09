import socket
import threading

from PyQt5.QtWidgets import QTableWidgetItem

class Server:

    def __init__(self, ip, port, ip_type=socket.AF_INET, sock_type=socket.SOCK_STREAM):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(ip_type, sock_type)
        self.sock.bind((ip, port))

        self.clients = []

    @staticmethod
    def get_address():
        import netifaces
        wlo = netifaces.ifaddresses('wlo1')
        ip = wlo[2][0]['addr']
        return (ip, 8888)

    def wait_connections(self, num_of_clients, table):
        self.sock.listen(num_of_clients)

        while len(self.clients) < num_of_clients:

            client, addr = self.sock.accept()

            nickname = client.recv(1024).decode('utf-8')
            client_data = {'nickname': nickname, 'addr': addr, 'sock': client}
            self.clients.append(client_data)

            self.update_table(table)

        self.send_all('start_game_screen')

    def send_all(self, signal):
        for client in self.clients:
            client['sock'].send(signal.encode())

    def update_table(self, table):
        for index, value in enumerate(self.clients):
            table.setItem(index, 0, QTableWidgetItem(value['nickname']))
            table.setItem(index, 1, QTableWidgetItem(value['addr'][0]))

