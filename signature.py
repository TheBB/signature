#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import os

homedir = os.getenv('HOME')

e = open(homedir + "/repos/signature/signature.txt", "w")

e.write("Eivind Fonn - http://www.aligulac.com/<br>SINTEF IKT Anvendt Matematikk<br>Strindveien 4, 7034 Trondheim<br><br>")

f = open(homedir + "/repos/signature/signatures.txt")
q = f.readlines()
e.write(q[random.randint(0, len(q)-1)])

e.close()
f.close()
