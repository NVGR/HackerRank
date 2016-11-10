from stack_end_top import Stack


def is_balanced_parentheses(input_str):
    parenth_stack = Stack()
    parenth_dict = {'(': ')', '[': ']', '{': '}'}
    for i in input_str:
        if i in parenth_dict.keys():
            parenth_stack.push(i)
        else:
            if parenth_stack.is_empty():
                return False
            else:
                top = parenth_stack.pop()
                if i == parenth_dict[top]:
                    pass
                else:
                    return False
    return True if parenth_stack.is_empty() else False

if __name__ == '__main__':
    print is_balanced_parentheses(raw_input())
