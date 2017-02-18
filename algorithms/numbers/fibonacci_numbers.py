def get_n_fibonacci():
    print 'Enter m value'
    m = int(raw_input())
    a, b = 0, 1
    if m == 1:
        return 0
    li = []
    for _ in xrange(m):
        a, b = b, a+b
        li.append(a)
    return li


def get_nth_fibonacci():
    n = int(raw_input())
    a, b = 0, 1
    if n == 1:
        return 0
    for _ in xrange(n):
        a, b = b, a+b
    return a


def get_fibonacci_inrange():
    start, end = [int(x) for x in raw_input().split()]
    a, b = 0, 1
    li = []
    for i in range(end):
        a , b = b, a+b
        if start <= a:
            li.append(a)
        if a >= end:
            break
    return li

if __name__ == '__main__':
    #n = int(raw_input())
    #print get_n_fibonacci(n)

    print '1. Get first n fibonacci numbers \n 2. Get nth fibonacci number\n 3. get fibonacci numbers in a range'
    print 'Enter your choice'
    n = int(raw_input())
    di = {1: get_n_fibonacci(),
          2: get_nth_fibonacci(),
          3: get_fibonacci_inrange()
          }
    print di[n]
