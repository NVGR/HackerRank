def first_non_repeating(st):
    return [c for c in st if st.count(c) == 1][0]

if __name__ == '__main__':
    print first_non_repeating(raw_input())
