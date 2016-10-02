"""
Sample input:
2
10
100

Sample output:
23
2318
"""


def sum_factors_of_n_below_k(k, n):
    m = (k-1) // n
    return n * m * (m+1) // 2


def main():
    for i in range(int(raw_input())):
        k = int(raw_input())

        print sum_factors_of_n_below_k(k, 3) +\
            sum_factors_of_n_below_k(k, 5) - \
            sum_factors_of_n_below_k(k, 15)

if __name__ == "__main__":
    main()
