from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
import math


@dataclass
class Post:
    post_id: int
    user_id: int
    content: str
    timestamp: int
    likes: int
    comments: int
    shares: int
    engagement_score: int = 0
    next: Optional["Post"] = None


def compute_score(likes: int, comments: int, shares: int) -> int:
    return likes * 1 + comments * 2 + shares * 3


class PriorityQueue:
    def __init__(self) -> None:
        self.head: Optional[Post] = None
        self.count: int = 0

    def init_queue(self) -> None:
        self.head = None
        self.count = 0

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.count

    def enqueue_post(self, new_post: Post) -> None:
        new_post.engagement_score = compute_score(
            new_post.likes, new_post.comments, new_post.shares
        )
        new_post.next = None

        if self.head is None or new_post.engagement_score > self.head.engagement_score:
            new_post.next = self.head
            self.head = new_post
        else:
            current = self.head
            while (
                current.next is not None
                and current.next.engagement_score >= new_post.engagement_score
            ):
                current = current.next

            new_post.next = current.next
            current.next = new_post

        self.count += 1

    def dequeue_max(self) -> Optional[Post]:
        if self.head is None:
            return None

        max_post = self.head
        self.head = self.head.next
        max_post.next = None
        self.count -= 1
        return max_post

    def peek_max(self) -> Optional[Post]:
        return self.head

    def update_score(
        self,
        post_id: int,
        new_likes: int,
        new_comments: int,
        new_shares: int,
    ) -> None:
        if self.head is not None:
            current = self.head
            previous = None

            while current is not None and current.post_id != post_id:
                previous = current
                current = current.next

            if current is not None:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                self.count -= 1

                current.likes = new_likes
                current.comments = new_comments
                current.shares = new_shares
                current.engagement_score = compute_score(
                    new_likes, new_comments, new_shares
                )
                current.next = None

                self.enqueue_post(current)

    def refresh_all(self) -> None:
        sorted_queue = PriorityQueue()
        sorted_queue.init_queue()

        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None
            current.engagement_score = compute_score(
                current.likes, current.comments, current.shares
            )
            sorted_queue.enqueue_post(current)
            current = next_node

        self.head = sorted_queue.head
        self.count = sorted_queue.count

    def get_top_k(self, k: int) -> List[Post]:
        result: List[Post] = []
        current = self.head
        i = 0

        while current is not None and i < k:
            result.append(current)
            current = current.next
            i += 1

        return result

    def decay_older_than(self, limit_timestamp: int) -> None:
        current = self.head

        while current is not None:
            if current.timestamp < limit_timestamp:
                current.engagement_score = math.floor(current.engagement_score * 0.8)
            current = current.next

        self.refresh_all()

    def to_list(self) -> List[tuple]:
        result = []
        current = self.head
        while current is not None:
            result.append((current.post_id, current.engagement_score))
            current = current.next
        return result
    
if __name__ == "__main__":

    q = PriorityQueue()

    print("---- Edge Case 1: Empty Queue ----")
    print("is_empty:", q.is_empty())
    print("dequeue:", q.dequeue_max())
    print("peek:", q.peek_max())
    print("size:", q.size())
    print()

    print("---- Edge Case 2: Insert into Empty Queue ----")
    p1 = Post(1, 101, "post1", 100, 10, 5, 2)
    q.enqueue_post(p1)
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 3: Insert Higher Score (new head) ----")
    p2 = Post(2, 102, "post2", 100, 30, 10, 5)
    q.enqueue_post(p2)
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 4: Insert Lower Score (tail) ----")
    p3 = Post(3, 103, "post3", 100, 1, 1, 0)
    q.enqueue_post(p3)
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 5: Insert Middle Score ----")
    p4 = Post(4, 104, "post4", 100, 15, 5, 3)
    q.enqueue_post(p4)
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 6: Update Score (increase) ----")
    q.update_score(3, 40, 10, 5)  # should move to head
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 7: Update Non-existing Post ----")
    q.update_score(999, 1, 1, 1)
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 8: Get Top K larger than size ----")
    top = q.get_top_k(10)
    print("top_k:", [(p.post_id, p.engagement_score) for p in top])
    print()

    print("---- Edge Case 9: Dequeue Until Empty ----")
    while not q.is_empty():
        p = q.dequeue_max()
        print("removed:", (p.post_id, p.engagement_score))
    print("queue:", q.to_list())
    print()

    print("---- Edge Case 10: Decay Test ----")
    q.enqueue_post(Post(5, 201, "old post", 50, 20, 5, 5))
    q.enqueue_post(Post(6, 202, "new post", 200, 10, 2, 1))
    print("before decay:", q.to_list())

    q.decay_older_than(100)
    print("after decay:", q.to_list())