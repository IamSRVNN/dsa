from main import ArrayStack


# matching delimiters
def is_matched(expr):
    stack = ArrayStack()

    lefty = '([{'
    righty = ')]}'
    for element in expr:
        if element in lefty:
            stack.push(element)
        elif element in righty:
            if (stack.is_empty()) or (lefty.index(stack.pop()) != righty.index(element)):
                return False
    return stack.is_empty()


if __name__ == '__main__':
    print(is_matched("( )(( )){([( )])}"))
    print(is_matched("((( )(( )){([( )])}))"))
    print(is_matched(")(( )){([( )])}"))
    print(is_matched("({[ ])}"))
    print(is_matched("("))
