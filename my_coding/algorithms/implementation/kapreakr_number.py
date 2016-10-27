# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_kaprekar_number(p, q):
    li = []
    for i in range(p, q + 1):
        n = str(i ** 2)
        d = len(str(i))
        r_d = n[-d:]
        l_d = n[:-d]
        diff = len(r_d) - len(l_d)
        if diff == 0 or diff == 1:
            l_d = int(l_d) if l_d else 0
            r_d = int(r_d) if r_d else 0
            if i == l_d + r_d:
                li.append(str(i))
    return li


if __name__ == '__main__':
    p = int(raw_input().strip())
    q = int(raw_input().strip())
    li = get_kaprekar_number(p, q)
    if li:
        print ' '.join(li)
    else:
        print 'INVALID RANGE'
