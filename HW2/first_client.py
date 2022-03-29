from http import client
import socket
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)  # 접속
msg = sock.recv(1024)  # 서버값받아오기
print(msg.decode())  # helloip주소출력

# 학생이름전송
name = 'Seongchan Lee'
sock.send(name.encode())

# 본인학번수신후출력
msg = sock.recv(1024)
print(int.from_bytes(msg, 'big'))
sock.close()
