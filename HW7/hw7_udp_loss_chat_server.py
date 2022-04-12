from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)

        # 고의로 50%의 데이터 손실을 만듦
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
        
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)

        # 소켓의 timeout 설정. 해당 timeout 내 메시지 수신을 못하면 timeout 예외 발생
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break