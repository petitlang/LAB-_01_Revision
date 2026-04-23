from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2
from typing import List
import random


@dataclass
class SegmentTreeNode:
    left: int = 0
    right: int = 0
    sum: int = 0
    max_value: int = 0
    min_value: int = 0


class ActivitySegmentTree:
    def __init__(self) -> None:
        self.tree: List[SegmentTreeNode] = []
        self.activity: List[int] = []
        self.n: int = 0

    # -------------------------
    # Main operations
    # -------------------------
    def build(self, activity_array: List[int]) -> None:
        """
        Build the segment tree from the initial activity array.
        Each node stores sum, max_value, and min_value for one interval.
        """
        self.activity = activity_array[:]
        self.n = len(activity_array)

        if self.n == 0:
            self.tree = []
            return

        self.tree = [SegmentTreeNode() for _ in range(4 * self.n)]
        self.build_helper(1, 0, self.n - 1)

    def query(self, l: int, r: int) -> int:
        """
        Return the total number of posts between day l and day r.
        """
        if self.n == 0:
            raise ValueError("The segment tree is empty.")
        if l > r or l < 0 or r >= self.n:
            raise ValueError("Invalid query range.")
        return self.query_sum(1, 0, self.n - 1, l, r)

    def get_range_max(self, l: int, r: int) -> int:
        """
        Return the maximum activity value in the interval [l, r].
        """
        if self.n == 0:
            raise ValueError("The segment tree is empty.")
        if l > r or l < 0 or r >= self.n:
            raise ValueError("Invalid query range.")
        return self.query_max(1, 0, self.n - 1, l, r)

    def get_range_min(self, l: int, r: int) -> int:
        """
        Return the minimum activity value in the interval [l, r].
        """
        if self.n == 0:
            raise ValueError("The segment tree is empty.")
        if l > r or l < 0 or r >= self.n:
            raise ValueError("Invalid query range.")
        return self.query_min(1, 0, self.n - 1, l, r)

    def simulate_activity(self) -> None:
        """
        Start with 30 days of random activity,
        then query the rolling 7-day totals for the last week.
        """
        activity = [random.randint(0, 1000) for _ in range(30)]
        self.build(activity)

        print("Activity array:", activity)
        print("7-day rolling totals for the last week:")

        for i in range(23, 30):
            print(f"days {i - 6} to {i}: {self.query(i - 6, i)}")

    # -------------------------
    # Auxiliary algorithms
    # -------------------------
    def build_helper(self, node: int, start: int, end: int) -> None:
        self.tree[node].left = start
        self.tree[node].right = end

        if start == end:
            self.tree[node].sum = self.activity[start]
            self.tree[node].max_value = self.activity[start]
            self.tree[node].min_value = self.activity[start]
            return

        mid = (start + end) // 2

        self.build_helper(2 * node, start, mid)
        self.build_helper(2 * node + 1, mid + 1, end)

        self.tree[node].sum = self.tree[2 * node].sum + self.tree[2 * node + 1].sum
        self.tree[node].max_value = max(
            self.tree[2 * node].max_value,
            self.tree[2 * node + 1].max_value,
        )
        self.tree[node].min_value = min(
            self.tree[2 * node].min_value,
            self.tree[2 * node + 1].min_value,
        )

    def query_sum(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or l > end:
            return 0

        if l <= start and end <= r:
            return self.tree[node].sum

        mid = (start + end) // 2

        return (
            self.query_sum(2 * node, start, mid, l, r)
            + self.query_sum(2 * node + 1, mid + 1, end, l, r)
        )

    def query_max(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or l > end:
            return float("-inf")

        if l <= start and end <= r:
            return self.tree[node].max_value

        mid = (start + end) // 2

        return max(
            self.query_max(2 * node, start, mid, l, r),
            self.query_max(2 * node + 1, mid + 1, end, l, r),
        )

    def query_min(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or l > end:
            return float("inf")

        if l <= start and end <= r:
            return self.tree[node].min_value

        mid = (start + end) // 2

        return min(
            self.query_min(2 * node, start, mid, l, r),
            self.query_min(2 * node + 1, mid + 1, end, l, r),
        )

    def get_tree_size(self) -> int:
        return len(self.tree)

    def get_height(self) -> int:
        if self.n == 0:
            return 0
        return ceil(log2(self.n)) + 1

    def get_leaf_values(self) -> List[int]:
        return self.activity[:]


# =====================================
# Test set for edge cases
# =====================================

def test_empty_activity_array() -> None:
    print("=== Test 1: Empty activity array ===")
    st = ActivitySegmentTree()
    st.build([])
    print("tree:", st.tree)
    try:
        print("query(0,0):", st.query(0, 0))
    except ValueError as e:
        print("query(0,0):", e)
    print()


def test_one_day_only() -> None:
    print("=== Test 2: One day only ===")
    st = ActivitySegmentTree()
    st.build([15])

    print("query(0,0):", st.query(0, 0))
    print("get_range_max(0,0):", st.get_range_max(0, 0))
    print("get_range_min(0,0):", st.get_range_min(0, 0))
    print()


def test_query_full_range() -> None:
    print("=== Test 3: Query the full range ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("query(0,4):", st.query(0, 4))  # 32
    print()


def test_query_single_day_inside_larger_array() -> None:
    print("=== Test 4: Query a single day inside a larger array ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("query(2,2):", st.query(2, 2))
    print("get_range_max(2,2):", st.get_range_max(2, 2))
    print("get_range_min(2,2):", st.get_range_min(2, 2))
    print()


def test_query_middle_interval() -> None:
    print("=== Test 5: Query a middle interval ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("query(1,3):", st.query(1, 3))  # 21
    print()


def test_range_max_query() -> None:
    print("=== Test 6: Range maximum query ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("get_range_max(1,4):", st.get_range_max(1, 4))
    print()


def test_range_min_query() -> None:
    print("=== Test 7: Range minimum query ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("get_range_min(1,4):", st.get_range_min(1, 4))
    print()


def test_all_values_equal() -> None:
    print("=== Test 8: All values equal ===")
    st = ActivitySegmentTree()
    st.build([7, 7, 7, 7, 7])

    print("query(0,4):", st.query(0, 4))
    print("get_range_max(1,3):", st.get_range_max(1, 3))
    print("get_range_min(1,3):", st.get_range_min(1, 3))
    print()


def test_invalid_range() -> None:
    print("=== Test 9: Invalid range ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    try:
        print("query(4,2):", st.query(4, 2))
    except ValueError as e:
        print("query(4,2):", e)
    print()


def test_out_of_bound_indices() -> None:
    print("=== Test 10: Out-of-bound indices ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    try:
        print("query(-1,3):", st.query(-1, 3))
    except ValueError as e:
        print("query(-1,3):", e)

    try:
        print("query(0,10):", st.query(0, 10))
    except ValueError as e:
        print("query(0,10):", e)
    print()


def test_height_and_tree_size_check() -> None:
    print("=== Test 11: Height and tree size check ===")
    st = ActivitySegmentTree()
    st.build([5, 8, 3, 10, 6])

    print("get_tree_size():", st.get_tree_size())
    print("get_height():", st.get_height())
    print("get_leaf_values():", st.get_leaf_values())
    print()


if __name__ == "__main__":
    test_empty_activity_array()
    test_one_day_only()
    test_query_full_range()
    test_query_single_day_inside_larger_array()
    test_query_middle_interval()
    test_range_max_query()
    test_range_min_query()
    test_all_values_equal()
    test_invalid_range()
    test_out_of_bound_indices()
    test_height_and_tree_size_check()

    # Optional simulation
    # st = ActivitySegmentTree()
    # st.simulate_activity()