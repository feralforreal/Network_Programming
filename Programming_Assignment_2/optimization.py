import threading
import requests
import time

def get_status_code(url):
    try:
        response = requests.get(url.strip())
        return response.status_code
    except Exception as e:
        print(f"Error occurred while accessing {url}: {e}")
        return None

def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    try:
        while True:
            if not urls:
                print("Quitting. All URLs checked.")
                break
            # Pop a URL out of the list and remove its new line
            url = urls.pop(0).strip()

            # Kick off a thread to get the status code
            thread = threading.Thread(target=get_status_code, args=(url,))
            thread.start()
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Quitting due to keyboard interrupt.")
        for t in threading.enumerate():
            if t != threading.main_thread():
                t.join()

if __name__ == "__main__":
    main()
