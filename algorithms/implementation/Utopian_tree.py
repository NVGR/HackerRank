def get_tree_height(n):
    val = 1
    if n == 0:
        return 1
    for i in range(1, n+1):
        val = val*2 if i % 2 else val+1
    return val


if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip())):
        n = int(raw_input().strip())
        print get_tree_height(n)

