def firstUniqueCharacterFinder(s):

    if len(s) == 0:
        return -1

    dic = {}



    for i in range(0, len(s)):
        c = s[i]

        if c not in dic:
            dic[c] = 1
        else:
            dic[c] = dic[c] + 1

    
    for i in range(0, len(s)):
        c = s[i]

        if dic[c] == 1:
            return i

    return -1


# -------------------- test --------------------
def test():
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("ddaccabba", 8),

        ("", -1),                
        ("a", 0),                
        ("aaaa", -1),             
    ]

    print("=== First Unique Character Tests ===\n")

    for s, expected in test_cases:
        output = firstUniqueCharacterFinder(s)

        print(f"Input:    \"{s}\"")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")

        if output == expected:
            print("test: successful")
        else:
            print("test: failed")

        print()


if __name__ == "__main__":
    test()