
def get_minimum_cost(b, w, x, y, z):
    min_cost = b * x + w * y
    temp_cost = min_cost
    if x < y:
        temp_cost = (b + w) * x + w * z
    elif y < x:
        temp_cost = (b + w) * y + b * z
    min_cost = temp_cost if temp_cost < min_cost else min_cost
    return min_cost

if __name__ == '__main__':
    for _ in xrange(int(raw_input().strip)):
        b, w = raw_input().strip().split(' ')
        b, w = [long(b), long(w)]
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [long(x), long(y), long(z)]
        print get_minimum_cost(b, w, x, y, z)
