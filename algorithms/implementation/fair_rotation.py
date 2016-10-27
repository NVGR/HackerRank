def get_carry(B):
    sum = 0
    carry = 0
    for x in B:
        carry = (carry + x) % 2
        sum += carry * 2
    return 'NO' if carry else sum


if __name__ == '__main__':
    N = int(raw_input().strip())
    B = map(int, raw_input().strip().split(' '))
    print get_carry(B)
