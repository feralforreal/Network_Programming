#!/usr/bin/env python 
from cryptography.fernet import Fernet

def main():
    #getting the key
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        
    #Turn the key into a fernet object for decrypting 
    
    key = Fernet(key)
    with open("example-encrypted.txt", "rb") as file:
        #reading the encrypted data
        encrypted_data = file.read()
    #decrypt data
    decrypted_data = key.decrypt(encrypted_data)
    print(decrypted_data)
    
if __name__ == "__main__":
    main()
    