#!/usr/bin/env python 

import multiprocessing
import time

def jobs(q):
    print(q.get())
    time.sleep(5)
    
    
def main():
    #building queue
    
    q = multiprocessing.Queue()
    #filling queues with tasks
    for job in range(10):
        q.put(job)
    #making 10 processes
    for x in range(10):
        multiprocessing.Process(target=jobs, args=(q, )).start()
        
    if __name__ == "__main__":
        main()