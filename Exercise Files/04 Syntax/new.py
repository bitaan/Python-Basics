#!/usr/bin/python3


class new:
    def __init__(self, kind = "fried"):
        self.kind = kind
    def kindof(self):
        return self.kind
def main():
    fried = new()
    poach = new('poach')
    print(fried.kindof())

if __name__ == "__main__": main()
