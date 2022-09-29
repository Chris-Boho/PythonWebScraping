import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.pcgamer.com/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text)
article_names = soup.findAll("h3", class_="article-name")

for articles in article_names:
    articles = re.sub("<.*?>", "", str(articles))
    print(articles)