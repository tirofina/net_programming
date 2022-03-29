from socket import *
s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    client, addr = s.accept()
    data = client.recv(1024)  # 수신
    msg = data.decode()  # 수신값decode
    req = msg.split('\r\n')

# 웹 서버 코드 작성
    req_m = req[0].split()[1].strip('/')

    print(req_m)

    if req_m == "index.html":  # filename
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: text/html \r\n\r\n')
        f = open("index.html", 'r', encoding='utf-8')
        data = f.read()
        client.send(data.encode('euc-kr'))

    elif req_m == "iot.png":
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: image/png\r\n\r\n')
        f = open('iot.png', 'rb')
        data = f.read()
        client.send(data)

    elif req_m == "favicon.ico":
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: image/x-icon\r\n\r\n')
        f = open('favicon.ico', 'rb')
        data = f.read()
        client.send(data)

    else:
        client.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        client.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        client.send(b'<BODY>Not Found</BODY></HTML>')


# 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close()
    client.close()
