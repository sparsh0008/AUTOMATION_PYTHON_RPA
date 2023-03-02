# CLIENT SIDE FILE CLIENT
import socket
import string

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fileNAme = input("Enter the File Name : ")
s.sendto(fileNAme.encode(), (host, port))
print("File name send to server")

content = s.recv(1024)
content_str = str(content.decode())
split = content_str.split("\n")
print(split)

s.close()
