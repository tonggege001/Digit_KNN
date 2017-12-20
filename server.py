
import socket
import threading
import time
from pkg4.DigitRec import*

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('10.135.1.70', 2017))

s.listen(10)
# print ('Waiting for connection...')

def tcplink(sock, addr):
#    print ('Accept new connection from %s:%s...' % addr)
#    sock.send('Welcome!')
    data = sock.recv(1024)
    time.sleep(1)
    vec = txt2vector(data)
    num = handWritingClassification(vec)
    sock.send(str(num))
#    if data == 'exit' or not data:
 #       break
#    sock.send('Hello, %s!' % data)
    sock.close()
#    print 'Connection from %s:%s closed.' % addr

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
