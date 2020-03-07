from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

MSW = "https://magicseaweed.com/Lahinch-Beach-Surf-Report/52/"

# open connection, grab page
uClient = uReq(MSW)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs table
# working containers = page_soup.findAll("table", {"class": "table table-sm table-striped table-inverse table-tide"})

containers = page_soup.findAll("table", {"class": "table table-sm table-striped table-inverse table-tide"})

container_sunTimes = containers[15]


