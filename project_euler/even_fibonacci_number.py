"""
Sample input:
2
10
100

Sample output:
10
44
"""


def even_fibonacci(maximum):
    f1, f2 = 0, 1
    while f1 < maximum:
        if f1 % 2 == 0:
            yield f1
        f1, f2 = f2, f1 + f2


def main():
    for i in xrange(int(raw_input())):
        maximum = int(raw_input())
        even_sum = 0
        for x in even_fibonacci(maximum):
            even_sum += x
        print even_sum


if __name__ == '__main__':
    main()