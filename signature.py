#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

e = open("signature.txt", "w")

e.write("Eivind Fonn - http://www.aligulac.com/ - HG J 59\nSeminar für Angewandte Mathematik\nRämistrasse 101, CH-8092 Zürich\n\n")

f = open("signatures.txt")
q = f.readlines()
e.write(q[random.randint(0, len(q)-1)])

e.close()
f.close()
