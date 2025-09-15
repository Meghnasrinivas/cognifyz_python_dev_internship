import requests
from bs4 import BeautifulSoup

def scrape_python_org():
    url = "https://www.python.org/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # More reliable: grab Upcoming Events
        events = soup.find("div", class_="medium-widget event-widget last").find_all("li")

        print("Upcoming Events on Python.org:")
        for e in events:
            time = e.find("time").text
            event_name = e.find("a").text
            print(f"{time} ➡ {event_name}")
    else:
        print("Failed to retrieve the page.")

scrape_python_org()
