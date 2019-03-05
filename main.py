#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template

all_link_and_name_and_size = []

def get_html(url):
    req = requests.get(url)
    return req.text

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    all_tr = soup.find("div", id="index").find_all("table")

    all_a = []
    for i in all_tr[0]:
        all_a.append(i.find_all("td"))

    for j in range(1, len(all_a)):
        link_and_name = []

        link_and_name.append(all_a[j][1].find_all("a"))
        size = ""
        a_href = ""
        a_text = ""
        pattern = ["Лицензия", "iTunes", "Пифагор", "Scarabey", "Leonardo"]
        if any(key in link_and_name[0][2].text for key in pattern):
            if (len(all_a[j]) == 5): size = all_a[j][3].text
            if (len(all_a[j]) == 4): size = all_a[j][2].text

            a_href = "http://rutor.info" + (link_and_name[0][2].attrs["href"])
            a_text = link_and_name[0][2].text

            all_link_and_name_and_size.append({"link": a_href, "name": a_text, "size": size})

for i in range(0, 30):
    new_url = "http://rutor.info/browse/{}/1/0/2".format(i)
    get_data(get_html(new_url))
    print("parse ", i)

def sort_list_dict(how):
    all_link_and_name_and_size.sort(key=lambda d: d[how])

sort_list_dict("name")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", content=all_link_and_name_and_size)

app.run(debug = True)
