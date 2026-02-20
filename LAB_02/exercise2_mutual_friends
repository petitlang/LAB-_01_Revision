def intersection(set1: set, set2: set) -> set:
    mutual = set()
    for x in set1:
        if x in set2:
            mutual.add(x)
    return mutual

def difference(set1: set, set2: set) -> set:
    diff = set()
    for x in set1:
        if x not in set2:
            diff.add(x)
    return diff

def union(set1: set, set2: set) -> set:
    uni = set()
    for x in set1:
        uni.add(x)
    for y in set2:
        uni.add(y)
    return uni

def mutual_friend_coefficient(set1: set, set2: set) -> float:
    uni = union(set1, set2)
    if len(uni) == 0:
        return 0.0
    inter = intersection(set1, set2)
    return len(inter) / len(uni)

# Edge Case Test Sets

# situation 1: both sets empty
a1 = set()
b1 = set()

# situation 2: one empty, one non-empty
a2 = set()
b2 = {1, 2, 3}

# situation 3: identical sets
a3 = {1, 2, 3}
b3 = {1, 2, 3}

# situation 4: no mutual friends
a4 = {1, 2, 3}
b4 = {4, 5, 6}

# situation 5: one set is a subset of the other
a5 = {1, 2, 3, 4}
b5 = {2, 3}

# situation 6: single-element sets
a6 = {1}
b6 = {1}

a7 = {1}
b7 = {2}

# situation 7: very unbalanced set sizes
a8 = set(range(1, 10001))   # large set
b8 = {5000}                # small set

test_cases = [
    (a1, b1),
    (a2, b2),
    (a3, b3),
    (a4, b4),
    (a5, b5),
    (a6, b6),
    (a7, b7),
    (a8, b8),
]

for i, (a, b) in enumerate(test_cases, start=1):
    print(f"\n--- Situation {i} ---")
    print("A:", a)
    print("B:", b)
    print("Intersection:", intersection(a, b))
    print("Difference A-B:", difference(a, b))
    print("Difference B-A:", difference(b, a))
    print("Union:", union(a, b))
    print("Jaccard:", mutual_friend_coefficient(a, b))