from collections import Counter


def number_needed(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    return sum((c_a - c_b).values()) + sum((c_b - c_a).values())

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)