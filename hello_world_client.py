import socket

# Get input to define server host address
server_address = input('Server IP Address: ')
server_port = int(input('Server Port: '))

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
s.connect((server_address, server_port))
# Recieve message from server
msg = s.recv(1024)
# Decode and print message
print(msg.decode("utf-8"))