#!/usr/bin/python3
from __future__ import print_function
import re
def main():
    text_to_search = ''' where were you,
    when i was hurt Neverore helpless
    wehn Nevermore days slipped by,
    from Nevermore my window watching
    When you were hanging your head
    on someone else's words 
    Nevermore'''
    fh = open('f:/NPTEL/Secure/Coding Essentials/Totally Interested\Python/Python 3 Essential Training/Exercise Files/Ex_Files_Python_3_EssT/Exercise Files/09 Regexes/raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('@#$',line), end='')
    pattern = re.compile(r'Nevermore')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

if __name__ == "__main__": main()
