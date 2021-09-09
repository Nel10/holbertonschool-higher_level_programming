#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    if leng == 0:
        print("{:d} arguments.".format(leng))
    elif leng == 1:
        print("{:d} argument:".format(leng))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(leng))
        for i in range(1, leng + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
