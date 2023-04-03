import socket

IP = "127.0.0.1"
PORT = 1234
client_id = 'mockclient'  # hardcoded client ID: has to be in subscribed users list

# create socket
server_address = ("127.0.0.1", 1234)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET = internet, SOCK_DGRAM = UDP
print("Socket successfully created")  # debug

# HELLO
hello_message = f'HELLO({client_id})'  # protocol message: syntax may be changed
client_socket.sendto(hello_message.encode(), server_address)
response, server_address = client_socket.recvfrom(1024) # Wait for the server to respond
print("Server says: " + response.decode())  # Debug

# close the socket
client_socket.close()

#create tcp socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5678
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((TCP_IP, TCP_PORT))

tcp_client.send("Hello Server!".encode('utf-8'))
print(tcp_client.recv(1024).decode('utf-8'))
tcp_client.send("Bye!".encode('utf-8'))
print(tcp_client.recv(1024).decode('utf-8'))
tcp_client.close()
