def is_balanced(s: str):
    stack = []
    comparisons = 0

    for ch in s:
        
        comparisons += 1
        if ch in "([{":
            stack.append(ch)
        else:
            comparisons += 1
            if not stack:
                return False, comparisons

            top = stack.pop()

            comparisons += 1
            if (ch == ')' and top != '(') or (ch == ']' and top != '[') or (ch == '}' and top != '{'):
                return False, comparisons

    comparisons += 1
    if not stack:
        return True, comparisons
    else:
        return False, comparisons
