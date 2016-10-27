"""
You are given an array of  integers, , and a positive integer, . Find and print the number of pairs where  and  +  is evenly divisible by .

Input Format
The first line contains  space-separated integers,  and , respectively.
The second line contains  space-separated integers describing the respective values of .

Output Format
Print the number of  pairs where  and  +  is evenly divisible by .

Sample Input
6 3
1 3 2 6 1 2

Sample Output
5

"""


def divisible_sum_pair(a, k):
    count = 0
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % k == 0:
                count += 1
    return count


def main():
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    # a = map(int, raw_input().strip().split(' '))
    a = [int(x) for x in raw_input().strip().split(' ')]
    print divisible_sum_pair(a, k)


if __name__ == '__main__':
    main()