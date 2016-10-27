
if __name__ == '__main__':
    n = raw_input().strip()
    print 2**(bin(n)[2:].count('0')) if n else 1
