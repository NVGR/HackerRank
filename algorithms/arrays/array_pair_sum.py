def get_pairs(li, k):
    found = []
    output = []
    for i in li:
        pair = k - i
        if pair in found:
            output.append((i, pair))
        else:
            found.append(i)
    return output

if __name__ == '__main__':
    print 'Enter the list elements separated by space'
    li = [int(x) for x in raw_input().split()]
    k = int(raw_input())
    print get_pairs(li, k)

