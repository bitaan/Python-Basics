#!/usr/bin/python3
import bitstring
def main():
    a = bitstring.Bitstring(bin = '01010101')
    print(a.hex, a.bin, a.uint)
if __name__ == "__main__": main()
