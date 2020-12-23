#import socket module

from socket import *
import os
import threading
import time 
import sys

SERVER_PORT = 1500

serverSocket = socket(AF_INET, SOCK_STREAM)



def run_client(connectionSocket,address):
	#Establish the connection
	# connectionSocket, address = serverSocket.accept()#Fill in start #Fill in end
	try:
		message = connectionSocket.recv(1024) #Fill in start #Fill in end
		filename = message.split()[1]
		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
		my_file = os.path.join(THIS_FOLDER, filename.decode()[1:])
		f = open(my_file)
		outputdata = f.read() 
		connectionSocket.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())

		connectionSocket.close()
		print("HTTP/1.1 200 OK Response has been Sent")
	except IOError:
		print("HTTP/1.1 404 Not Found Response has been Sent")
		connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
		connectionSocket.close()

def run_server(sp):
	print("Server has been started")
	serverSocket.bind(("",sp))
	serverSocket.listen(5)
	threads=[]
	keep_going = True
	while keep_going:
		try:
			connectionSocket, addr = serverSocket.accept()
			t = threading.Thread(target = run_client, 
                                 args = (connectionSocket, addr))
			threads.append(t)
			t.start()
			print(threads)
		except KeyboardInterrupt:
			keep_going = False
			serverSocket.close()
			sys.exit()

if __name__ == '__main__':
	sp = int(sys.argv[1]) if len(sys.argv) > 1 else SERVER_PORT
	run_server(sp)