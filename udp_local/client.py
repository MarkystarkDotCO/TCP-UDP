import socket
host ="127.0.0.1"
port=10002
databind=("127.0.0.1", port)
server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host,port))
data=input("Input Message :")
while data!='q':
    server.sendto(data.encode('utf-8'), databind)
    data, addr=server.recvfrom(1024)
    data=data.decode('utf-8')
    print("Message From Server: "+data)
    data=input("INput Message :")