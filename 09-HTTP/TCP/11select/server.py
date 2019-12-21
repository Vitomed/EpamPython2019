import select, socket, sys, queue, time
from collections import deque
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 50000))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}
my_users_socket = {}
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
                    message = [i for i in my_users_socket.values()]
                    s.send(("Список всех участников чата: " + str(message)).encode("utf-8"))
                elif "ЛС" in next_msg:
                    try:
                        client_name = next_msg.split(" ")[1]
                    except Exception as e:
                        print("exc", e)
                    else:
                        if client_name in my_users_socket.values():
                            message = next_msg.replace(client_name, "")
                            for sock, name in my_users_socket.items():
                                if client_name == name:
                                    print(f"ЛС можно отправить {client_name}")
                                    sock.send(message.encode("utf-8"))
                        else:
                            s.send(f"{client_name} вышел из чате".encode("utf-8"))
                    for sock in inputs:
                        pass
                elif "your name" in next_msg:
                    name_user = next_msg.split(" ")[-1]
                    my_users_socket[s] = name_user
                    print("my_users socket", my_users_socket)
                    # s.send(f"Подключился пользователь по имени: {name_user}".encode("utf-8"))
                    for sock in inputs:
                        if sock != server and sock != s:
                            sock.send(f"Подключился пользователь по имени: {name_user}".encode("utf-8"))
                elif "quit" == next_msg:
                    s.close()
                    # remove_sockets[s] = my_users[s]
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    # del my_users[s]
                    for sock in inputs:
                        if sock != server:
                            print("Нас покинул участник", my_users_socket[s])
                            sock.send(f"Из чата вышел {my_users_socket[s]}".encode("utf-8"))
                    del message_queues[s]
                    del my_users_socket[s]

                else:
                    # time.sleep(1)
                    for sock in inputs:
                        if sock != server and sock != s:
                            message_from_username = my_users_socket[s]
                            print("message from username", message_from_username)
                            sock.send(f"Сообщение от {message_from_username}: {next_msg}".encode("utf-8"))

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