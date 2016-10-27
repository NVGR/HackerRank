import operator


def lonely_integer(a):
    answer = reduce(operator.xor, a)
    return answer

if __name__ == '__main__':
    a = raw_input()
    b = map(int, raw_input().strip().split(" "))
    print lonely_integer(b)
