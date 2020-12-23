from socket import *
import sys

SERVER_NAME = ''
SERVER_PORT = 1500

def run_client(server_name, server_port, file_name):
    print("run_client is called")
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    host = server_name+":"+str(server_port)
    msg = "GET /"+file_name+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nDNT: 1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n"
    print(msg)
    client_socket.send(msg.encode())
    response = client_socket.recv(1024)
    print(response.decode())
    response = client_socket.recv(1024)
    print(response.decode())
    client_socket.close()

if __name__ == "__main__":
    sn = sys.argv[1] if len(sys.argv) > 1 else SERVER_NAME
    sp = int(sys.argv[2]) if len(sys.argv) > 2 else SERVER_PORT
    fn = sys.argv[3]
    run_client(sn, sp, fn)