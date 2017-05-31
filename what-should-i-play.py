#!/usr/bin/python

import os
import getpass
import random

# assuming you're in windows
x = 'c:\Users\\'

# whodat?
y = getpass.getuser()

# assuming you're in windows
z = '\\Desktop'

# add it up
w = x + y + z

# list your desktop contents for the random picker
u = os.listdir(w)

# what should i play?
print(random.choice(u))

# that's what you should play

# keep the thing open so you don't have to launch a cmd
raw_input("Press enter to exit")