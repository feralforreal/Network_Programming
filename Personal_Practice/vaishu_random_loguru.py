#!/usr/bin/env python3

import sys
from loguru import logger
logger.add("logfile.log")

def main():
    try:
        #taking a user arg
        foo = sys.argv[1]
        #fetching different logs info, success, warning, error and others
        logger.info(f"foo is {foo}")
    except:
        foo = "default"
        logger.error(f"foo is {foo}")
        
    print(foo)
    
if __name__ == "__main__":
    main()