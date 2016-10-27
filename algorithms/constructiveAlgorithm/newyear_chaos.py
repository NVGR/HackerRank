def get_number_swaps(q):
    length = len(q) - 1
    swaps = 0
    swap_flag = False

    # check if the queue is too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            return "Too chaotic"

    # bubble sorting to find the answer
    for i in xrange(length):
        for j in xrange(length):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                swaps += 1
                swap_flag = True
        if swap_flag:
            swap_flag = False
        else:
            break
    return swaps


if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip())):
        q = [int(x) for x in raw_input().strip().split()]
        print get_number_swaps(q)
