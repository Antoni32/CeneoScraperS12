import requests
from bs4 import BeautifulSoup

respons = requests.get("https://www.ceneo.pl/55433796#tab=reviews")

page_dom = BeautifulSoup(respons.text, "html.parser")

opinion = page_dom.select("div.js_product-review").pop(0)

opinion_id = opinion["data-entry-id"]

author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
try:
    recommendation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
except IndexError:
    recommendation = None
stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
stars = float(stars.split("/")[0].replace(",","."))
content = opinion.select("div.user-post__text").pop(0).get_text().strip()
try:
    pros = opinion.select("")
    pros =[x.get_text().strip() for x in pros]
except IndexError:
    pros = None
try:
    cons = opinion.select("").pop(0).get_text().strip().pop(0).get_text().strip()
except IndexError:
    cons = None
try:
    purchased = bool(opinion.select("div.review-pz").pop(0).get_text().strip())
    
submit_date = opinion.select("").pop(0).get_text().strip()
purchase_date = opinion.select("").pop(0).get_text().strip()
usefull = int(opinion.select("").pop(0).get_text().strip())
useless = int(opinion.select("").pop(0).get_text().strip())

print(author,recommendation,stars,content, sep="\n")


