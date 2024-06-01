##################################SOCKET_CLIENT##############

##__author__ = "Srivaishnavi"
## File Transfer in Socket Programming using Python
## Client_Program

import socket

IP = socket.gethostbyname(socket.gethostname())
Port = 4444
ADDR = (IP, Port)
FORMAT = "utf-8"
SIZE = 1024

def main():
   print("[Client] client starting.....")
   Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   Client.connect(ADDR)

   #Reading the file from local machine
   file = open("C:/Users/Srivaishnavi/Documents/Unmask.txt", "r")
   data_1 = file.read()

   #Sending the File to server ad printing the server acknowledgment
   Client.send("Unmask.txt".encode(FORMAT))
   msg = Client.recv(SIZE).decode(FORMAT)
   print(f"[Server]: {msg}")

   Client.send(data_1.encode(FORMAT))
   msg = Client.recv(SIZE).decode(FORMAT)
   print(f"[Server]: {msg}")

   #Connection Closure
   file.close()
   Client.close()

if __name__ == "__main__":
   main()

