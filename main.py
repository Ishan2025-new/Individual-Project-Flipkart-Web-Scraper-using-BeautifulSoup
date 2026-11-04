import pandas as pd
import requests as re
from bs4 import BeautifulSoup

product_name = []
price = []
description = []
review = []

for i in range(2, 5):
    url = "https://www.flipkart.com/search?q=samsung+5g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore" \
    "OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&" \
    "suggestionId=samsung+5g+mobile%7CMobiles&requestId=85cfacf8-0ef0-42e0-8bac-872409433f26&as-backfill" \
    "=on&page="+str(i)

    r = re.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="QSCKDh dLgFEE")

    names = box.find_all("div", class_="RG5Slk")

    for i in names:
        name = i.text
        product_name.append(name)

    prices = box.find_all("div", class_="hZ3P6w DeU9vF")

    for i in prices:
        name = i.text
        price.append(name)

    desc = box.find_all("ul", class_="HwRTzP")

    for i in desc:
        name = i.text
        description.append(name)

    reviews = box.find_all("div", class_="MKiFS6")

    for i in reviews:
        name = i.text
        review.append(name)

df = pd.DataFrame({"Product Name": product_name, "Price": price, "Description": description, "Review": review})
df.to_csv("C:/Excel/CSV/New 2026/flipkart_samsung_5g_mobiles.csv")