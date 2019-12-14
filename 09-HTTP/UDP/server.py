import re, socket, time

host = socket.gethostbyname(socket.gethostname())  # 127.0.1.1
port = 6060

addr_list = []  # [addr]
clients = {}  # {name: addr}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
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

        itistime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print(f"[{addr[0]}]==[{addr[1]}]==[{itistime}]/", end="")
        print(data.decode("utf-8"))

        data_list_elements = data.decode("utf-8").partition(" ")

        pattern = "`\w+`"
        result_pattern_action = re.findall(pattern, data_list_elements[-1])
        if result_pattern_action:
            private_client_name = result_pattern_action[0].replace("`", "")

        private_client_name = result_pattern_action[0].replace("`", "") if bool(result_pattern_action) else "empty_name"
        if private_client_name in clients:
            private_message = f"ЛС {data_list_elements[0]} " + data_list_elements[-1].replace(result_pattern_action[0],
                                                                                              "")
            s.sendto(private_message.encode("utf-8"), clients[private_client_name])
            print("Успешно отправлено")

        elif "List of clients" in data.decode("utf-8"):
            s.sendto(str([i for i in clients.keys()]).encode("utf_8"), clients[client_name])

        else:
            for client in addr_list:
                if addr != client:
                    s.sendto(data, client)
    except:
        print("\n[Server stop]")
        quit = True

s.close()
