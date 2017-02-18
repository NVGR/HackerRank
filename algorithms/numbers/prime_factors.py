def get_prime_factors(n):
    i = 2
    li = []
    while i**2 <= n:
        if n % i == 0:
            li.append(i)
        while n % i == 0:
            n /= i
        i += 1
    if n > 1:
        li.append(n)
    return li


if __name__ == '__main__':
    n = int(raw_input())
    print get_prime_factors(n)