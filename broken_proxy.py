import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#AF_INET indicates ipv4 socket

#-----
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#---

serverSocket.bind(("0.0.0.0", 8000))
serverSocket.listen(5)

clientSocket.connect(("www.google.com",80))


clientSocket.setblocking(0)


while True:
	request = bytearray()
	while True:
		incomingSocket.setblocking(0)
		(incomingSocket, address) = serverSocket.accept()
		
		#print "we got a connection from %s" % (str(address))
		try:	
			part = incomingSocket.recv(1024)
		except IOError, e:
			if e.errno ==11:
				part = None
			else:
				raise
		if (part):
			clientSocket.sendall(part)
			request.extend(part)
		else:
			break
		print request
	
	response = bytearray()
	while True:
		try:
			part = clientSocket.recv(1024)
		except IOError, e:
			if e.errno ==11:
				part = None
			else:
				raise
		if (part):
			incomingSocket.sendall(part)
			response.extend(part)
		else:
			break
		print response
	
