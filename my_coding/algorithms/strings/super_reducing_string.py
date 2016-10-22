import re


def reduce_string(s):
    match = re.compile(r'(\w)(\1)').search(s)
    while match:
        s = s.replace(match.group(), '')
        if not len(s):
            return 'Empty String'
        match = re.compile(r'(\w)(\1)').search(s)
    return s

if __name__ == '__main__':
    s = raw_input().strip()
    print reduce_string(s)
