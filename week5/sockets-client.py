# создание сокета, клиент
import socket


# более короткая запись
sock = socket.create_connection(("127.0.0.1", 10001), 5)
# set socket read timeout
sock.settimeout(2)
try:
    sock.sendall("ping".encode("utf8"))
except socket.timeout:
    print("send data timeout")
except socket.error as ex:
    print("send data error:", ex)
sock.close()
