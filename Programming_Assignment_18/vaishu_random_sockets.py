#!/usr/bin/env python 

import socket

def main():
    target_host = "127.0.0.1"
    target_port = 9997
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client.sendto(b"ZZZHHHHCCCC", (target_host, target_port))
    client.close()
    
if __name__ == "__main__":
    main()