#!/usr/bin/python3

def main():
    choices = dict(
        one = '1',
        two = '2',
        three = '3',
        four = '4',
        five = '5',
    )
    v = 'three'
    print( choices.get(v, 'other'))

if __name__ == "__main__": main()
