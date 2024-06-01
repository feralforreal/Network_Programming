import argparse
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def write_key_to_file(key, key_file):
    with open(key_file, "wb") as f:
        f.write(key)

def read_key_from_file(key_file):
    with open(key_file, "rb") as f:
        return f.read()

def encrypt_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

def encrypt_file(input_file, output_file):
    try:
        key = generate_key()
        write_key_to_file(key, output_file + ".key")
        with open(input_file, "r") as f:
            text = f.read()
        encrypted_text = encrypt_text(text, key)
        with open(output_file, "wb") as f:
            f.write(encrypted_text)
        print(f"Encrypted file '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"Error occurred during encryption: {e}")

def decrypt_file(input_file, output_file, key_file):
    try:
        key = read_key_from_file(key_file)
        with open(input_file, "rb") as f:
            encrypted_text = f.read()
        decrypted_text = decrypt_text(encrypted_text, key)
        with open(output_file, "w") as f:
            f.write(decrypted_text)
        print(f"Decrypted file '{input_file}' to '{output_file}' using key from '{key_file}'")
    except Exception as e:
        print(f"Error occurred during decryption: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt text files")
    parser.add_argument("input_file", type=str, help="Input file name")
    parser.add_argument("output_file", type=str, help="Output file name")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the file")
    parser.add_argument("--key_file", type=str, help="Key file for decryption")
    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.input_file, args.output_file)
    elif args.decrypt:
        if not args.key_file:
            print("Error: Key file is required for decryption")
            exit()
        decrypt_file(args.input_file, args.output_file, args.key_file)
