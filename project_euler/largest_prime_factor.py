"""
Sample input:
2
10
17

Sample output:
5
17
"""


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def main():
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        print largest_prime_factor(n)


if __name__ == '__main__':
    main()