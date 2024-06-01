import socket
import hashlib

def send_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 64523)  
    try:
        client_socket.connect(server_address)

        # Read the file and compute its MD5 hash
        with open(file_name, 'rb') as file:
            file_data = file.read()
            md5_hash = hashlib.md5(file_data).hexdigest()

        client_socket.sendall(file_data)

        # Receive the MD5 hash from the server
        received_md5_hash = client_socket.recv(1024).decode()

        # Compare MD5 hashes
        if md5_hash == received_md5_hash:
            print("File uploaded successfully.")
        else:
            print("File upload failed. MD5 hash does not match.")

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    file_name = "testing.txt"
    send_file(file_name)
