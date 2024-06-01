#!/usr/bin/env python3

import threading
import time
from loguru import logger

# Function 1: Print numbers from 1 to 5
def function1():
    for i in range(1, 6):
        logger.info("starting the thread")
        logger.info(f"Function 1: {i}")
        logger.info("Ending the thread")
        time.sleep(1)

# Function 2: Print letters from G to M
def function2():
    for letter in "GHIJKLM":
        logger.info("starting the thread")
        logger.info(f"Function 2: {letter}")
        time.sleep(1)

def main():
    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    print("Both functions have finished.")

if __name__ == "__main__":
    main()
