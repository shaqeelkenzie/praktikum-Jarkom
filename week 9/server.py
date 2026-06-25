from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Web server berjalan di port", serverPort)

while True:
    print('Meluncurr...')

    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        
        filename = message.split()[1]
        
        f = open(filename[1:])
        outputdata = f.read()
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        
        connectionSocket.close()
serverSocket.close()