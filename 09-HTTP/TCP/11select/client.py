import socket
import select
import queue
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 50000))

# try:
#     while True:
#         msg = input("msg: ")
#         client_socket.send(msg.encode("utf-8"))
#         data = client_socket.recv(1024)
#         if data:
#             print("data:", repr(data))
#         else:
#             print("continue")
# except:
#     client_socket.close()
#     sys.exit()



# inputs = [client_socket]
# outputs = []
# message_queues = {}
#
# while inputs:
#     readable, writable, exceptional = select.select(
#         inputs, outputs, inputs)
#     for client in readable:
#         if client is client:
#             connection.setblocking(0)
#             inputs.append(connection)
#             message_queues[connection] = queue.Queue()
#         else:
#             data = s.recv(1024)
#             print("server data", data)
#             if data:
#                 message_queues[s].put(data)
#                 if s not in outputs:
#                     outputs.append(s)
#             else:
#                 if s in outputs:
#                     outputs.remove(s)
#                 inputs.remove(s)
#                 s.close()
#                 del message_queues[s]
#
#     for s in writable:
#         try:
#             next_msg = message_queues[s].get_nowait()
#         except queue.Empty:
#             outputs.remove(s)
#         else:
#             s.send(next_msg)
#
#     for s in exceptional:
#         inputs.remove(s)
#         if s in outputs:
#             outputs.remove(s)
#         s.close()
#         del message_queues[s]

import socket
import sys
import select
import time


user = input('your name: ')
message = "your name " + user
client_socket.send(message.encode("utf-8"))
time.sleep(2)
while True:
    r, w, x = select.select([sys.stdin, client_socket], [], [])
    print("r", r)
    print("w", w)
    if not r:
        continue
    if r[0] is sys.stdin:
        message = input()
        # message = sys.stdout.write()
        if message == "quit":
            # client_socket.send("{user} <= left chat".format(user=user).encode("utf-8"))
            client_socket.close()
            break
        # elif message == "":
        #     pass
        client_socket.send(message.encode("utf-8"))
        sys.stdout.write('your message: ')
        sys.stdout.flush()
    else:
        data = client_socket.recv(1024)
        print("message from server:", data.decode("utf-8"))