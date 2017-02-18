def get_factors(n):
    i = 1
    li = []
    while i**2 <= n:
        if n % i == 0:
            li.append(i)
            li.append(n/i)
        i += 1
    return sorted(li)


if __name__ == '__main__':
    n = int(raw_input())
    print get_factors(n)

