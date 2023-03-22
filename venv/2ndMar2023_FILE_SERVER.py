# SERVER SIDE FILE CLIENT
import socket

host="localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Server is Listening")
c, addr = s.accept()
print("Connection is Established")
f_name = c.recv(1024)
fn = f_name.decode()
print("File NAme Received - " + fn)
try:
    print("Address - " + str(addr))
    f = open(fn, "r")
    print("file Opened")
    content = f.read()
    c.send(content.encode())
    print("File Data Send To the Client")
    f.close()

except FileNotFoundError:
    c.sendto("File Not Found", (host, port))

c.close()
dd