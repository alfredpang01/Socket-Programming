import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(1)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                response = data
                client.send(response)

            except:
                client.close()
                return False

if __name__ == "__main__":
    while 1:
        try:
            port_num = 7
            print 'The server is ready to receive'
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()
# open TCP socket to listen at well-known port


