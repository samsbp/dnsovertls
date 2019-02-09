import socket
import sys
import ssl

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostname(), 53)
print  'starting up on %s port %s' % server_address
sock.bind(server_address)

CA_DATA=open('certificate.pem','r').read()

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain("client.crt","client.key")


clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dnsSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(dnsSock)

secure_socket.connect(('172.17.0.3',1000))
while True:
    data, addr = sock.recvfrom(4096)
    print 'data is recieved from '+ data
    secure_socket.sendall(data.encode('hex'))
    datadns=secure_socket.recv(4096)
    sock.sendto(datadns,addr)
