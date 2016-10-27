"""
Sample input:
2
10 5
3675356291
10 5
2709360626

Sample output:
3150
0
"""


def largest_product(s, d):
    largest_prod = 0
    for i in xrange(0, len(s) - d):
        product = 1
        for j in xrange(i, i + d):
            product *= int(s[j: j + 1])
        if product > largest_prod:
            largest_prod = product
    return largest_prod


def main():
    for i in xrange(int(raw_input())):
        li = raw_input().split()
        n, d = int(li[0]), int(li[1])
        s = raw_input()
        print largest_product(s, d)


if __name__ == '__main__':
    main()
