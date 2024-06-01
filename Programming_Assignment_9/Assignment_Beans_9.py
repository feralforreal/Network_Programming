import requests
import re
import time
from time import strftime
import csv
from loguru import logger

logger.add("Beans_Lab_9_Logfile.log")

def price_check(url):
            r=requests.get(url)
            price = re.search('\$\d+.\d+', r.text)
            if price:
                    return (price[0])
                    logger.info(f"Price check is made {price}")
            else:
                    return("Error, Price not found")
@logger.catch
def main():
    while True:
                 price=price_check("http://beans.itcarlow.ie/prices.html")
                 logger.info(f"Price check is made {price}")
                 date = strftime("%m/%d/%y")
                 clocktime = strftime("%I:%M%p")
                 header = "Price, Day, Time"
                 with open("Beans_Lab9_Assignment_9.csv", 'a', newline='') as file:
                         x = csv.writer(file)
                         for i in price:
                             x.writerow([price, date, clocktime])
                         logger.success(f"Price is written to Beans_Lab9_Assignment_9: {x}")

    time.sleep(300)

if __name__ == "__main__":
    main()



'''logger.add("Beans_lab_9_logfile.log")

@logger.catch
def main():
    while True:
        p = requests.get("http://beans.itcarlow.ie/prices.html")
        price = re.search('\$\d+.\d+', p.text)
        price_1 = price.group(0)
        date = strftime("%m/%d/%y")
        clocktime = strftime("%I:%M%p")
        if price:
                with open("Beans_Ladpkwpl.csv", 'a', newline= '') as file:
                    x = csv.writer(file)
                    logger.info(f"Price check {x}")
                    for i in price_1:
                        x.writerow([price_1, date, clocktime])
                    logger.success(f"foo  is success {x}")
                time.sleep(3)
        else:
            print("Error")


if __name__ == "__main__":
    main()'''
