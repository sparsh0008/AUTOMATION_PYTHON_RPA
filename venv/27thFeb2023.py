# import urllib.parse
# url = "http://www.ab.com:88/engineering/computer-science.html"
# tpl = urllib.parse.urlparse(url)
# print(tpl)
# print("SCHEME - {0}".format(tpl.scheme))
# print("PATH - {0} ".format(tpl.path))
# print("NETLOC - {0} ".format(tpl.netloc))
# print("PORT - {0} ".format(tpl.port))
# print("PARAMS - {0} ".format(tpl.params))
# print("QUERY - {0} ".format(tpl.query))
# print("GET URL - {0} ".format(tpl.geturl()))

# SERVER SIDE
import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET , SOCK_STREAM - used for TCPIP
s.bind((host, port))
s.listen(1)
print("Server is Listening")

c, addr = s.accept()
print(str(addr))

c.send(b"Hello how are you")
msg = "I am Fine"
c.send(msg.encode())
c.close()
