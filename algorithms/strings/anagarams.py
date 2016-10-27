from itertools import permutations


def get_needle_permutations(needle):
    return ["".join(s) for s in permutations(needle)]


def getAnagramIndices(haystack, needle):
    # WRITE YOUR CODE HERE
    needle_perm = get_needle_permutations(needle)
    li = []
    #print needle_perm
    for x in needle_perm:
        if x in haystack:
            li2 = [n for n in xrange(len(haystack)) if haystack.find(needle, n) == n]
            li.extend(li2)
    return sorted(list(set(li)))


if __name__ == '__main__':
    haystack, needle = raw_input().strip().split()
    #print haystack, needle
    print getAnagramIndices(haystack, needle)