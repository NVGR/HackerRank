def max_sublist_sum_positions(l):
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur+i > 0:
            cur += i
        else: # reset start position
            cur, curi = 0, ind+1

        if cur > best:
            starti, besti, best = curi, ind+1, cur
    return starti, besti, best


def max_sublist_sum(l):
    best = cur = 0
    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best

