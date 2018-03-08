#!/usr/bin/python3
from __future__ import print_function
def main():
    print('This is the containers.py file.')
    fin = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/14 Containers/utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('$#{:04d};' .format(ord(c)),encoding = 'utf_8')
            else:
                outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr , file = fout)
    print(outstr)
    print('Done.')

if __name__ == "__main__": main()
