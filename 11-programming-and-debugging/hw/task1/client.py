import socket, time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 3310))
while True:
    data = "Data from client".encode("utf-8")
    client.send(data)
    time.sleep(4)
    print(client.recv(512).decode("utf-8"))
