# Server Side Using UDP

import time
import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
time.sleep(5)

s.sendto(b"Hello Client ", (host, port))
msg = "How Are You"
s.sendto(msg.encode(), (host, port))
s.close()
