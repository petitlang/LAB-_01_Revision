from __future__ import annotations


class UserBSTNode:
    def __init__(self, user_id: int, name: str, friends: list[int]):
        self.user_id = user_id
        self.name = name
        self.friends = friends[:] if friends else []
        self.left: UserBSTNode | None = None
        self.right: UserBSTNode | None = None


class UserBST:
    def __init__(self):
        self.root: UserBSTNode | None = None

    # 1. insert(root, user_id, name, friends_list)
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
        # if equal, do nothing
        return root

    # 2. find(root, user_id)
    def find(self, user_id: int) -> UserBSTNode | None:
        return self._find(self.root, user_id)

    def _find(self, root: UserBSTNode | None, user_id: int) -> UserBSTNode | None:
        if root is None:
            return None

        if user_id == root.user_id:
            return root
        elif user_id < root.user_id:
            return self._find(root.left, user_id)
        else:
            return self._find(root.right, user_id)

    # 3. inorder_traversal(root)
    def inorder_traversal(self) -> list[int]:
        result: list[int] = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, root: UserBSTNode | None, result: list[int]) -> None:
        if root is not None:
            self._inorder_helper(root.left, result)
            result.append(root.user_id)
            self._inorder_helper(root.right, result)

    # 4. find_min(root)
    def _find_min(self, root: UserBSTNode | None) -> UserBSTNode | None:
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    # 5. delete(root, user_id)
    def delete(self, user_id: int) -> None:
        self.root = self._delete(self.root, user_id)

    def _delete(self, root: UserBSTNode | None, user_id: int) -> UserBSTNode | None:
        if root is None:
            return None

        if user_id < root.user_id:
            root.left = self._delete(root.left, user_id)
        elif user_id > root.user_id:
            root.right = self._delete(root.right, user_id)
        else:
            # case 1: no left child
            if root.left is None:
                return root.right
            # case 2: no right child
            elif root.right is None:
                return root.left

            # case 3: two children
            temp = self._find_min(root.right)
            if temp is not None:
                root.user_id = temp.user_id
                root.name = temp.name
                root.friends = temp.friends[:]
                root.right = self._delete(root.right, temp.user_id)

        return root

    # 6. suggest_friends(root, user_id, max_suggestions)
    def suggest_friends(self, user_id: int, max_suggestions: int = 5) -> list[tuple[int, int]]:
        user = self.find(user_id)

        if user is None:
            return []

        direct_friends = set(user.friends)
        direct_friends.add(user.user_id)

        freq: dict[int, int] = {}

        for friend_id in user.friends:
            friend_node = self.find(friend_id)

            if friend_node is not None:
                for fof_id in friend_node.friends:
                    if fof_id not in direct_friends:
                        if fof_id not in freq:
                            freq[fof_id] = 1
                        else:
                            freq[fof_id] += 1

        result: list[tuple[int, int]] = []
        for candidate_id in freq:
            result.append((candidate_id, freq[candidate_id]))

        # sort by frequency descending, then by user_id ascending
        result.sort(key=lambda x: (-x[1], x[0]))
        return result[:max_suggestions]

    # 7. get_height(root)
    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root: UserBSTNode | None) -> int:
        if root is None:
            return 0

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        return 1 + max(left_height, right_height)

    # 8. is_balanced(root)
    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)

    def _is_balanced(self, root: UserBSTNode | None) -> bool:
        if root is None:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(root.left) and self._is_balanced(root.right)

    # 9. get_leaf_count(root)
    def get_leaf_count(self) -> int:
        return self._get_leaf_count(self.root)

    def _get_leaf_count(self, root: UserBSTNode | None) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self._get_leaf_count(root.left) + self._get_leaf_count(root.right)

    # helper: print nodes in-order with details
    def print_inorder_detailed(self) -> None:
        nodes = []
        self._collect_inorder_nodes(self.root, nodes)
        for node in nodes:
            print(f"user_id={node.user_id}, name={node.name}, friends={node.friends}")

    def _collect_inorder_nodes(self, root: UserBSTNode | None, nodes: list[UserBSTNode]) -> None:
        if root is not None:
            self._collect_inorder_nodes(root.left, nodes)
            nodes.append(root)
            self._collect_inorder_nodes(root.right, nodes)


