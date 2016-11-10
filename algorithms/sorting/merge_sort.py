def merge_sort_impl(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort_impl(left_half)
        merge_sort_impl(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k]=right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    # print("Merging ", alist)
    return alist


if __name__ == '__main__':
    print 'Enter elements separated by space'
    li = [int(x) for x in raw_input().split()]
    print merge_sort_impl(li)
