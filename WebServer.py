from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
PortNumber= 8888
serverSocket.bind(('127.1.2.3', PortNumber))
serverSocket.listen(1)

while True:
    print ('Ready to serve....')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 200 OK  \r\n\r\n 404 Not Found".encode())
    connectionSocket.close()
serverSocket.close()
sys.exit()