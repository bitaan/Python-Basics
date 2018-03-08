#!/usr/bin/python3
from __future__ import print_function
def main():
    buffersize = 50000
    infile = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/15 Files/olives.jpg', 'rb')
    outfile = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/15 Files/new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
        print()
        print('Done')
if __name__ == "__main__": main()
