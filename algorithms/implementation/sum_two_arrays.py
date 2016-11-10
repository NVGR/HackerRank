from itertools import izip_longest
import operator


def perform_operation_arrays(li1, li2, op):
    li3 = []
    for i, j in izip_longest(li1, li2):
        if i and j:
            if op == 'add':
                li3.append(operator.add(i, j))
            elif op == 'sub':
                li3.append(operator.sub(i, j))
            elif op == 'mul':
                li3.append(operator.mul(i, j))
            elif op == 'div':
                li3.append(operator.div(i, j))
            elif op == 'mod':
                li3.append(operator.mod(i, j))
            elif op == 'floordiv':
                li3.append(operator.floordiv(i, j))

            # val = eval('{0}{1}{2}'.format(i, op, j))
            # li3.append(val)
        elif i and op in ['add', 'sub']:
            li3.append(i)
        elif j and op in ['add', 'sub']:
            li3.append(j)
    return li3

if __name__ == '__main__':
    li1 = [int(x) for x in raw_input().split()]
    li2 = [int(x) for x in raw_input().split()]
    print 'Enter Operator:  It should be in add, mul, sub, mod, div, floordiv'
    op = raw_input()
    print perform_operation_arrays(li1, li2, op)
