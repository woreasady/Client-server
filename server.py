from socket import *
import json

class Server:
    def __init__(self,ip,port):
        print(f'server ip:{ip}\n server port:{port}\n')
        self.server = socket(AF_INET,SOCK_STREAM)
        self.server.bind((ip,port))
        self.server.listen(1)


    def sender(self, user, text):
        user.send(text.encode('utf-8'))

    def start(self):
        while True:
            global user,addr
            user, addr = self.server.accept()
            print(f'Client:\n\tIP: {addr[0]}\n\tport:{addr[1]}')
            self.listen(user)

    def listen(self,user):
        self.sender(user,'connected!')
        is_work = True

        while is_work:
            try:
                data = user.recv(1024)
                self.sender(user,'getted')
            except Exception as e:
                data = ''
                is_work = False

            if len(data)>0:
                message = data.decode('utf-8')
                if message == 'disconnect':
                    self.sender(user, 'You are disconnected')
                    user.close()
                    print('Client disconnected')
                    is_work == False
                else:
                    message = json.loads(message)
                    print(f'{addr[0]} Загрузка ЦП: {message}')
            else:
                print('Client disconnected')
                is_work = False

Server('127.0.0.2',6543).start()