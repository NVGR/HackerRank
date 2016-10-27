import math

if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip())):
        n, m = [int(x) for x in raw_input().split()]
        print int(math.floor(m ** 0.5) - math.ceil(n ** 0.5)) + 1
