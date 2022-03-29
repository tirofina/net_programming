from http import client
import socket
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)  # 접속
msg = sock.recv(1024)  # 서버값받아오기
print(msg.decode())  # helloip주소출력

while True:
    msg = input()
    if msg == 'q':
        break
    sock.send(msg.encode())

sock.close()
