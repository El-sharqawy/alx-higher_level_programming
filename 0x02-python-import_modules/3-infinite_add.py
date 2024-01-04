#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    import sys

    args = sys.argv[1:]
    num = 0
    for arg in args:
        num += int(arg)
    print("{:d}".format(num))
