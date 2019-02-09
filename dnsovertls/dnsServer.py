import socket,ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain("server.crt","server.key")

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dnsSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dnsSock.bind((socket.gethostname(),1000))
dnsSock.listen(1)
conn, addr = dnsSock.accept()
secure_socket = context.wrap_socket(conn,server_side=True)
while 1:
    data = secure_socket.recv(1024).decode("hex")
    print 'data is recieved'
    clientSock.sendto(data, ('127.0.0.1', 53))
    datadns=clientSock.recvfrom(4096)
    secure_socket.sendall(datadns[0])
