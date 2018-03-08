#!/usr/bin/python3
from __future__ import print_function
def main():
    fh = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/02 Quick Start/lines.txt')
    for index,line in enumerate(fh.readlines()):
        print(index, line, end = '')
    s = "This is a string"
    for i, c in enumerate(s):
        print(i,c)

if __name__ == "__main__": main()
