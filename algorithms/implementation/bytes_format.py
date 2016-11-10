def byte_format(n, round_to=2):
    """
    Runtime: O(1)
    """
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    index = 0
    factor = 1024
    while n > factor:
        n /= factor
        index += 1
    n = "{0}.{1}f".format(n, round_to)
    return "{0} {1}".format(n, units[index])


if __name__ == '__main__':
    n = float(raw_input())
    round_to = int(raw_input())
    print byte_format(n, round_to=round_to)

"""
print byte_format(156833213)  # "149.57 MB"
print byte_format(8101)      # "7.91 KB"
print byte_format(12331, 3)  # "12.042 KB"
"""
