def quick_sort_impl(li):
    """
        Runtime: O(nlogn)
    """
    if len(li) <= 1:
        return li
    else:
        pivot_index = len(li) // 2
        pivot = li[pivot_index]
        lesser, greater, pivot_list = [], [], []

        for i, v in enumerate(li):
            if i == pivot_index:
                pivot_list.append(v)
            else:
                if v < pivot:
                    lesser.append(v)
                elif v > pivot:
                    greater.append(v)
                else:
                    pivot_list.append(v)

        return quick_sort_impl(lesser) + pivot_list + quick_sort_impl(greater)


if __name__ == '__main__':
    print 'Enter elements separated by space'
    li = [int(x) for x in raw_input().split()]
    print quick_sort_impl(li)
