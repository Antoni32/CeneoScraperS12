import requests

respons = requests.get("https://www.ceneo.pl/55433796#tab=reviews")

print(respons.text)


