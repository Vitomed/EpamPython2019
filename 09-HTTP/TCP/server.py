import select, socket, sys, queue, time
from collections import deque

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 33310))
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}
my_users_socket = {}
remove_sockets = {}
help_msg = """
* Чтобы написать ЛС участнику чата, необходимо написать команду ЛС name, 
где name - это имя клиента, которому хочешь написать

* Чтобы покинуть чат, нужно нажать ctrl+C

* Посмотри всех участников чата, напиши слово:
				clients"""

try:
    while inputs:

        readable_sock, writable_sock, exceptional = select.select(
            inputs, outputs, inputs)

        for s in readable_sock:
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

        for s in writable_sock:
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

                elif next_msg == "help":
                    s.send((help_msg).encode("utf-8"))


                elif "ЛС" in next_msg:
                    try:
                        client_name = next_msg.split(" ")[1]
                    except Exception as e:
                        print("exc", e)
                    else:
                        if client_name in my_users_socket.values():
                            message = next_msg.replace(client_name, f">> {my_users_socket[s]}:")
                            for sock, name in my_users_socket.items():
                                if name == client_name and name != my_users_socket[s]:
                                    print(f"ЛС можно отправить {client_name}")
                                    sock.send(message.encode("utf-8"))
                        else:
                            s.send(f"{client_name} вышел из чате".encode("utf-8"))

                elif "your name" in next_msg:
                    name_user = next_msg.split(" ")[-1]
                    my_users_socket[s] = name_user
                    print("my_users socket", my_users_socket)
                    for sock in inputs:
                        if sock != server and sock != s:
                            sock.send(f"Подключился пользователь по имени: {name_user}".encode("utf-8"))

                elif "quit" == next_msg:
                    s.close()
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    for sock in inputs:
                        if sock != server:
                            print("Из чата вышел: ", my_users_socket[s])
                            sock.send(f"Из чата вышел: {my_users_socket[s]}".encode("utf-8"))
                    del message_queues[s]
                    del my_users_socket[s]

                else:
                    for sock in inputs:
                        if sock != server and sock != s:
                            message_from_username = my_users_socket[s]
                            print("message from username", message_from_username)
                            sock.send(f">> {message_from_username}: {next_msg}".encode("utf-8"))

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]
finally:
    sys.exit()
