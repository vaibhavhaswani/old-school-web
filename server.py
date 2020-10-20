from socket import *

def createServer():
	servsock=socket(AF_INET,SOCK_STREAM)
	try:
		servsock.bind(('localhost',9000))
		servsock.listen(5)
		while(1):
			(clisock,addrs)=servsock.accept()

			rd=clisock.recv(5000).decode()
			chunks=rd.split('\n')
			if len(chunks)>0:
				print(chunks[0])
			data='HTTP/1.1 200 OK\r\n'
			data+='ContentType:HTML/TEXT; '
			data+='Charset:utf-8\r\n\r\n'
			data+='<html><body><center><h1>HELLO WORLD</h1></center></body></html>\r\n\r\n'

			clisock.sendall(data.encode())
			clisock.shutdown(SHUT_WR)

	except KeyboardInterrupt:
		print('KeyboardInterrupt: shutting server down...')
	except Exception as e:
		print('Error')
		print(e)

	servsock.close()


if __name__=='__main__':
	print('Server started Access to https://localhost:9000')
	createServer()

