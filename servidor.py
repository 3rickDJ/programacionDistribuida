import socket
port=60005
s=socket.socket()
host=socket.gethostname()
print(host)
host="172.31.1.196"
s.bind((host,port))
s.listen(15)
print('Server listening...')
while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data.decode()))
    filename='mytext.txt'
    f=open(filename, 'rb')
    l = f.read(1024)
    while True:
        conn.send(l)
        print('Sent', repr(l.decode()))
        l = f.read(1024)
        f.close()
        print('Done sending')
        conn.send('-> Thank you for connecting'.encode())
        conn.close()



