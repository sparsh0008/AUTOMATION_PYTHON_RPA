import socket

host = "127.0.0.1"
port = 9000

s = socket.socket()
s.connect((host, port))

chat = input("You : ")
while chat != "exit" and chat != "EXIT" and chat != "Exit":

    s.send(chat.encode())

    res = s.recv(1024)
    print("Server : " + res.decode() + "\n")
    chat = input("You : ")

s.close()
