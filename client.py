from socket import *
import psutil
import json
from time import sleep

class Client:
    def __init__(self,ip,port):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((ip,port))

    def connect(self):
        try:
            msg = self.client.recv(1024).decode('utf-8')
        except Exception as e:
            print(f'error:{str(e)}')
            exit()
        if msg == 'connected!':
            print(msg)
            self.listen()
        else:
            exit()
    def sender(self,text):
        self.client.send(text.encode('utf-8'))
        while self.client.recv(1024).decode('utf-8')!='getted':
            self.client.send(text.encode('utf-8'))

    def listen(self):
        is_work = True
        while is_work:
            cpu = psutil.cpu_percent(interval=2)
            cpu = json.dumps(
               {'CPU':cpu}
           )
            print(cpu)
            self.sender(cpu)
            sleep(2)

Client(input('type server ip: '), 6543).connect()