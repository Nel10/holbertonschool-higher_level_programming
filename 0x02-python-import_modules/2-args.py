#!/usr/bin/python3
import sys
if __name__ == "__main__":
    leng = len(sys.argv) - 1
    if leng > 1:
        print(leng, "arguments:")
        for i in range(1, leng + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    elif leng == 1:
        print(leng, "arguments:")
        for i in range(1, leng + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    elif leng == 0:
        print(leng, "arguments.")
