def get_time(h, m):
    word = ["o' clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen",
            "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
            "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

    if m == 45:
        time_str = "quarter to {0}".format(word[h + 1])
    elif m > 30:
        time_str = "{0} minutes to {1}".format(word[60 - m], word[h + 1])
    elif m == 15 or m == 30:
        time_str = "{0} past {1}".format(word[m], word[h])
    elif m == 0:
        time_str = "{0} {1}".format(word[h], word[m])
    else:
        time_str = "{0} minutes past {1}".format(word[m], word[h])

    return time_str

if __name__ == '__main__':
    h = int(raw_input().strip())
    m = int(raw_input().strip())
    print get_time(h, m)
