from socket import *
import psutil
import json
import threading

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
            self.start()
        else:
            exit()
    def sender(self,text):
        self.client.send(text.encode('utf-8'))
        while self.client.recv(1024).decode('utf-8')!='getted':
            self.client.send(text.encode('utf-8'))

    def PCdata(self):
        while True:
            cpu = int(psutil.cpu_percent(interval=2))
            username = psutil.users()
            memory = psutil.virtual_memory()
            indicators = json.dumps(
                {
                    'CPU': cpu,
                    'Memory': memory[2],
                    'User': username[0][0]
                }
            )
            self.sender(indicators)


    def listen(self):
        while True:
            message = input(':')
            self.sender(message)

    def start(self):
        thr1 = threading.Thread(target=Client.PCdata(self), daemon=True, name='PCData')
        thr2 = threading.Thread(target=Client.listen(self), daemon=True, name='Listen')
        thr1.start()
        thr2.start()


Client(input('type server ip: '), 6543).connect()