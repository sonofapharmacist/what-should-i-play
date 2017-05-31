#!/usr/bin/python

import os
import getpass
import random

x = 'c:\Users\\'
y = getpass.getuser()
z = '\\Desktop'
w = x + y + z
u = os.listdir(w)

print(random.choice(u))
