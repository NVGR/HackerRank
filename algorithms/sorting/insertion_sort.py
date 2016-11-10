def insertion_sort_impl(li):
    for p in range(1, len(li)):
        while p != 0 and li[p] < li[p-1]:
            li[p], li[p - 1] = li[p - 1], li[p]
            p -= 1
    return li

if __name__ == '__main__':
    print 'Enter elements separated by space'
    li = [int(x) for x in raw_input().split()]
    print insertion_sort_impl(li)
