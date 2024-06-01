#!/usr/bin/env python 
from cryptography.fernet import Fernet

def write_and_get_key():
    #generating the key
    key = Fernet.generate_key()
    #writing it to a file (for backup)
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    #key needs to be a fernet type to work in this case
    return Fernet(key)
def main():
    key = write_and_get_key()
    #reading the plain file data
    with open("example.txt", "rb") as file:
        file_data = file.read()
    
    #encrypting the data
    encrypted_data = key.encrypt(file_data)
    
    #writing the encrypted file
    with open("example-encrypted.xtx", "wb") as file:
        file.write(encrypted_data)
    
    if __name__ == "__main__":
        main()