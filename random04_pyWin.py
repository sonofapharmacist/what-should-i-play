#!/usr/bin/python

# determine current Users folder
import getpass
currentUser = getpass.getuser()
print(currentUser)
def desktopFolder = c\Users\currentUser\Desktop

# games list
import os
desktop = os.listdir(desktopFolder)

# random chooser
import random
print(random.choice(desktop))
