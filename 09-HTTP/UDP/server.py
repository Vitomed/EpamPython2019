import re, socket, time

host = socket.gethostbyname(socket.gethostname())  # 127.0.1.1
port = 6060
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
addr_list = []  # [addr]
clients = {}  # {name: addr}
quit = False
help_msg = """
* Чтобы написать ЛС участнику чата, необходимо написать команду:
                `name` текст сообщения 
где name - это имя клиента, которому хочешь написать

* Чтобы покинуть чат, нужно нажать ctrl+C

* Посмотри всех участников чата, напиши слово:
				clients"""

print("[Server started]")
while not quit:
    try:
        data, addr = s.recvfrom(1024)  # max data size

        if addr not in addr_list:
            addr_list.append(addr)
            start_name, stop_name = "[", "]"
            index_start_name = data.decode("utf-8").find(start_name) + 1
            index_stop_name = data.decode("utf-8").find(stop_name)
            client_name = data.decode("utf-8")[index_start_name:index_stop_name]
            clients[client_name] = addr
            print("clients", clients)
        else:
            for name, port_value in clients.items():
                if addr == port_value:
                    client_name = name

        itistime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print(f"[{addr[0]}]==[{addr[1]}]==[{itistime}]/", end="")
        print(data.decode("utf-8"))

        data_list_elements = data.decode("utf-8").partition(" ")

        pattern = "`\w+`"
        result_pattern_action = re.findall(pattern, data_list_elements[-1])
        private_client_name = result_pattern_action[0].replace("`", "") if bool(result_pattern_action) else "empty_name"

        if private_client_name in clients:
            private_message = f"ЛС {data_list_elements[0]} " + data_list_elements[-1].replace(result_pattern_action[0],
                                                                                              "")
            s.sendto(private_message.encode("utf-8"), clients[private_client_name])
            print("Успешно отправлено")

        elif "help" in data.decode("utf-8"):
            s.sendto("help".encode("utf-8"), clients[client_name])

        elif "clients" in data.decode("utf-8"):
            try:
                s.sendto(str([i for i in clients.keys()]).encode("utf_8"), clients[client_name])
            except Exception as e:
                print("Exc List of client", e)
        else:
            for client in addr_list:
                if addr != client:
                    s.sendto(data, client)
            if "left chat" in data.decode(("utf-8")):
                clients.pop(client_name)
                addr_list.remove(addr)
                print("after pop", clients)
                print("after remove", addr_list)
    except:
        print("\n[Server stop]")
        quit = True

s.close()

