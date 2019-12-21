import select, socket, sys, queue, time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}
my_users = {}
count = 0
try:
    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        count += 1
        print("count", count)
        print("read", readable)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = queue.Queue()
                time.sleep(0.2)

            else:
                # if "your name" in s.recv(1024).decode("utf-8"):
                #     name_user = s.recv(1024).decode("utf-8")
                #     name_user = name_user.split(" ")[-1]
                #     print(name_user)
                #     my_users[name_user] = inputs[-1]
                #     print("my_users", my_users)
                # else:
                data = s.recv(1024)

                print("server data", data)
                print("inputs", inputs)
                # if "your name" in data.decode("utf-8"):
                #     name_user = s.recv(1024).decode("utf-8")
                #     name_user = name_user.split(" ")[-1]
                #     my_users[name_user] = inputs[-1]
                #     print("my_users", my_users)
                if data:
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]
        print("write", writable)
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                outputs.remove(s)
            else:
                next_msg = next_msg.decode("utf-8")
                if next_msg == "clients":
                    s.send("Список всех участников чата".encode("utf-8"))
                elif next_msg == "ЛС":
                    s.send("Личное сообщение".encode("utf-8"))

                    for sock in inputs:
                        pass
                else:
                    print("write msg", next_msg)
                    s.send(next_msg.encode("utf-8"))
                    time.sleep(2)
                    for sock in inputs:
                        if sock != server and sock != s:
                            sock.send("Подключился новый пользователь".encode("utf-8"))

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