def selection_sort_impl(li):
    for i in reversed(range(len(li))):
        greatest = 0
        for j in range(1, i + 1):
            if li[j] > li[greatest]:
                greatest = j
        li[i], li[greatest] = li[greatest], li[i]
    return li

if __name__ == '__main__':
    print 'Enter elements separated by space'
    li = [int(x) for x in raw_input().split()]
    print selection_sort_impl(li)