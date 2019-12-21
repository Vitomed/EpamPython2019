import select, socket, sys, queue, time
from collections import deque
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 50002))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}
my_users = {}
remove_sockets = {}

try:
    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = queue.Queue()
                time.sleep(0.1)
            else:
                data = s.recv(1024)
                print("server data", data)
                print("inputs", inputs)
                if data:
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                        print("outputs", outputs)
                else:
                    print("отключился сокет", s)
                    message_queues[s].put("quit".encode("utf-8"))
                    if s not in outputs:
                        outputs.append(s)
                    # s.close()
        print("write", writable)
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
                print("next_msg", next_msg)
                print("quit" == next_msg)
            except queue.Empty:
                outputs.remove(s)
            except Exception as e:
                print(f"Exc {e}")
            else:
                next_msg = next_msg.decode("utf-8")
                if next_msg == "clients":
                    message = [i for i in my_users.values()]
                    s.send(("Список всех участников чата: " + str(message)).encode("utf-8"))
                elif next_msg == "ЛС":
                    s.send("Личное сообщение".encode("utf-8"))
                    for sock in inputs:
                        pass
                elif "your name" in next_msg:
                    name_user = next_msg.split(" ")[-1]
                    my_users[s] = name_user
                    print("my_users", my_users)
                    s.send(f"Подключился пользователь по имени: {name_user}".encode("utf-8"))
                    # for sock in inputs:
                    #     if sock != server and sock != s:
                    #         s.send("Подключился пользователь по имени".encode("utf-8"))
                elif "quit" == next_msg:
                    s.close()
                    # remove_sockets[s] = my_users[s]
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    # del my_users[s]
                    del message_queues[s]
                    for sock in inputs:
                        if sock != server:
                            # print("Нас покинул участник", remove_sockets[s])
                            # sock.send(f"Из чата вышел {remove_sockets[s]}".encode("utf-8"))
                            print("Нас покинул участник", my_users[s])
                            sock.send(f"Из чата вышел {my_users[s]}".encode("utf-8"))
                            # remove_sockets.pop(s)
                            del my_users[s]

                else:
                    # s.send(next_msg.encode("utf-8"))
                    time.sleep(1)
                    for sock in inputs:
                        if sock != server and sock != s:
                            message_from_username = my_users[s]
                            print("message from username", message_from_username)
                            sock.send(f"Сообщение в общем чате от {message_from_username}".encode("utf-8"))

        print("exceptional", exceptional)
        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]
except Exception:
    sys.exit()
finally:
    sys.exit()