"""
Sample input:
2
3
6

Sample output:
5
13

http://code.mikeyaworski.com/python/project_euler/problem_8
"""


def sieve_of_eratosthenes_prime(n, l):
    x = l[len(l) - 1]
    while len(l) < n:
        x += 2
        count = 0
        for i in l:
            if i > int(x ** 0.5):
                count = 0
                break
            if x % i == 0:
                count = 1
                break
        if count == 0:
            l.append(x)
    return l


def main():
    l = [2, 3]
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        if len(l) < n:
            l = sieve_of_eratosthenes_prime(n, l)
        print l[n - 1]


if __name__ == '__main__':
    main()
