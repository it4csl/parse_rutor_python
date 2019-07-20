#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = []

arr = [{"a": "name", "b": "link1", "ar": 100},
        {"a": "name", "b": "link2", "ar": 200},
        {"a": "name1", "b": "link3", "ar": 300},
        {"a": "name1", "b": "link4", "ar": 400},
        {"a": "name2", "b": "link5", "ar": 500}]

arr2 = [{"a2": "name", "b2": [], "ar2": []}]

arr2_l = len(arr2)
for i in arr:
    if (len(arr2) != 0): 
        if (i["a"] == (arr2[(arr2_l-1)]["a2"])):
            arr2[(arr2_l-1)]["b2"].append(i["b"])
            arr2[(arr2_l-1)]["ar2"].append(i["ar"])

        if (i["a"] != (arr2[(arr2_l-1)]["a2"])):
            arr2.append(i)

        # print(i["a"])
for i in arr2:    
    print(i)
