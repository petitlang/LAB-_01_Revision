from dataclasses import dataclass
from math import floor, log2
from typing import List, Optional
import time
import random


@dataclass
class Post:
    likes: int
    post_id: int
    timestamp: float


class TrendingHeap:
    def __init__(self) -> None:
        self.heap: List[Post] = []

    # -------------------------
    # Auxiliary functions
    # -------------------------
    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def size(self) -> int:
        return len(self.heap)

    def peek_max(self) -> Optional[Post]:
        if self.size() == 0:
            return None
        return self.heap[0]

    def is_valid_heap(self) -> bool:
        for i in range(self.size()):
            l = self.left(i)
            r = self.right(i)

            if l < self.size() and self.heap[i].likes < self.heap[l].likes:
                return False
            if r < self.size() and self.heap[i].likes < self.heap[r].likes:
                return False
        return True

    def get_height(self) -> int:
        n = self.size()
        if n == 0:
            return 0
        return floor(log2(n)) + 1

    def get_level_order(self) -> List[tuple]:
        return [(post.likes, post.post_id, post.timestamp) for post in self.heap]

    # -------------------------
    # Main operations
    # -------------------------
    def push(self, post_id: int, likes: int, timestamp: float) -> None:
        """
        Insert the new post at the end of the heap,
        then move it upward until the max-heap property is restored.
        """
        self.heap.append(Post(likes, post_id, timestamp))
        i = self.size() - 1

        while i > 0 and self.heap[self.parent(i)].likes < self.heap[i].likes:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def pop_max(self) -> Optional[Post]:
        """
        Remove the root, move the last element to the root,
        then move it downward until the max-heap property is restored.
        """
        if self.size() == 0:
            return None

        if self.size() == 1:
            return self.heap.pop()

        max_post = self.heap[0]
        self.heap[0] = self.heap[self.size() - 1]
        self.heap.pop()

        i = 0
        while True:
            largest = i
            l = self.left(i)
            r = self.right(i)

            if l < self.size() and self.heap[l].likes > self.heap[largest].likes:
                largest = l

            if r < self.size() and self.heap[r].likes > self.heap[largest].likes:
                largest = r

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

        return max_post

    def get_top_k(self, k: int) -> List[Post]:
        """
        Copy the heap, then remove the maximum element k times
        from the copied heap.
        """
        temp_heap = TrendingHeap()
        temp_heap.heap = [Post(post.likes, post.post_id, post.timestamp) for post in self.heap]

        result: List[Post] = []
        count = 0

        while temp_heap.size() > 0 and count < k:
            max_post = temp_heap.pop_max()
            if max_post is not None:
                result.append(max_post)
            count += 1

        return result

    def update_likes(self, post_id: int, new_likes: int, timestamp: float) -> None:
        """
        Find the post, update its likes, then restore heap order
        by moving it upward or downward.
        """
        for i in range(self.size()):
            if self.heap[i].post_id == post_id:
                old_likes = self.heap[i].likes
                self.heap[i].likes = new_likes
                self.heap[i].timestamp = timestamp

                # sift up
                if new_likes > old_likes:
                    while i > 0 and self.heap[(i - 1) // 2].likes < self.heap[i].likes:
                        p = (i - 1) // 2
                        self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                        i = p

                # sift down
                else:
                    while True:
                        largest = i
                        l = 2 * i + 1
                        r = 2 * i + 2

                        if l < self.size() and self.heap[l].likes > self.heap[largest].likes:
                            largest = l

                        if r < self.size() and self.heap[r].likes > self.heap[largest].likes:
                            largest = r

                        if largest == i:
                            break

                        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                        i = largest
                return

    def simulate_trending_feed(self) -> None:
        """
        Build the heap with 100 posts, perform 10,000 updates,
        and query top 5 posts every 1,000 updates.
        """
        for i in range(1, 101):
            likes = random.randint(0, 1000)
            timestamp = time.time()
            self.push(i, likes, timestamp)

        for i in range(1, 10001):
            if self.size() == 0:
                break

            post_id = random.choice([post.post_id for post in self.heap])
            new_likes = random.randint(0, 1000)
            timestamp = time.time()
            self.update_likes(post_id, new_likes, timestamp)

            if i % 1000 == 0:
                print(f"\nAfter {i} updates:")
                top5 = self.get_top_k(5)
                for post in top5:
                    print(f"post_id={post.post_id}, likes={post.likes}")


# =====================================
# Test set for edge cases
# =====================================

def print_posts(posts: List[Post]) -> List[tuple]:
    return [(p.likes, p.post_id) for p in posts]


def test_empty_heap() -> None:
    print("=== Test 1: Empty heap ===")
    h = TrendingHeap()
    print("pop_max():", h.pop_max())
    print("peek_max():", h.peek_max())
    print("is_valid_heap():", h.is_valid_heap())
    print()


def test_one_post_only() -> None:
    print("=== Test 2: One post only ===")
    h = TrendingHeap()
    h.push(1, 50, 1.0)
    print("before pop:", h.get_level_order())
    print("pop_max():", h.pop_max())
    print("after pop:", h.get_level_order())
    print()


def test_insert_increasing_likes() -> None:
    print("=== Test 3: Insert with increasing likes ===")
    h = TrendingHeap()
    h.push(1, 10, 1.0)
    h.push(2, 20, 2.0)
    h.push(3, 30, 3.0)
    h.push(4, 40, 4.0)
    print("heap:", h.get_level_order())
    print("root:", h.peek_max())
    print()


def test_insert_decreasing_likes() -> None:
    print("=== Test 4: Insert with decreasing likes ===")
    h = TrendingHeap()
    h.push(1, 40, 1.0)
    h.push(2, 30, 2.0)
    h.push(3, 20, 3.0)
    h.push(4, 10, 4.0)
    print("heap:", h.get_level_order())
    print("root:", h.peek_max())
    print("valid heap:", h.is_valid_heap())
    print()


def test_get_top_k_smaller_than_size() -> None:
    print("=== Test 5: get_top_k(k) with k < n ===")
    h = TrendingHeap()
    h.push(1, 50, 1.0)
    h.push(2, 10, 2.0)
    h.push(3, 80, 3.0)
    h.push(4, 35, 4.0)
    h.push(5, 60, 5.0)

    top3 = h.get_top_k(3)
    print("top 3:", print_posts(top3))
    print("original heap unchanged:", h.get_level_order())
    print()


def test_get_top_k_larger_than_size() -> None:
    print("=== Test 6: get_top_k(k) with k > n ===")
    h = TrendingHeap()
    h.push(1, 50, 1.0)
    h.push(2, 10, 2.0)
    h.push(3, 80, 3.0)

    top10 = h.get_top_k(10)
    print("top 10:", print_posts(top10))
    print()


def test_update_likes_increase() -> None:
    print("=== Test 7: update_likes() with larger value ===")
    h = TrendingHeap()
    h.push(1, 20, 1.0)
    h.push(2, 40, 2.0)
    h.push(3, 30, 3.0)

    print("before:", h.get_level_order())
    h.update_likes(1, 100, 10.0)
    print("after:", h.get_level_order())
    print("root:", h.peek_max())
    print()


def test_update_likes_decrease() -> None:
    print("=== Test 8: update_likes() with smaller value ===")
    h = TrendingHeap()
    h.push(1, 100, 1.0)
    h.push(2, 40, 2.0)
    h.push(3, 30, 3.0)
    h.push(4, 20, 4.0)

    print("before:", h.get_level_order())
    h.update_likes(1, 10, 10.0)
    print("after:", h.get_level_order())
    print("valid heap:", h.is_valid_heap())
    print()


def test_update_likes_missing_post() -> None:
    print("=== Test 9: update_likes() for non-existing post ===")
    h = TrendingHeap()
    h.push(1, 50, 1.0)
    h.push(2, 30, 2.0)

    before = h.get_level_order()
    h.update_likes(99, 100, 10.0)
    after = h.get_level_order()

    print("before:", before)
    print("after :", after)
    print()


def test_heap_validity_check() -> None:
    print("=== Test 10: Heap validity check ===")
    h = TrendingHeap()
    h.push(1, 50, 1.0)
    h.push(2, 20, 2.0)
    h.push(3, 70, 3.0)
    h.push(4, 10, 4.0)
    h.pop_max()
    h.update_likes(2, 80, 5.0)

    print("heap:", h.get_level_order())
    print("is_valid_heap():", h.is_valid_heap())
    print("height:", h.get_height())
    print()


if __name__ == "__main__":
    test_empty_heap()
    test_one_post_only()
    test_insert_increasing_likes()
    test_insert_decreasing_likes()
    test_get_top_k_smaller_than_size()
    test_get_top_k_larger_than_size()
    test_update_likes_increase()
    test_update_likes_decrease()
    test_update_likes_missing_post()
    test_heap_validity_check()

    # Optional full simulation
    # h = TrendingHeap()
    # h.simulate_trending_feed()