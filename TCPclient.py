from socket import *
import sys
from time import *



try:
    serverName = raw_input('Please enter server IP address: ')
    serverPort = 7
    # initiate 3 way handshake TCP connection with server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

except gaierror:
    print 'Error, could not connect with server'
    sys.exit(1)

while 1:
    sentence = raw_input('Input sentence: ')
    if sentence != 'terminate':
        # send TCP byte stream to server
        clientSocket.send(sentence)
        # receive TCP byte stream from server
        bufferSize = 2048
        receivedSentence = clientSocket.recv(bufferSize)
        print 'From Server: ', receivedSentence
    else:
        print 'Connection closing......'
        break

#close TCP connection
clientSocket.close()

