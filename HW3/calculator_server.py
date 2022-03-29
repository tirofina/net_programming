import socket
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(5)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)  # 연결확인
    client.send(b'Hello ' + addr[0].encode())

    # 학생의 이름을 수신한 후 출력
    msg = client.recv(1024)

    msg = msg.decode()  # msg를 복호화하여 저장 (str로 변환됨)
    num1, op, num2 = msg.split()
    num1, num2 = int(num1), int(num2)  # num1이랑 num2는 int형

    if(op == '+'):  # 문자열 비교연산자
        print(num1 + num2)
    elif op == '-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)
    else:
        print('다시입력')

    msg = client.recv(1024)
    msg = msg.decode()
    client.close()
