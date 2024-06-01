################SOCKET_SERVER##############

##__author__ = "Srivaishnavi"
## File Transfer in Socket Programming using Python
## Server_Program

import socket

IP = socket.gethostbyname(socket.gethostname())
Port = 4444
ADDR = (IP, Port)
FORMAT = "utf-8"
SIZE = 1024


def main():
    print("[Starting] Server is starting.....")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[Listening] Server is Listening....")

while True:
    # Establishing connection between client and server
    connection, addr = server.accept()
    print(f"[New Connection] {addr} is connected..")

    # File Reception from Client
    filename = connection.recv(SIZE).decode(FORMAT)
    print("[Recv] filename Received.")
    file = open(filename, "w")
    connection.send("Filename recieved.".encode(FORMAT))

    # Returning the file reception acknowledgment to client
    data_1 = connection.recv(SIZE).decode(FORMAT)
    print(f"[RECV] File data recieved")
    file.write(data_1)
    connection.send("File data recieved.".encode(FORMAT))

    # Connection closure
    file.close()
    connection.close()
    print(f"[Disconnected] {ADDR} disconnected.")

if __name__ == "__main__":
    main()


