#!/usr/bin/python3
from __future__ import print_function
def main():
    print("This is the functions.py file.")
    for i in real_inclusive_range(25):
        print(i, end = ' ')
#def inclusive_range(start, stop, step):
#    i = start
#    while i <= stop:
#        yield i
#        i += step
def real_inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('Requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        start = args[0]
        step = 1
        stop = args[1]    
    elif numargs == 3:
        start = args[0]
        step = args[2]
        stop = args[1]
    else:
        raise TypeError('The range can be at max of 3 arguments, got{}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step
if __name__ == "__main__": main()
