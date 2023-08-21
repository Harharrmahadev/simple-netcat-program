import socket


host = input("Enter client Address: ")
port = int(input("Enter port: "))

#creating socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Binding server 
s.bind((host,port))
# Listening to 1 client
s.listen(1)

# Accepting connection from client
client,addr = s.accept()

while True:
	cmd = input("$ ")
	client.send(cmd.encode())
	if cmd == "exit":
		print("exiting out of shell \nConnection closed....")
		break
	print(client.recv(4096).decode())

client.close()
s.close()
