from __future__ import annotations
from dataclasses import dataclass, field
from math import ceil, log2
import heapq


# =========================================================
# Part 1: Trie for autocomplete
# =========================================================

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_username: bool = False
        self.user_id: int | None = None


class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username: str, user_id: int) -> None:
        node = self.root
        for c in username:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_username = True
        node.user_id = user_id

    def search(self, username: str) -> int | None:
        node = self.root
        for c in username:
            if c not in node.children:
                return None
            node = node.children[c]
        if node.is_end_of_username:
            return node.user_id
        return None

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def autocomplete(self, prefix: str, max_results: int = 10) -> list[tuple[str, int]]:
        node = self.root
        result: list[tuple[str, int]] = []

        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        self._collect_words(node, prefix, result, max_results)
        return result

    def _collect_words(
        self,
        node: TrieNode,
        current_word: str,
        result: list[tuple[str, int]],
        max_results: int,
    ) -> None:
        if len(result) >= max_results:
            return

        if node.is_end_of_username and node.user_id is not None:
            result.append((current_word, node.user_id))

        for c in sorted(node.children.keys()):
            self._collect_words(node.children[c], current_word + c, result, max_results)
            if len(result) >= max_results:
                return

    def delete(self, username: str) -> bool:
        """
        Return True if username existed and was deleted, else False.
        """
        if self.search(username) is None:
            return False

        self._delete_helper(self.root, username, 0)
        return True

    def _delete_helper(self, node: TrieNode | None, username: str, depth: int) -> bool:
        if node is None:
            return False

        if depth == len(username):
            if node.is_end_of_username:
                node.is_end_of_username = False
                node.user_id = None
            return len(node.children) == 0

        c = username[depth]
        if c in node.children:
            should_delete_child = self._delete_helper(node.children[c], username, depth + 1)
            if should_delete_child:
                del node.children[c]

        return (len(node.children) == 0) and (not node.is_end_of_username)


# =========================================================
# Part 2: Heap for trending posts
# =========================================================

@dataclass
class Post:
    likes: int
    post_id: int
    timestamp: int


class TrendingHeap:
    """
    Max-heap by likes.
    Python heapq is min-heap, so we store (-likes, post_id, timestamp).
    """

    def __init__(self):
        self.heap: list[tuple[int, int, int]] = []

    def push(self, post_id: int, likes: int, timestamp: int) -> None:
        heapq.heappush(self.heap, (-likes, post_id, timestamp))

    def pop_max(self) -> Post | None:
        if not self.heap:
            return None
        neg_likes, post_id, timestamp = heapq.heappop(self.heap)
        return Post(-neg_likes, post_id, timestamp)

    def peek_max(self) -> Post | None:
        if not self.heap:
            return None
        neg_likes, post_id, timestamp = self.heap[0]
        return Post(-neg_likes, post_id, timestamp)

    def size(self) -> int:
        return len(self.heap)

    def get_top_k(self, k: int) -> list[Post]:
        temp = self.heap[:]
        result: list[Post] = []
        count = 0

        while temp and count < k:
            neg_likes, post_id, timestamp = heapq.heappop(temp)
            result.append(Post(-neg_likes, post_id, timestamp))
            count += 1

        return result


# =========================================================
# Part 3: BST for users
# =========================================================

class UserBSTNode:
    def __init__(self, user_id: int, name: str, friends: list[int]):
        self.user_id = user_id
        self.name = name
        self.friends = friends[:]
        self.left: UserBSTNode | None = None
        self.right: UserBSTNode | None = None


class UserBST:
    def __init__(self):
        self.root: UserBSTNode | None = None

    def insert(self, user_id: int, name: str, friends_list: list[int]) -> None:
        self.root = self._insert(self.root, user_id, name, friends_list)

    def _insert(
        self,
        root: UserBSTNode | None,
        user_id: int,
        name: str,
        friends_list: list[int],
    ) -> UserBSTNode:
        if root is None:
            return UserBSTNode(user_id, name, friends_list)

        if user_id < root.user_id:
            root.left = self._insert(root.left, user_id, name, friends_list)
        elif user_id > root.user_id:
            root.right = self._insert(root.right, user_id, name, friends_list)
        return root

    def find(self, user_id: int) -> UserBSTNode | None:
        return self._find(self.root, user_id)

    def _find(self, root: UserBSTNode | None, user_id: int) -> UserBSTNode | None:
        if root is None:
            return None
        if user_id == root.user_id:
            return root
        if user_id < root.user_id:
            return self._find(root.left, user_id)
        return self._find(root.right, user_id)

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root: UserBSTNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self._get_height(root.left), self._get_height(root.right))

    def warn_if_degenerate(self, warning_threshold: int = 1000) -> str:
        h = self.get_height()
        if h >= warning_threshold:
            return f"Warning: BST is highly unbalanced. Current height = {h}."
        return f"BST height is acceptable. Current height = {h}."


# =========================================================
# Part 4: Segment Tree
# =========================================================

@dataclass
class SegmentTreeNode:
    left: int = 0
    right: int = 0
    sum: int = 0
    max_value: int = 0
    min_value: int = 0


