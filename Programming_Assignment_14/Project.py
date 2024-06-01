import smtplib
import requests
from bs4 import BeautifulSoup


def main():
    gmail_sender = 'vaishurao18@gmail.com'
    gmail_passwd = 'yjqwzjzjoaqaqbdh'
    server = smtplib.SMTP('stmp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    TO = 'nyano@nyano.dev'
    SUBJECT = "TEST"
    TEXT = 'HERE IS THE MESSAGE'
    BODY = f"To: {TO}\r\nFROM: {gmail_sender}\r\nSubject: {SUBJECT}\r\n{TEXT}"

    try:
        server.sendmail(gmail_sender, TO, BODY)
        print('email sent')
    except:
        print('error')

    server.quit()


def extract(e):
    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    url = f'https:https://in.indeed.com/jobsq=Python+Developer&l=Colorado&start={e}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def tranform(s):
    divs = s.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='salaryText').text.strip()
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }

        joblist = []
        H = extract(0)
        transform(H)
        print(joblist)


if __name__ = "__main__":
    main()
