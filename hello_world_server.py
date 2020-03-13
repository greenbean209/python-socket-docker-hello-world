import socket
import select

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind port and listen
address = "0.0.0.0"
port = 2222
server_socket.bind((address, port))
server_socket.listen()
print(f'Listening for connections on {address}:{port}...')

# List of sockets for select.select()
sockets_list = [server_socket]

while True:
     # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    read_sockets, _, exception_sockets = select.select(sockets_list, [], [])

    # Iterate over notified sockets
    for notified_socket in read_sockets:
        clientsocket, clientaddress = notified_socket.accept()
        print(f"Connection from {clientaddress} has been establised!")
        clientsocket.send(bytes("Hello World", "utf-8"))
        clientsocket.close()