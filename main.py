#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import render_template
from multiprocessing import Pool

all_link_name_size = []
BASE_URL_TOP = "http://rutor.info/top"
BASE_URL_NEW = "http://rutor.info/new"

def get_data(url):

    req = requests.get(url)
    html = req.text
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

            all_link_name_size.append({"link": a_href, "name": a_text, "size": size})

def sort_list_dict(how):
    all_link_name_size.sort(key=lambda d: d[how])

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route("/new", methods=["GET"])
    def new():
        all_link_name_size.clear()
        get_data(BASE_URL_NEW)
        sort_list_dict("name")
        print("parse new")
        return render_template("index.html", content=all_link_name_size)

    @app.route("/top", methods=["GET"])
    def top():
        all_link_name_size.clear()
        get_data(BASE_URL_TOP)
        sort_list_dict("name")
        print("parse top")
        return render_template("index.html", content=all_link_name_size)

    count_page = 60
    new_url = []
    for i in range(0, count_page):
        new_url.append("http://rutor.info/browse/{0}/1/0/2".format(i))

    @app.route("/kino", methods=["GET"])
    def kino():
        all_link_name_size.clear()
        
        for i in new_url:
            get_data(i)

        sort_list_dict("name")

        return render_template("index.html", content=all_link_name_size)

    app.run(debug = True, host = "localhost")
