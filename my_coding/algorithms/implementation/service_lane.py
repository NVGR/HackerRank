
if __name__ == '__main__':
    n, t = [int(x) for x in raw_input().strip().split(' ')]
    width = map(int, raw_input().strip().split(' '))
    for _ in xrange(t):
        i, j = raw_input().strip().split(' ')
        i, j = [int(i), int(j)]
        print min(width[i:j+1])