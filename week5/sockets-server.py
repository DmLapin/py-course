# создание сокета, сервер
import socket


# https://docs.python.org/3/library/socket.html
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))   # max port 65535
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
conn.settimeout(5)  # timeout := None|0|gt 0

while True:
    try:
        data = conn.recv(1024)
    except socket.timeout:
        print("close connection by timeout")
        break

    if not data:
        break
    print(data.decode("utf8"))

conn.close()
sock.close()
