from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end_of_username: bool = False
    user_id: Optional[int] = None


class AutocompleteTrie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # -------------------------
    # Main operations
    # -------------------------
    def insert(self, username: str, user_id: int) -> None:
        """
        Insert the username character by character into the Trie.
        If a node does not exist, create it.
        At the end, mark the last node as the end of a valid username.
        """
        node = self.root

        for c in username:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_end_of_username = True
        node.user_id = user_id

    def search(self, username: str) -> Optional[int]:
        """
        Traverse the Trie character by character.
        If all characters exist and the last node is an end node,
        return its user_id. Otherwise return None.
        """
        node = self.root

        for c in username:
            if c not in node.children:
                return None
            node = node.children[c]

        if node.is_end_of_username:
            return node.user_id

        return None

    def autocomplete(self, prefix: str, max_results: int = 10) -> List[Tuple[str, int]]:
        """
        Follow the prefix in the Trie.
        If it exists, collect usernames below that prefix node.
        """
        node = self.root
        result: List[Tuple[str, int]] = []

        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        self.collect_words(node, prefix, result, max_results)
        return result

    def delete(self, username: str) -> None:
        """
        Follow the username path.
        If it exists, unmark the final node.
        Then remove useless nodes from bottom to top.
        """
        self.delete_helper(self.root, username, 0)

    # -------------------------
    # Auxiliary operations
    # -------------------------
    def starts_with(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

    def count_words(self) -> int:
        return self.count_words_helper(self.root)

    def count_words_helper(self, node: TrieNode) -> int:
        count = 1 if node.is_end_of_username else 0

        for child in node.children.values():
            count += self.count_words_helper(child)

        return count

    def get_height(self) -> int:
        return self.get_height_helper(self.root)

    def get_height_helper(self, node: TrieNode) -> int:
        if not node.children:
            return 0

        return 1 + max(self.get_height_helper(child) for child in node.children.values())

    def get_total_nodes(self) -> int:
        return self.count_nodes(self.root)

    def count_nodes(self, node: TrieNode) -> int:
        total = 1

        for child in node.children.values():
            total += self.count_nodes(child)

        return total

    def collect_words(
        self,
        node: TrieNode,
        current_word: str,
        result: List[Tuple[str, int]],
        max_results: int,
    ) -> None:
        if len(result) == max_results:
            return

        if node.is_end_of_username and node.user_id is not None:
            result.append((current_word, node.user_id))

        for c in sorted(node.children.keys()):
            if len(result) == max_results:
                return
            self.collect_words(node.children[c], current_word + c, result, max_results)

    def delete_helper(self, node: Optional[TrieNode], username: str, depth: int) -> bool:
        if node is None:
            return False

        if depth == len(username):
            if node.is_end_of_username:
                node.is_end_of_username = False
                node.user_id = None
            return len(node.children) == 0

        c = username[depth]

        if c in node.children:
            should_delete = self.delete_helper(node.children[c], username, depth + 1)

            if should_delete:
                del node.children[c]

        return len(node.children) == 0 and not node.is_end_of_username


# =====================================
# Test set for edge cases
# =====================================

def test_empty_trie() -> None:
    print("=== Test 1: Empty Trie ===")
    trie = AutocompleteTrie()
    print("search('alice'):", trie.search("alice"))
    print("starts_with('al'):", trie.starts_with("al"))
    print("autocomplete('al', 5):", trie.autocomplete("al", 5))
    print()


def test_insert_one_username() -> None:
    print("=== Test 2: Insert one username ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)

    print("search('alice'):", trie.search("alice"))
    print("starts_with('ali'):", trie.starts_with("ali"))
    print("autocomplete('ali', 5):", trie.autocomplete("ali", 5))
    print()


def test_search_non_existing_username() -> None:
    print("=== Test 3: Search non-existing username ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)
    trie.insert("bob", 102)

    print("search('alex'):", trie.search("alex"))
    print()


def test_prefix_exists_but_not_full_username() -> None:
    print("=== Test 4: Prefix exists but full username does not ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)

    print("search('ali'):", trie.search("ali"))
    print("starts_with('ali'):", trie.starts_with("ali"))
    print()


def test_multiple_usernames_same_prefix() -> None:
    print("=== Test 5: Multiple usernames with same prefix ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)
    trie.insert("alex", 102)
    trie.insert("alina", 103)

    print("autocomplete('al', 10):", trie.autocomplete("al", 10))
    print()


def test_autocomplete_with_limit() -> None:
    print("=== Test 6: autocomplete with max_results limit ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)
    trie.insert("alex", 102)
    trie.insert("alina", 103)
    trie.insert("anna", 104)

    print("autocomplete('a', 2):", trie.autocomplete("a", 2))
    print()


def test_delete_existing_username() -> None:
    print("=== Test 7: Delete existing username ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)
    trie.insert("alex", 102)

    print("before delete, search('alice'):", trie.search("alice"))
    trie.delete("alice")
    print("after delete, search('alice'):", trie.search("alice"))
    print("search('alex'):", trie.search("alex"))
    print()


def test_delete_non_existing_username() -> None:
    print("=== Test 8: Delete non-existing username ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)

    before = trie.autocomplete("a", 10)
    trie.delete("bob")
    after = trie.autocomplete("a", 10)

    print("before:", before)
    print("after :", after)
    print()


def test_delete_prefix_username() -> None:
    print("=== Test 9: Delete username that is a prefix of another ===")
    trie = AutocompleteTrie()
    trie.insert("ali", 100)
    trie.insert("alice", 101)

    print("before delete:")
    print("search('ali'):", trie.search("ali"))
    print("search('alice'):", trie.search("alice"))

    trie.delete("ali")

    print("after delete:")
    print("search('ali'):", trie.search("ali"))
    print("search('alice'):", trie.search("alice"))
    print()


def test_count_and_height() -> None:
    print("=== Test 10: Count and height check ===")
    trie = AutocompleteTrie()
    trie.insert("alice", 101)
    trie.insert("alex", 102)
    trie.insert("alina", 103)
    trie.insert("bob", 104)

    print("count_words():", trie.count_words())
    print("get_height():", trie.get_height())
    print("get_total_nodes():", trie.get_total_nodes())
    print()


if __name__ == "__main__":
    test_empty_trie()
    test_insert_one_username()
    test_search_non_existing_username()
    test_prefix_exists_but_not_full_username()
    test_multiple_usernames_same_prefix()
    test_autocomplete_with_limit()
    test_delete_existing_username()
    test_delete_non_existing_username()
    test_delete_prefix_username()
    test_count_and_height()