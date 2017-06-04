#!/usr/bin/python

import os
import getpass
import random

# find OS to determine Desktop path
t = os.name
nt = "c:\Users\\"
posix = "/home/"
znt = "\\Desktop"
zposix = "/Desktop"
if t == "nt":
	x = nt
	z = znt
else:
	x = posix
	z = zposix

# whodat?
y = getpass.getuser()

# add it up
w = x + y + z

# list your desktop contents for the random picker
u = os.listdir(w)

# what should i play?
print(random.choice(u))

# that's what you should play

# keep the thing open so you don't have to launch a cmd
raw_input("Press enter to exit")
