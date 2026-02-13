def RotateTemp(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    Temp = [None] * n

    for i in range(0, n):
        Temp[(i + k) % n] = Vect[i]

    for i in range(0, n):
        Vect[i] = Temp[i]

    return Vect


def RotateOneByOne(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    for step in range(1, k + 1):
        last = Vect[n - 1]

        for i in range(n - 1, 0, -1):
            Vect[i] = Vect[i - 1]

        Vect[0] = last

    return Vect

def Reverse(Vect, left, right):
    while left < right:
        temp = Vect[left]
        Vect[left] = Vect[right]
        Vect[right] = temp

        left = left + 1
        right = right - 1


def RotateReverse(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    Reverse(Vect, 0, n - 1)
    Reverse(Vect, 0, k - 1)
    Reverse(Vect, k, n - 1)
    
    return Vect

##  Test set for edge cases
def test_rotation_edge_cases():
    print("\n=== Edge cases: array rotations ===")

    rotation_cases = [
        ([], 0),                 # empty vector
        ([1], 0),                # single element, k=0
        ([1], 5),                # single element, k>n
        ([1, 2, 3, 4, 5], 0),     # k=0
        ([1, 2, 3, 4, 5], 5),     # k=n
        ([1, 2, 3, 4, 5], 6),     # k>n
        ([1, 2, 3, 4, 5], 1),     # small rotate
        ([1, 2, 3, 4, 5], 2),     # typical rotate
        ([1, 2, 3, 4, 5], -1),    # negative k
        ([1, 2, 3, 4, 5], -6),    # negative k with abs(k)>n
    ]

    for vect, k in rotation_cases:
        # so we pass copies to keep test inputs clean.
        v1 = vect[:]
        v2 = vect[:]
        v3 = vect[:]

        out1 = RotateTemp(v1, k)
        out2 = RotateOneByOne(v2, k)
        out3 = RotateReverse(v3, k)

        print(f"Vect={vect}, k={k}")
        print(f"  RotateTemp     -> {out1}")
        print(f"  RotateOneByOne -> {out2}")
        print(f"  RotateReverse  -> {out3}")

if __name__ == "__main__":
    test_rotation_edge_cases()