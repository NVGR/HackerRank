"""
John's clothing store has a pile of  loose socks where each sock  is labeled with an integer, , denoting its color. He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks, and , are a single matching pair if .
Given  and the color of each sock, how many pairs of socks can John sell?

Input Format
The first line contains an integer, , denoting the number of socks.
The second line contains  space-separated integers describing the respective values of .

Output Format
Print the total number of matching pairs of socks that John can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
"""
from collections import Counter


def paired_socks_count(c):
    count = 0
    co = Counter(c)
    for i in co:
        count += co[i] / 2
    return count


def main():
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    print paired_socks_count(c)

if __name__ == '__main__':
    main()
