#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    result = 0
    for i in range(1, (leng + 1)):
        result = result + int(sys.argv[i])
    print("{:d}".format(result))
