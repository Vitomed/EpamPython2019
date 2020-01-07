import socket

# Creat the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3310))
server.listen(1)
print("Server is running on port 3310:")
while True:
    clientsocket, clientaddress = server.accept()
    print("Received the connection from:", clientaddress)
    while True:
        data = clientsocket.recv(512).decode("utf-8")
        print(data)
        newdata = "Data from server".encode("utf-8")
        clientsocket.send(newdata)
