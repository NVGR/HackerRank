from stack_end_top import Stack


def is_balanced_parentheses(input_str):
    parenth_stack = Stack()
    for i in input_str:
        if i == '(':
            parenth_stack.push(i)
        elif i == ')':
            if parenth_stack.is_empty():
                return False
            else:
                parenth_stack.pop()
    parenth_stack.print_stack()
    return True if parenth_stack.is_empty() else False


if __name__ == '__main__':
    print is_balanced_parentheses(raw_input())
