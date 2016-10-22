# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_sum_flip_matrix(matrix, n):
    r = 2*n - 1
    max_sum = 0
    for p in range(n):
        for q in range(n):
            i1 = r - p
            j1 = r - q
            max_sum = max_sum + max(matrix[p][q], matrix[p][j1], matrix[i1][q], matrix[i1][j1])
    return max_sum


if __name__ == '__main__':
    for _ in xrange(int(raw_input())):
        n = int(raw_input().strip())
        matrix = []
        for _ in xrange(2*n):
            li = [int(x) for x in raw_input().strip().split()]
            matrix.append(li)
        print max_sum_flip_matrix(matrix, n)
