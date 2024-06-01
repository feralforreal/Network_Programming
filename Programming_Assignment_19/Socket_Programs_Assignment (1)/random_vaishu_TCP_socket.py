#!/usr/bin/env python
import socket

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 20
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.binf((TCP_IP, TCP_PORT)) #binidng to the TCP port
    s.listen(1) #required for backlogged queue / connections
    
    conn, addr = s.accept()
    print(f"Connection from IP :{addr}")
    
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print(f"Recieved Message : {data}")
        returnmsg = b"msg recieved"
        conn.send(returnmsg)
    conn.close()
    
if __name__ == '__main__':
    main()