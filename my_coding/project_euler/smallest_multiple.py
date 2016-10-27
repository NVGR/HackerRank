"""
Sample input:
2
3
10

Sample output:
6
2520
"""


def find_smallest_multiple(n):
    for i in xrange(n, factorial(n) + 1, n):
        if is_multiple(i, n):
            return i
    return -1


def is_multiple(x, n):
    for i in xrange(1, n):
        if x % i != 0:
            return False
    return True


# returns the n factorial, or -1 if it does not exist
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n >= 0:
        return 1
    else:
        return -1


def main():
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        print find_smallest_multiple(n)


if __name__ == '__main__':
    main()