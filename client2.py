import socket
s = socket.socket()
host="172.31.2.226"
port=60005
s.connect((host,port))
s.send('HelloServer!'.encode())
with open('received.txt','wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        if not data:
            break
        print('Data=>', data.decode())
        f.write(data)
    f.close()
    print('successfully get the file')
    s.close()
    print('connnection close')
