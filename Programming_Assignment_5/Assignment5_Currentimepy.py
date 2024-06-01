#This script fetches the current time executed for every 30 seconds

import datetime
import time

def get_current_time():
    return datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S %p")

def main():
    while True:
        current_time = get_current_time()
        print(f"The current time in Boulder is: {current_time}")
        time.sleep(30)

if __name__ == "__main__":
    main()






