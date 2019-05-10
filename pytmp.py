#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = {"name": {"link": ["1", "2", "3"], "size": [10, 20, 30]}, "name2": {"link": ["11", "22", "33"], "size": [101, 202, 303]}}
str["name"]["link"].append(6)
print(str[0])