import threading
import time
import sys
import argparse
from loguru import logger

def task1():
    for i in range(1, 6):
        logger.info(f"Task 1: {i}")
        time.sleep(1)
def task2():
    for letter in "ABCDE":
        logger.info(f"Task 2: {letter}")
        time.sleep(1)

def main(task_number):
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    logger.info("Both tasks have finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multithreading example with logging")
    parser.add_argument("task_number", type=int, choices=[1, 2], help="Task number to execute (1 or 2)")
    args = parser.parse_args()

    # Configure logger
    logger.add(sys.stdout, level="INFO")

    start_time = time.time()
    main(args.task_number)
    end_time = time.time()

    logger.info(f"Total execution time: {end_time - start_time:.2f} seconds")
