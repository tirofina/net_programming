from socket import *
import random

# 초기 연결 설정
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2017))
s.listen(5)
print('[waiting]...')

while True:
    client, addr = s.accept()
    print('[Connection from :', addr+"]")

    while True:
        data = client.recv(1024)
        if not data:
            break
        data = data.decode()
        print(data)

        if data == 'Request':
            temp = str(random.randrange(0, 41))
            humid = str(random.randrange(0, 101))
            illum = str(random.randrange(70, 151))
            total = temp + ' ' + humid + ' ' + illum
            print(total)
            client.send(total.encode())
 
        # 사용자로부터 quit 메시지 수신 시 종료
        elif data == 'quit':
            break

    # 사용자로부터 quit 메시지 수신 시 종료
    if data == 'quit':
        break

    client.close()