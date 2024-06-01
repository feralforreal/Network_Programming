from cryptography.fernet import Fernet
import argparse
import hashlib

def Argparse_Helper():
    parser = argparse.ArgumentParser(description='This inputs the files to hash with MD5')
    parser.add_argument('First_File', required = True, action='store_true', help='First file to hash')
    parser.add_argument('Second_File', required = True, action='store_true', help='Second file to hash')
    parser.add_argument('--version', action='version',version='%(prog)s 1.0')
    args=parser.parse_args()
    return(args)
def main():
    args=Argparse_Helper()
    hash1=hashlib.md5()
    hash2=hashlib.md5()
    try:
        with open(args.First_File,'rb') as F1:
            buffer=F1.read()
            hash1.update(buffer)
    except:
        print("Error opening first file!")
        
    try:
        with open(args.Second_File,'rb') as F2:
            buffer=F2.read()
            hash2.update(buffer)
    except:
        print("Error opening second file")
        
    if hash1.hexdigest() == hash2.hexdigest():
        print("Files Match")
    else:
        print("Files do not Match")

if __name__ == "__main__":
    main()
    
