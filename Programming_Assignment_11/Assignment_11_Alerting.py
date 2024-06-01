#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loguru import logger
import time

# Function to scrape the website and extract relevant information
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Extracting the product availability
            availability = soup.find("div", class_="availability").get_text().strip()
            return availability
        else:
            logger.error("Failed to access website")
            return None
    except Exception as e:
        logger.error(f"Error occurred during scraping: {e}")
        return None

# Function to send alert message
def send_alert(message):
    try:
        # Email configuration
        sender_email = "your_email@gmail.com"
        receiver_email = "recipient_email@gmail.com"
        password = "your_password"

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Alert: Product Available"

        # Email content
        body = f"Product is now available!\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # SMTP server setup (Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        logger.info("Alert email sent successfully")
        server.quit()
    except Exception as e:
        logger.error(f"Error occurred while sending alert email: {e}")

# Function to monitor the website for changes and send alert
def monitor_website(url, desired_state):
    while True:
        data = scrape_website(url)
        if data == desired_state:
            send_alert("The product is now available!")
            logger.info("Desirable state reached! Alert sent.")
            break
        else:
            logger.info("Desirable state not reached. Waiting for next check.")
            time.sleep(60)  # Check website every 60 seconds

# Main function
def main():
    url = "https://example.com/product"
    desired_state = "In Stock"
    monitor_website(url, desired_state)

if __name__ == "__main__":
    # Loguru configuration
    logger.add("scraper.log", rotation="500 MB", level="INFO")
    main()
