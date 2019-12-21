import socket
import select
import queue
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 50002))

import socket
import sys
import select
import time


user = input('your name: ')
mess_name = "your name " + user
client_socket.send(mess_name.encode("utf-8"))
try:
    while True:
        r, w, x = select.select([sys.stdin, client_socket], [], [])
        if not r:
            continue
        if r[0] is sys.stdin:
            message = input("")
            if message == "quit":
                client_socket.close()
            # elif message == "":
            #     pass
            client_socket.send(message.encode("utf-8"))
            # sys.stdout.write("")
            # sys.stdout.flush()
        else:
            data = client_socket.recv(1024)
            print("message from server:", data.decode("utf-8"))
except KeyboardInterrupt:
    print("Ctr + С. Выход из программы клиента")
finally:
    client_socket.close()


