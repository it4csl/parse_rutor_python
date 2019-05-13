#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = {"name": {"link": [], "size": []}, "name2": {"link": [], "size": []}}

str2 = ["name", "name2"]

for i in str2:
    str[i]["link"].append("url")
    str[i]["size"].append(1)

#print(str)
for i in str:
    print(i)