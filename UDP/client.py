import socket
import time

# IP host ของ server
# Lv1 จะเป็น IP local
# Lv2 จะเป็น network IP
HOST = '27.145.208.78'
# เลข port ที่ server ปลายทางเปิดให้บริการอยู่
PORT = 5454

# AF_INET = IPv4 และ SOCK_DGRAM เป็นการรับส่งข้อมูลแบบ Datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# รับ input string จาก user
t1 = input('ENTER MESSAGE 1:\n')
t2 = input('ENTER MESSAGE 2:\n')
t3 = input('ENTER MESSAGE 3:\n')

#concat string
message = t1 + t2 + t3
#check sum จาก string ด้านบน
checksum = len(message)

# ส่ง message ไปยัง Server
sock.sendto(t1.encode(), (HOST, PORT))
sock.sendto(t2.encode(), (HOST, PORT))
sock.sendto(t3.encode(), (HOST, PORT))

# ตัวแปรสำหรับรับค่า message
recv_message = ''
# ตัวแปรสำหรับรับค่า checksum
recv_checksum = ''

# loop จนกว่าจะมี message และมี timeout = 50 วินาที
while len(recv_message) == 0 : recv_message = sock.recv(50).decode()
while len(recv_checksum) == 0 : recv_checksum = sock.recv(50).decode()

# ถ้า message ตอบกลับมา จะ print message 
if (recv_message.replace('#', '') == message): print('message is correct! sent:', message, ', received:', recv_message)
else: print('message is wrong', recv_message)

if (int(recv_checksum) == checksum): print('checksum is correct! sent:', checksum, ', received:', recv_checksum)
else: print('checksum is wrong', recv_checksum)
