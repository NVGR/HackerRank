"""
Sample input:
2
101110
800000

Sample output:
101101
793397
"""


def largest_palindrom_n(n):
    maximum = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            res = x * y
            if res <= n and str(res) == str(res)[::-1]:
                maximum = res if res > maximum else maximum
    print maximum


def main():
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        largest_palindrom_n(n)


if __name__ == '__main__':
    main()