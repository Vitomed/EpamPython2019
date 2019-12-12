import socket, time

host = socket.gethostbyname(socket.gethostname())  # 127.0.1.1 IP-шник
port = 6060

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print("Server started")

while not quit:
    try:
        data, addr = s.recvfrom(1024)  # max data size
        if addr not in clients:
            clients.append(addr)
        itistime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print(f"[{addr[0]}]==[{addr[1]}==[{itistime}]", end="")
        print(data.decode("utf-8"))
        # Отправитель не должен получать свои сообщения. Делаем проверку.
        for client in clients:
            if addr != client:
                s.sendto(data, client)

    except Exception:
        print("\nServer stop")
        quit = True

s.close()



