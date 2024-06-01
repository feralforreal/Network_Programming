#!/usr/bin/env python3
import argparse,sys
from loguru import logger

logger.add("logfile.log")

def Argparse_Helper():
    parser = argparse.ArgumentParser(description="Random app that reads strings off the file.")
    parser.add_argument("--silence", action = "store_true", help="disable logging")
    args=parser.parse_args()
    return args()

def main():
    args = Argparse_Helper()
    if args.silence:
        logger.remove()
        logger.add("loggerfile.log", level="success")
        logger.add(sys.stdout, level="Critical")
        logger.add(sys.stdout, level="Warning")
        
    logger.info(f"name is {args.name}")
    print(f"hello{args.namee}")
    logger.critical("test message")
    
if __name__ == "__main__":
    main()