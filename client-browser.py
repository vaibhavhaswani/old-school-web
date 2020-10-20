import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #TCP/IP socket
url=input("enter url:")
port=int(input("Port to forward request:"))
suburls=url.split('/')
sock.connect((suburls[0],port))  #server / port

cmd=f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)

while True:
	data=sock.recv(512) 
	if len(data)<1:
		break
	print(data.decode(),end='')