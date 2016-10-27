def get_last_stone(n, a, b):
    li = []
    val = (n-1)*a if a <= b else (n-1)*b
    li.append(str(val))
    for i in range(n-1):
        if a == b:
            break
        else:
            val += abs(b-a)
        # if str(val) not in li:    
        #    li.append(str(val))
    return li

if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip())):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        li = get_last_stone(n, a, b)
        print ' '.join(li)
