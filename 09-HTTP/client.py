import socket, threading, time

key = 6632  # ключ для шифрования данных
shutdown = False
join = False

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                # Симметричное шифрование сообщений
                # Расшифровка
                decrypt = ""
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt = chr(ord(i)^key)
                print(decrypt)
                # Пауза между отправками
                time.sleep(0.2)
        except Exception:
            pass


# Содержит в себе IP
host = socket.gethostbyname(socket.gethostname())
# Клиент подключается к сети и не создает ее, поэтому порт 0
port = 0

server = ("127.0.1.1", 6060)  # 192.168.0.118
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

chat_threading = threading.Thread(target=receving, args=("ChatThread", s))
chat_threading.start()

while shutdown == False:
    if join == False:
        s.sendto(f"[{alias}] => join chat".encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            # Симметричное шифрование сообщений
            # Зашифровка
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt

            if message != "":
                s.sendto(f"[{alias}] :: {message}".encode("utf-8"), server)
            time.sleep(0.2)
        except Exception:
            s.sendto(f"[{alias}] <= left chat".encode("utf-8"), server)
            shutdown = True

chat_threading.join()
s.close()

import socket, threading, time

key = 8194

shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                # print(data.decode("utf-8"))

                # Begin
                decrypt = "";
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)
                # End

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.101", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            # Begin
            crypt = ""
            for i in message:
                crypt += chr(ord(i) ^ key)
            message = crypt
            # End

            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()