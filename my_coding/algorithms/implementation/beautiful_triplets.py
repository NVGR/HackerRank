
def get_triplets_count(li, d):
    count = 0
    for i in li:
        if i+d in li and i+(2*d) in li:
            count += 1
    return count

if __name__ == '__main__':
    n, d = [int(x) for x in raw_input().split()]
    li = [int(y) for y in raw_input().split()]
    print get_triplets_count(li, d)