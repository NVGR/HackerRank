def get_contiguous_sum(li):
    max_sum, local_max = 0, 0
    for i in li:
        local_max = max(0, local_max + i)
        max_sum = max(max_sum, local_max)
    return max_sum