#!/usr/bin/python3
from __future__ import print_function
def main():
    try:
        fh = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/xlines.txt')
    except IOError as e:
        print("Couldn't find the file you are looking for, because:",e)
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()
