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
    
##  Test set for edge cases
def test_is_balanced_edge_cases():
    print("=== Edge cases: is_balanced ===")

    cases = [
        "",              # empty string
        "()",            # simple balanced
        "({[]})",        # nested balanced
        "(",             # single opening
        ")",             # single closing
        "([)]",          # wrong nesting order
        "(((())))",      # deep nesting
        "[]{}()",        # multiple groups
        "]{",            # starts with closing
        "(((((",         # all openings
        "))))",          # all closings
        "{[()]}",        # balanced mixed
        "{[(])}",        # mismatched mixed
    ]

    for s in cases:
        result = is_balanced(s)
        print(f"is_balanced({s!r}) -> {result}")

if __name__ == "__main__":
    test_is_balanced_edge_cases()