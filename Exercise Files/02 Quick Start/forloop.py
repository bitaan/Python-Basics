#!/usr/bin/python3

# read the lines from the file
from __future__ import print_function
fh = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/02 Quick Start/lines.txt')
for line in fh.readlines():
    print(line , end='')