import socket

# Get input to define server host address
server_address = input('Server IP Address: ')
server_port = int(input('Server Port: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_address, server_port))

msg = s.recv(1024)
print(msg.decode("utf-8"))