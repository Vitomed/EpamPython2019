import socket, time, re

host = socket.gethostbyname(socket.gethostname())  # 127.0.1.1 IP-шник
port = 6060

clients = []
clients_2 = {}

# def server(host, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((host, port))
#
#     while not quit:
#         try:
#             data, addr = s.recvfrom(1024)  # max data size
#             print("Got data from", addr)
#             if addr not in clients:
#                 clients.append(addr)
#                 print("addr", addr)
#
#             for client in clients:
#                 if addr != client:
#                     sock.sendto(data, client)
#         except:
#             print("\n[Server stop]")
#             quit = True


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print("[Server started]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)  # max data size

        if addr not in clients:
            clients.append(addr)
            start_name, stop_name = "[", "]"
            index_start_name = data.decode("utf-8").find(start_name) + 1
            index_stop_name = data.decode("utf-8").find(stop_name)
            client_name = data.decode("utf-8")[index_start_name:index_stop_name]
            clients_2[client_name] = addr

        print("addr", addr)
        print("clients_2", clients_2)

        itistime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print(f"[{addr[0]}]==[{addr[1]}]==[{itistime}]/", end="")
        print(data.decode("utf-8"))

        # Отправитель не должен получать свои сообщения. Делаем проверку.
        # for client in clients:
        #     print("Data and clients", data.decode("utf-8") in clients_2)
        #     print("Data", data.decode("utf-8"))
        #     print("clients", data.decode("utf-8"))
        #     if addr != client:
        #         s.sendto(data, client)

        data_list_elements = data.decode("utf-8").partition(" ")

        pattern = "`\w+`"
        result_pattern_action = re.findall(pattern, data_list_elements[-1])
        if result_pattern_action:
            private_client_name = result_pattern_action[0].replace("`", "")

        private_client_name = result_pattern_action[0].replace("`", "") if bool(result_pattern_action) else "empty_name"
        if private_client_name in clients_2:
            private_message = f"ЛС {data_list_elements[0]} " + data_list_elements[-1].replace(result_pattern_action[0], "")
            s.sendto(private_message.encode("utf-8"), clients_2[private_client_name])
            print("Успешно отправлено")

        elif "List of clients" in data.decode("utf-8"):
            for client in clients:
                if addr == client:
                    s.sendto(str(clients_2).encode("utf-8"), client)
        else:
            for client in clients:
                if addr != client :
                    s.sendto(data, client)
    except:
        print("\n[Server stop]")
        quit = True

s.close()
