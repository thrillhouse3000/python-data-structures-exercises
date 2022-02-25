def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    op = [p for p in parens if p == '(']
    cp = [p for p in parens if p == ')']
    
    if not len(op) == len(cp) or parens[0] == ')':
        return False
    else:
        return True
