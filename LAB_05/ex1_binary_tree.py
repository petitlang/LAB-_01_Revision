from collections import deque


class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"CategoryNode(id={self.category_id}, name='{self.name}')"


# helper functions
def set_left(parent, child):
    parent.left = child
    if child is not None:
        child.parent = parent


def set_right(parent, child):
    parent.right = child
    if child is not None:
        child.parent = parent


def print_path(path):
    if not path:
        print("Empty path")
        return
    print(" -> ".join(node.name for node in path))


# Algorithm 1: calculate_height
def calculate_height(node):
    if node is None:
        return -1

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    if left_height > right_height:
        return 1 + left_height
    else:
        return 1 + right_height


# Algorithm 2: count_nodes
def count_nodes(node):
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Algorithm 3: count_leaves
def count_leaves(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return count_leaves(node.left) + count_leaves(node.right)


# Algorithm 4: is_balanced
def is_balanced(node):
    if node is None:
        return True

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    diff = left_height - right_height
    if diff < 0:
        diff = -diff

    if diff > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


# Algorithm 5: find_category
def find_category(target_id, node):
    if node is None:
        return None

    if node.category_id == target_id:
        return node

    result = find_category(target_id, node.left)

    if result is not None:
        return result

    return find_category(target_id, node.right)


# Algorithm 6: find_path_to_root
def find_path_to_root(target_id, root):
    target = find_category(target_id, root)

    if target is None:
        return []

    path = []

    while target is not None:
        path.append(target)
        target = target.parent

    return path


# Algorithm 7: lowest_common_ancestor
def lowest_common_ancestor(id1, id2, root):
    path1 = find_path_to_root(id1, root)
    path2 = find_path_to_root(id2, root)

    if not path1 or not path2:
        return None

    for node1 in path1:
        for node2 in path2:
            if node1.category_id == node2.category_id:
                return node1

    return None


# Algorithm 8: calculate_node_height
def calculate_node_height(target_id, root):
    target = find_category(target_id, root)

    if target is None:
        return -1

    height = 0

    while target.parent is not None:
        height += 1
        target = target.parent

    return height


# Algorithm 9: is_full_binary_tree
def is_full_binary_tree(node):
    if node is None:
        return True

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    diff = left_height - right_height
    if diff < 0:
        diff = -diff

    if diff > 1:
        return False

    if node.left is None and node.right is None:
        return True

    if node.left is None or node.right is None:
        return False

    return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)


# Algorithm 10: is_perfect_binary_tree
def is_perfect_binary_tree(root):
    if root is None:
        return True

    q = deque([root])
    found_missing_child = False

    while q:
        current = q.popleft()

        if current.left is not None:
            if found_missing_child:
                return False
            q.append(current.left)
        else:
            found_missing_child = True

        if current.right is not None:
            if found_missing_child:
                return False
            q.append(current.right)
        else:
            found_missing_child = True

    return True


# Algorithm 11: is_complete_binary_tree
def is_complete_binary_tree(root):
    if root is None:
        return True

    q = deque([root])
    current_level = 0

    while q:
        level_size = len(q)

        if level_size != 2 ** current_level:
            return False

        for _ in range(level_size):
            current = q.popleft()

            if current.left is None or current.right is None:
                if current.left is not None or current.right is not None:
                    return False
            else:
                q.append(current.left)
                q.append(current.right)

        current_level += 1

    return True


def main():
    # Test Case 1: Empty tree
    print("Test Case 1: Empty tree")
    empty_root = None

    print("Tree height:", calculate_height(empty_root))
    print("Total nodes:", count_nodes(empty_root))
    print("Leaf nodes:", count_leaves(empty_root))
    print("Is balanced:", is_balanced(empty_root))
    print("Find category id 1:", find_category(1, empty_root))
    print()

    # Test Case 2: Single node tree
    print("Test Case 2: Single node tree")
    single_root = CategoryNode(1, "Technology", 100)

    print("Tree height:", calculate_height(single_root))
    print("Total nodes:", count_nodes(single_root))
    print("Leaf nodes:", count_leaves(single_root))
    print("Is balanced:", is_balanced(single_root))
    print("Node height of Technology from root:", calculate_node_height(1, single_root))
    print()

    # Test Case 3: Normal category tree
    print("Test Case 3: Normal category tree")

    technology = CategoryNode(1, "Technology", 100)
    programming = CategoryNode(2, "Programming", 80)
    gadgets = CategoryNode(3, "Gadgets", 60)
    java = CategoryNode(4, "Java", 40)
    python = CategoryNode(5, "Python", 50)
    smartphones = CategoryNode(6, "Smartphones", 30)
    laptops = CategoryNode(7, "Laptops", 20)

    set_left(technology, programming)
    set_right(technology, gadgets)

    set_left(programming, java)
    set_right(programming, python)

    set_left(gadgets, smartphones)
    set_right(gadgets, laptops)

    root = technology

    print("Tree height:", calculate_height(root))
    print("Total nodes:", count_nodes(root))
    print("Leaf nodes:", count_leaves(root))
    print("Is balanced:", is_balanced(root))

    found = find_category(5, root)
    print("Find category id 5:", found)

    path = find_path_to_root(5, root)
    print("Path from Python to root:", end=" ")
    print_path(path)

    lca = lowest_common_ancestor(4, 5, root)
    print("LCA of Java and Python:", lca)

    print("Node height of Python from root:", calculate_node_height(5, root))
    print("Is full binary tree:", is_full_binary_tree(root))
    print("Is perfect binary tree:", is_perfect_binary_tree(root))
    print("Is complete binary tree:", is_complete_binary_tree(root))
    print()

    # Test Case 4: Unbalanced tree
    print("Test Case 4: Unbalanced tree")

    a = CategoryNode(10, "Technology", 100)
    b = CategoryNode(11, "Programming", 80)
    c = CategoryNode(12, "Java", 40)

    set_left(a, b)
    set_left(b, c)

    unbalanced_root = a

    print("Tree height:", calculate_height(unbalanced_root))
    print("Total nodes:", count_nodes(unbalanced_root))
    print("Leaf nodes:", count_leaves(unbalanced_root))
    print("Is balanced:", is_balanced(unbalanced_root))
    print("Is full binary tree:", is_full_binary_tree(unbalanced_root))


if __name__ == "__main__":
    main()