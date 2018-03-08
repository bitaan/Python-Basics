#!/usr/bin/python3
from __future__ import print_function
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1 :
            raise TypeError('Requires atleast one argument to work')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start,self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        elif numargs > 3:
            raise Typeerror('Expected 3 arguments, got {}'.format(numargs))
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
def main():
    for i in inclusive_range(25): 
        print(i, end = ' ')

if __name__ == "__main__": main()