class ActivitySegmentTree:
    def __init__(self):
        self.tree: list[SegmentTreeNode] = []
        self.activity: list[int] = []
        self.n: int = 0

    def build(self, activity_array: list[int]) -> None:
        self.activity = activity_array[:]
        self.n = len(activity_array)

        if self.n == 0:
            self.tree = []
            return

        self.tree = [SegmentTreeNode() for _ in range(4 * self.n)]
        self._build_helper(1, 0, self.n - 1)

    def _build_helper(self, node: int, start: int, end: int) -> None:
        self.tree[node].left = start
        self.tree[node].right = end

        if start == end:
            value = self.activity[start]
            self.tree[node].sum = value
            self.tree[node].max_value = value
            self.tree[node].min_value = value
            return

        mid = (start + end) // 2
        self._build_helper(2 * node, start, mid)
        self._build_helper(2 * node + 1, mid + 1, end)

        self.tree[node].sum = self.tree[2 * node].sum + self.tree[2 * node + 1].sum
        self.tree[node].max_value = max(
            self.tree[2 * node].max_value,
            self.tree[2 * node + 1].max_value,
        )
        self.tree[node].min_value = min(
            self.tree[2 * node].min_value,
            self.tree[2 * node + 1].min_value,
        )

    def update(self, day: int, value: int) -> bool:
        if day < 0 or day > self.n - 1:
            return False
        self.activity[day] = value
        self._update_helper(1, 0, self.n - 1, day, value)
        return True

    def _update_helper(self, node: int, start: int, end: int, idx: int, value: int) -> None:
        if start == end:
            self.tree[node].sum = value
            self.tree[node].max_value = value
            self.tree[node].min_value = value
            return

        mid = (start + end) // 2
        if idx <= mid:
            self._update_helper(2 * node, start, mid, idx, value)
        else:
            self._update_helper(2 * node + 1, mid + 1, end, idx, value)

        self.tree[node].sum = self.tree[2 * node].sum + self.tree[2 * node + 1].sum
        self.tree[node].max_value = max(
            self.tree[2 * node].max_value,
            self.tree[2 * node + 1].max_value,
        )
        self.tree[node].min_value = min(
            self.tree[2 * node].min_value,
            self.tree[2 * node + 1].min_value,
        )


# =========================================================
# Helpers for nicer output
# =========================================================

def print_case(title: str, expected_result: str, real_result) -> None:
    print(f"--- {title} ---")
    print("Expected Result:")
    print(expected_result)
    print("Real Result:")
    print(real_result)
    print()


def posts_to_simple_list(posts: list[Post]) -> list[tuple[int, int, int]]:
    return [(p.likes, p.post_id, p.timestamp) for p in posts]


# =========================================================
# Main: Edge Cases to Consider
# =========================================================

def main():
    print("===== Edge Cases to Consider =====\n")

    # -----------------------------------------------------
    # Edge Case 1
    # What happens if you try to delete a username from
    # the Trie that doesn't exist?
    # -----------------------------------------------------
    trie = AutocompleteTrie()
    trie.insert("alice", 1)
    trie.insert("alex", 2)

    before_search_alice = trie.search("alice")
    before_search_alex = trie.search("alex")
    delete_result = trie.delete("bob")  # does not exist
    after_search_alice = trie.search("alice")
    after_search_alex = trie.search("alex")

    real_result_1 = {
        "delete_return": delete_result,
        "search_alice_before": before_search_alice,
        "search_alice_after": after_search_alice,
        "search_alex_before": before_search_alex,
        "search_alex_after": after_search_alex,
        "trie_changed": (
            before_search_alice != after_search_alice
            or before_search_alex != after_search_alex
        ),
    }

    print_case(
        "Edge Case 1: Delete non-existing username from Trie",
        "Trie remains unchanged, delete operation returns False or safe message, no crash.",
        real_result_1,
    )

    # -----------------------------------------------------
    # Edge Case 2
    # What happens if get_top_k(1000) is called but only
    # 50 posts exist in the heap?
    # -----------------------------------------------------
    heap = TrendingHeap()
    for i in range(1, 51):
        heap.push(post_id=i, likes=i * 10, timestamp=1000 + i)

    top_1000 = heap.get_top_k(1000)

    real_result_2 = {
        "heap_size": heap.size(),
        "returned_count": len(top_1000),
        "first_5_results": posts_to_simple_list(top_1000[:5]),
        "heap_still_exists": heap.size() == 50,
    }

    print_case(
        "Edge Case 2: get_top_k(1000) with only 50 posts",
        "Return all 50 posts only, no error, original heap unchanged.",
        real_result_2,
    )

    # -----------------------------------------------------
    # Edge Case 3
    # What happens if the BST becomes a degenerate chain
    # (height = 1,000,000)? How would you detect and warn
    # the user?
    # -----------------------------------------------------
    bst = UserBST()
    for i in range(1, 21):  # smaller demo, but clearly skewed
        bst.insert(i, f"User{i}", [])

    height = bst.get_height()
    warning_message = bst.warn_if_degenerate(warning_threshold=10)

    real_result_3 = {
        "insert_order": "increasing order",
        "height": height,
        "warning_threshold": 10,
        "warning_message": warning_message,
    }

    print_case(
        "Edge Case 3: Degenerate BST detection",
        "Detect very large height and print a warning that the BST is highly unbalanced.",
        real_result_3,
    )

    # -----------------------------------------------------
    # Edge Case 4
    # What happens if the Segment Tree receives an update
    # with day = -1 or day > n-1?
    # -----------------------------------------------------
    seg = ActivitySegmentTree()
    seg.build([5, 8, 3, 10, 6])

    result_neg = seg.update(-1, 99)
    result_big = seg.update(10, 99)
    result_valid = seg.update(2, 99)

    real_result_4 = {
        "n": seg.n,
        "update(day=-1, value=99)": result_neg,
        "update(day=10, value=99)": result_big,
        "update(day=2, value=99)": result_valid,
        "activity_after_updates": seg.activity,
    }

    print_case(
        "Edge Case 4: Invalid Segment Tree update index",
        "Invalid indices should be rejected safely; valid index should update normally.",
        real_result_4,
    )


if __name__ == "__main__":
    main()