import socket
import threading

nickname = input("Enter a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 44444))

TEXT_RED = '\033[31m'
TEXT_GREEN = '\033[32m'
TEXT_RESET = '\033[0m'


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print('An error occurred.')
            client.close()
            break


def write():
    client.send(nickname.encode('ascii'))
    while True:
        message = TEXT_RED + nickname + ':' + TEXT_RESET + f' {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()