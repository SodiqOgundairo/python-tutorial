# sockets
# socets are used to communicate between computers
# server and client
# server listens for connections

# best practice to use try and except block to handle errors
# import socket module

# the protocols used in sockets are TCP and UDP
# TCP is connection oriented and reliable while UDP is connectionless and unreliable
# TCP is used for most applications while UDP is used for streaming and gaming
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept()
    print(f'Connected to {address}')
    client.send('You are connected'.encode())
    client.close()