def main():
    print("===== Test Set for Edge Cases =====\n")

    # --------------------------------------------------
    # Edge Case 1: Empty tree
    # --------------------------------------------------
    print("--- Edge Case 1: Empty tree ---")
    bst1 = UserBST()
    print("inorder_traversal:", bst1.inorder_traversal())
    print("find(10):", bst1.find(10))
    print("suggest_friends(1):", bst1.suggest_friends(1))
    print("get_height:", bst1.get_height())
    print("is_balanced:", bst1.is_balanced())
    print("get_leaf_count:", bst1.get_leaf_count())
    bst1.delete(10)  # should not crash
    print("after delete(10):", bst1.inorder_traversal())
    print()

    # --------------------------------------------------
    # Edge Case 2: Single node tree
    # --------------------------------------------------
    print("--- Edge Case 2: Single node tree ---")
    bst2 = UserBST()
    bst2.insert(10, "Alice", [])
    print("inorder_traversal:", bst2.inorder_traversal())
    node = bst2.find(10)
    print("find(10):", (node.user_id, node.name, node.friends) if node else None)
    print("suggest_friends(10):", bst2.suggest_friends(10))
    print("get_height:", bst2.get_height())
    print("is_balanced:", bst2.is_balanced())
    print("get_leaf_count:", bst2.get_leaf_count())
    bst2.delete(10)
    print("after delete(10):", bst2.inorder_traversal())
    print()

    # --------------------------------------------------
    # Edge Case 3: Find non-existing user
    # --------------------------------------------------
    print("--- Edge Case 3: Find non-existing user ---")
    bst3 = UserBST()
    bst3.insert(20, "Bob", [30])
    bst3.insert(10, "Carol", [20])
    bst3.insert(30, "David", [20])
    node = bst3.find(99)
    print("inorder_traversal:", bst3.inorder_traversal())
    print("find(99):", node)
    print()

    # --------------------------------------------------
    # Edge Case 4: Insert duplicate user_id
    # --------------------------------------------------
    print("--- Edge Case 4: Insert duplicate user_id ---")
    bst4 = UserBST()
    bst4.insert(15, "Eva", [25])
    bst4.insert(15, "Eva-duplicate", [99])  # duplicate, should be ignored
    print("inorder_traversal:", bst4.inorder_traversal())
    bst4.print_inorder_detailed()
    print()

    # --------------------------------------------------
    # Edge Case 5: Delete leaf node
    # --------------------------------------------------
    print("--- Edge Case 5: Delete leaf node ---")
    bst5 = UserBST()
    bst5.insert(20, "A", [])
    bst5.insert(10, "B", [])
    bst5.insert(30, "C", [])
    bst5.insert(5, "D", [])
    print("before delete(5):", bst5.inorder_traversal())
    bst5.delete(5)
    print("after delete(5):", bst5.inorder_traversal())
    print("get_height:", bst5.get_height())
    print("is_balanced:", bst5.is_balanced())
    print("get_leaf_count:", bst5.get_leaf_count())
    print()

    # --------------------------------------------------
    # Edge Case 6: Delete node with one child
    # --------------------------------------------------
    print("--- Edge Case 6: Delete node with one child ---")
    bst6 = UserBST()
    bst6.insert(20, "A", [])
    bst6.insert(10, "B", [])
    bst6.insert(5, "C", [])
    print("before delete(10):", bst6.inorder_traversal())
    bst6.delete(10)
    print("after delete(10):", bst6.inorder_traversal())
    bst6.print_inorder_detailed()
    print()

    # --------------------------------------------------
    # Edge Case 7: Delete node with two children
    # --------------------------------------------------
    print("--- Edge Case 7: Delete node with two children ---")
    bst7 = UserBST()
    bst7.insert(20, "A", [])
    bst7.insert(10, "B", [])
    bst7.insert(30, "C", [])
    bst7.insert(25, "D", [])
    bst7.insert(35, "E", [])
    print("before delete(20):", bst7.inorder_traversal())
    bst7.delete(20)
    print("after delete(20):", bst7.inorder_traversal())
    bst7.print_inorder_detailed()
    print()

    # --------------------------------------------------
    # Edge Case 8: Friend suggestion with no suggestions
    # --------------------------------------------------
    print("--- Edge Case 8: Friend suggestion with no suggestions ---")
    bst8 = UserBST()
    bst8.insert(1, "Alice", [2])
    bst8.insert(2, "Bob", [1])
    print("suggest_friends(1):", bst8.suggest_friends(1))
    print()

    # --------------------------------------------------
    # Edge Case 9: Friend suggestion with valid FoF results
    # --------------------------------------------------
    print("--- Edge Case 9: Friend suggestion with valid FoF results ---")
    bst9 = UserBST()
    bst9.insert(1, "Alice", [2, 3])
    bst9.insert(2, "Bob", [1, 4, 5])
    bst9.insert(3, "Carol", [1, 4])
    bst9.insert(4, "David", [2, 3, 6])
    bst9.insert(5, "Eva", [2])
    bst9.insert(6, "Frank", [4])

    print("inorder_traversal:", bst9.inorder_traversal())
    print("suggest_friends(1):", bst9.suggest_friends(1))
    print("suggest_friends(4):", bst9.suggest_friends(4))
    print()

    # --------------------------------------------------
    # Edge Case 10: Friend list contains user not in BST
    # --------------------------------------------------
    print("--- Edge Case 10: Friend list contains user not in BST ---")
    bst10 = UserBST()
    bst10.insert(1, "Alice", [2, 99])   # 99 does not exist
    bst10.insert(2, "Bob", [1, 3])
    bst10.insert(3, "Carol", [2])
    print("suggest_friends(1):", bst10.suggest_friends(1))
    print()

    # --------------------------------------------------
    # Edge Case 11: Skewed BST (increasing insertion order)
    # --------------------------------------------------
    print("--- Edge Case 11: Skewed BST (increasing insertion order) ---")
    bst11 = UserBST()
    for i in range(1, 6):
        bst11.insert(i, f"User{i}", [])
    print("inorder_traversal:", bst11.inorder_traversal())
    print("get_height:", bst11.get_height())
    print("is_balanced:", bst11.is_balanced())
    print("get_leaf_count:", bst11.get_leaf_count())
    print()

    # --------------------------------------------------
    # Edge Case 12: Balanced-looking BST
    # --------------------------------------------------
    print("--- Edge Case 12: Balanced-looking BST ---")
    bst12 = UserBST()
    bst12.insert(4, "U4", [])
    bst12.insert(2, "U2", [])
    bst12.insert(6, "U6", [])
    bst12.insert(1, "U1", [])
    bst12.insert(3, "U3", [])
    bst12.insert(5, "U5", [])
    bst12.insert(7, "U7", [])
    print("inorder_traversal:", bst12.inorder_traversal())
    print("get_height:", bst12.get_height())
    print("is_balanced:", bst12.is_balanced())
    print("get_leaf_count:", bst12.get_leaf_count())
    print()


if __name__ == "__main__":
    main()