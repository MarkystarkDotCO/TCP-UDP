import socketserver
# Lv2 host IP เป็น network IP ของเครือข่ายนั้นๆ
# Lv1 host IP เป็น local host (127.0.0.1)

HOST = '192.168.1.1' 
PORT = 5454 # port ที่ไม่ได้ใช้งาน
messages = [] # Array สำหรับ เก็บ messages



# class สำหรับสร้าง messages
class Message():
    
    # มี attributes 3 ตัว มีค่าเป็น None
    msg1 = None
    msg2 = None
    msg3 = None
   
# เชื่อม message ทั้ง 3 ตัว
    def encoded(self):
        return self.msg1 + '#' + self.msg2 + '#' + self.msg3
# หาความยาว message
    def checksum(self):
        return len(self.msg1 + self.msg2 + self.msg3)




                       # รับส่งข้อมูลแบบ Datagram  (ของ TCP จะเป็นแบบ สตรีม)
class MyUDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        print('listening...')

        # ถ้า message ใด เป็น None
        if self.server.data.msg1 is None:
            print('received 1')
            self.server.data.msg1 = self.request[0].decode()
        elif self.server.data.msg2 is None:
            print('received 2')
            self.server.data.msg2 = self.request[0].decode()
        elif self.server.data.msg3 is None:
            print('received 3')
            self.server.data.msg3 = self.request[0].decode()

            # encode message เพื่อตอบ client
            reply = self.server.data.encoded()
            # check sum เพื่อนับความยาวอักขระ
            checksum = str(self.server.data.checksum())

            print('sending reply:', reply)
            print('sending checksum:', checksum)

            # request ข้อมูลด้านบนทั้งหมดที่จัดเตรียมไว้ กลับไป client
            self.request[1].sendto(reply.encode(), self.client_address)
            self.request[1].sendto(checksum.encode(), self.client_address)

            # สร้าง object Message() เพื่อเก็บ attributes ทั้งหมดที่ set ไว้ (พวก msg1 2 3 ที่ set ในนี้ เป็น attribute ของ Message()  )
            self.server.data = Message()



            # สร้าง server UDP จาก HOST PORT MyUDPHandler ที่ได้ set up ไว้ตอนต้น
server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
# กำหนด object Message เพื่อเป็น data ที่จะรับส่ง
server.data = Message()
# วนลูปสำหรับการ รอรับส่งข้อมูล
server.serve_forever()
