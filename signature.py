#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

e = open("/home/efonn/repos/signature/signature.txt", "w")

e.write("Eivind Fonn - http://www.aligulac.com/ - HG J 59<br>Seminar für Angewandte Mathematik<br>Rämistrasse 101, CH-8092 Zürich<br><br>")

f = open("/home/efonn/repos/signature/signatures.txt")
q = f.readlines()
e.write(q[random.randint(0, len(q)-1)])

e.close()
f.close()
