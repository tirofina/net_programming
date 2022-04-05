from socket import *
import random

# 초기 연결 설정
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1499))
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
            heartbeat = str(random.randrange(40, 141))
            steps = str(random.randrange(2000, 6001))
            cal = str(random.randrange(1000, 4001))

            total = heartbeat + ' ' + steps + ' ' + cal

            print(total)
            client.send(total.encode())
            
        # 사용자로부터 quit 메시지 수신 시 종료
        elif data == 'quit':
            break

    # 사용자로부터 quit 메시지 수신 시 종료
    if data == 'quit':
        break

    client.close()