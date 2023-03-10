import socket

host = "127.0.0.1"
port = 9000

s = socket.socket()
s.bind((host, port))
s.listen(1)
print("Server is Listening")

c, addr = s.accept()
print("Client Connected")

print("\n\nWelcome to the chat Bot")
# server will run Continuously
while True:
    data = c.recv(1024)

    if not data:
        break
    print("From Client : " + str(data.decode()))
    response = input("From Server : ")
    c.send(response.encode())
    print("\n")

print("Client Disconnected")
c.close()
