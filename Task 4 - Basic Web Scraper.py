import requests
from bs4 import BeautifulSoup

# Requesting the website
URL = "https://www.bbc.com/news"
response = requests.get(URL)
print("The response code is:", response.status_code, "\n")

# Parse the HTML Document
soup = BeautifulSoup(response.content, "html.parser")

# Extract the news headlines from HTML
headlines = soup.find_all("h2")

# Display the headlines
for h in headlines:
    print(h.text)
