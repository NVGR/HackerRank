def bubble_sort_impl(li):
    """
    Runtime: O(n^2)
    """
    last = len(li)-1
    for i in range(last):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li


if __name__ == '__main__':
    print 'Enter elements separated by space'
    li = [int(x) for x in raw_input().split()]
    print bubble_sort_impl(li)
