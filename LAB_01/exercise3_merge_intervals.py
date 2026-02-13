from typing import List, Tuple


def mergeOverLappingIntervals(interval):

    if len(interval) == 0:
        return []

   
    interval.sort()  

    result = []
    a_start, a_end = interval[0]

    for i in range(1, len(interval)):
        b_start, b_end = interval[i]

        if b_start <= a_end: 
            a_end = max(a_end, b_end)
        else:  
            result.append((a_start, a_end))
            a_start, a_end = b_start, b_end

    result.append((a_start, a_end))
    return result


# -------------------- test --------------------
def tests():
    test_cases = [
        ([(1, 3), (2, 6), (15, 18), (8, 10)], [(1, 6), (8, 10), (15, 18)]),
        ([(1, 4), (4, 5)], [(1, 5)]),
        ([(1, 4), (0, 4)], [(0, 4)]),

        ([], []),
        ([(5, 7)], [(5, 7)]),
        ([(1, 2), (3, 4)], [(1, 2), (3, 4)]),
        ([(0, 0), (0, 0)], [(0, 0)]),
    ]


    for interval, expected in test_cases:
        output = mergeOverLappingIntervals(interval)
        print(f"Input:  {interval}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")

        if output == expected:
            print("test: successful")
        else:
            print("test: failed")

        print()

if __name__ == "__main__":
    tests()


