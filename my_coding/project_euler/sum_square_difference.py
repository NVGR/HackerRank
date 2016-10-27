"""
Sample input:
2
3
10

Sample output:
22
2640
"""


def difference_squaressum_numberssquare(n):
    squares_sum = (n*(n+1)*(2*n+1))/6
    sum_square = (n*(n+1)/2)**2
    return sum_square - squares_sum


def main():
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        print difference_squaressum_numberssquare(n)

if __name__ == '__main__':
    main()
