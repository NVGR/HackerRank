"""
a+b+c = N
a2 + b2 = c2
return a*b*c
Sample input:
2
12
4

Sample output:
60
-1
http://code.jasonbhill.com/python/project-euler-problem-9/
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt 
"""


def special_pythageorean(n):
    for a in xrange(1, n/2):
        b = int((a**2 - ((a-n)**2))/(2*(a-n)))
        if b < a:
            return -1
        c = int((a**2 + b**2)**0.5)
        #print a, b, c
        if a+b+c == n:
            return a*b*c
    return -1


def main():
    for i in xrange(int(raw_input())):
        n = int(raw_input())
        print special_pythageorean(n)


if __name__ == '__main__':
    main()