import select
import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('localhost', 33310))
except:
    print("Server не отвечает")
else:
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
                client_socket.send(message.encode("utf-8"))
            else:
                data = client_socket.recv(1024)
                print(data.decode("utf-8"))
    except KeyboardInterrupt:
        print("Ctr + С. Выход из программы клиента")
    except Exception as e:
        print("Exc сервер отключили", e)

finally:
    print("Работа прекращена")
    client_socket.close()
