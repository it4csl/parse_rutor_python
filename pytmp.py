#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import render_template
from multiprocessing import Pool
import multiprocessing.dummy as multiprocessing

URL_TOP = "http://the-rutor.org/top"
all_link_and_name_and_size = []

def get_data(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    all_tr = soup.find("div", id="index").find_all("tr", {"class": "yhh"})

    for i in range(1, len(all_tr)):
        if (len(all_tr[i].contents[1]) < 4): continue
        url = "http://the-rutor.org" + all_tr[i].contents[1].contents[3].attrs["href"]
        text = all_tr[i].contents[1].contents[3].text

        size = ""
        if (len(all_tr[i].contents) == 7): size = all_tr[i].contents[5].text
        if (len(all_tr[i].contents) == 5): size = all_tr[i].contents[3].text
        #print(len(all_tr[i].contents[1]))
        all_link_and_name_and_size.append({"link": url, "name": text, "size": size})

    #     pattern = ["Лицензия", "iTunes", "Пифагор", "Scarabey", "Leonardo"]
    #     if any(key in link_and_name[0][2].text for key in pattern):

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route("/top", methods=["GET"])
    def top():
        all_link_and_name_and_size.clear()
        get_data(URL_TOP)
        #sort_list_dict("name")
        print("parse top")
        return render_template("index.html", content=all_link_and_name_and_size)

    app.run(debug = True, host = "localhost")