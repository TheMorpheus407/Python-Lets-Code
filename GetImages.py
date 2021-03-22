from bs4 import BeautifulSoup as bs
import requests
import os

URL = "https://the-morpheus.de/"

soup = bs(requests.get(URL).content, "html.parser")
img_urls = []
for img in soup.find_all("img"):
    img_url = URL + img.attrs.get("src")
    img_urls.append(img_url)

for url in img_urls:
    response = requests.get(url)
    size = int(response.headers.get("Content-Length", 0))
    name = os.path.join("imgs", url.split("/")[-1])
    with open(name, "wb") as f_out:
        f_out.write(response.content)