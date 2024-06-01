
import socket
import hashlib

def receive_file(file_name):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 64523))  # Bind the socket to the address and port
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print("Waiting for connection...")
        connection, client_address = server_socket.accept()

        try:
            print("Connection established with:", client_address)

            file_data = b''
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file_data += data

            md5_hash = hashlib.md5(file_data).hexdigest()
            with open(file_name, 'wb') as file:
                file.write(file_data)

            print("File received and saved successfully.")

            # Send the MD5 hash back to the client
            connection.sendall(md5_hash.encode())

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    file_name = "recieved.txt"
    receive_file(file_name)
