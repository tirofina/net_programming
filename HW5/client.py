from socket import *
from tkinter.ttk import setup_master
import time

# 초기 연결 설정
s_device1 = socket(AF_INET, SOCK_STREAM)
s_device2 = socket(AF_INET, SOCK_STREAM)
s_device1.connect(('localhost', 2017))
s_device2.connect(('localhost', 1499))

# a 는 추가모드
f = open('./HW5_SEONGCHAN_LEE/data.txt', 'a')

while True:
    msg = input('Enter the device from which you want to get the data.\n')
    if msg == 'quit':
        s_device1.send('quit'.encode())
        s_device2.send('quit'.encode())
        break

    elif msg == '1':
        s_device1.send('Request'.encode())
        rsp = s_device1.recv(1024).decode()
        data = rsp.split(' ')
        temp = data[0]
        humid = data[1]
        illum = data[2]
        t = time.asctime()

        line = t + ':' + ' ' + 'Device_1:' + ' ' + 'Temp=' + temp + ', Humid=' + humid + ', Illum=' + illum + '\n'
        print(line)
        f.write(line)

    elif msg == '2':
        s_device2.send('Request'.encode())
        rsp  = s_device2.recv(1024).decode()
        data = rsp.split(' ')
        heartbeat = data[0] 
        steps = data[1]
        cal = data[2]
        t = time.asctime()

        line = t + ':' + ' ' + 'Device_2:' + ' ' + 'Heartbeat=' + heartbeat + ', Steps=' + steps + ', Cal=' + cal + '\n'
        print(line)
        f.write(line)

s_device1.close()
s_device2.close()

f.close()