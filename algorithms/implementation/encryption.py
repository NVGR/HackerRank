import math


def encrypt_string(s):
    l = len(s)
    row = int(math.floor(l ** 0.5))
    col = int(math.ceil(l ** 0.5))
    li = []
    row = row if row == col else row + 1

    for i in range(row):
        li.append(s[i::col])
        
    return ' '.join(li)


if __name__ == '__main__':
    s = raw_input().strip()
    print encrypt_string(s)