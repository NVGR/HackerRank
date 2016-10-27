def get_total_chocolate(n, c, m):
    choc, wrappers = [int(n / c), int(n / c)]
    while wrappers >= m:
        choc += 1
        wrappers -= m
        wrappers += 1
    return choc

if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip())):
        n, c, m = [int(x) for x in raw_input().strip().split(' ')]
        print get_total_chocolate(n, c, m)
