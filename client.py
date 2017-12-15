import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('111.230.238.239', 2017))

#print(s.recv(1024).decode('utf-8'))
#for data in [b'Michael', b'Tracy', b'Sarah']:

fr = open('2_30.txt')
s.send(fr.read())
print(s.recv(1024).decode('utf-8'))
#s.send(b'exit')
s.close()
