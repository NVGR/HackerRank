def get_duplicate_intigers(li):
    return [x for x in li if li.count(x) > 1]

if __name__ == '__main__':
    li = [int(x) for x in raw_input().split()]
    print get_duplicate_intigers(li)
