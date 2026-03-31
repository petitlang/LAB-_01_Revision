class CategoryNode:
    def __init__(self, category_id, category_name, post_count, left=None, right=None):
        self.category_id = category_id
        self.category_name = category_name
        self.post_count = post_count
        self.left = left
        self.right = right


# Part A

def in_order_collect(node):
    """
    Return a list of category names in in-order sequence.
    Left -> Root -> Right
    """
    result = []

    if node is None:
        return result

    result.extend(in_order_collect(node.left))
    result.append(node.category_name)
    result.extend(in_order_collect(node.right))

    return result


def in_order_accumulate_posts(node):
    """
    Process categories in in-order and return total post count.
    """
    if node is None:
        return 0

    total = 0
    total += in_order_accumulate_posts(node.left)
    total += node.post_count
    total += in_order_accumulate_posts(node.right)

    return total


def in_order_collect_nodes(node):
    """
    Helper function for in_order_find_kth.
    Return nodes in in-order sequence.
    """
    result = []

    if node is None:
        return result

    result.extend(in_order_collect_nodes(node.left))
    result.append(node)
    result.extend(in_order_collect_nodes(node.right))

    return result


def in_order_find_kth(k, node):
    """
    Find the k-th category in in-order sequence (1-indexed).
    Return the node or None if invalid.
    """
    ordered_nodes = in_order_collect_nodes(node)

    if k < 1 or k > len(ordered_nodes):
        return None

    return ordered_nodes[k - 1]


# Part B

def pre_order_export(node, level=0):
    """
    Generate a formatted tree representation with indentation.
    Root -> Left -> Right
    """
    if node is None:
        return ""

    indent = "    " * level
    result = f"{indent}{node.category_name}({node.post_count})\n"
    result += pre_order_export(node.left, level + 1)
    result += pre_order_export(node.right, level + 1)

    return result


def pre_order_copy(node):
    """
    Create a deep copy of the entire tree.
    Return the root of the copied tree.
    """
    if node is None:
        return None

    new_node = CategoryNode(
        node.category_id,
        node.category_name,
        node.post_count
    )

    new_node.left = pre_order_copy(node.left)
    new_node.right = pre_order_copy(node.right)

    return new_node


def pre_order_serialize(node):
    """
    Serialize tree into a string using pre-order traversal.
    """
    if node is None:
        return "#"

    return (
        f"{node.category_name}({node.post_count}) | "
        f"{pre_order_serialize(node.left)} | "
        f"{pre_order_serialize(node.right)}"
    )


# Part C

def post_order_total_posts(node):
    """
    Compute total posts in a category including all subcategories.
    Left -> Right -> Root
    """
    if node is None:
        return 0

    left_total = post_order_total_posts(node.left)
    right_total = post_order_total_posts(node.right)

    return left_total + right_total + node.post_count


def post_order_leaf_depth_stats(node, depth=0):
    """
    Return (depth_sum, leaf_count) for all leaf nodes.
    """
    if node is None:
        return 0, 0

    left_sum, left_count = post_order_leaf_depth_stats(node.left, depth + 1)
    right_sum, right_count = post_order_leaf_depth_stats(node.right, depth + 1)

    if node.left is None and node.right is None:
        return depth, 1

    return left_sum + right_sum, left_count + right_count


def post_order_average_depth(node):
    """
    Calculate average depth of leaf categories.
    """
    depth_sum, leaf_count = post_order_leaf_depth_stats(node, 0)

    if leaf_count == 0:
        return 0

    return depth_sum / leaf_count


def post_order_collect_leaves(node):
    """
    Collect all leaf category names in post-order.
    """
    result = []

    if node is None:
        return result

    result.extend(post_order_collect_leaves(node.left))
    result.extend(post_order_collect_leaves(node.right))

    if node.left is None and node.right is None:
        result.append(node.category_name)

    return result


# Traversal-based Analytics

def find_most_popular_category(node):
    """
    Find the category with the highest post_count.
    Only consider the category itself, not children totals.
    Return the node.
    """
    if node is None:
        return None

    best = node

    left_best = find_most_popular_category(node.left)
    right_best = find_most_popular_category(node.right)

    if left_best is not None and left_best.post_count > best.post_count:
        best = left_best

    if right_best is not None and right_best.post_count > best.post_count:
        best = right_best

    return best


def count_direct_children(node):
    """
    Count direct children of a node.
    """
    if node is None:
        return 0

    count = 0
    if node.left is not None:
        count += 1
    if node.right is not None:
        count += 1

    return count


def category_with_most_subcategories(node):
    """
    Find the category with the most direct children.
    Return the node.
    """
    if node is None:
        return None

    best = node
    best_children = count_direct_children(node)

    left_best = category_with_most_subcategories(node.left)
    right_best = category_with_most_subcategories(node.right)

    if left_best is not None and count_direct_children(left_best) > best_children:
        best = left_best
        best_children = count_direct_children(left_best)

    if right_best is not None and count_direct_children(right_best) > best_children:
        best = right_best
        best_children = count_direct_children(right_best)

    return best


# Distribution by Depth

def distribution_by_depth(node, depth=0, depth_map=None):
    """
    Count how many nodes appear at each depth.
    Example output: {0: 1, 1: 2, 2: 4}
    """
    if depth_map is None:
        depth_map = {}

    if node is None:
        return depth_map

    depth_map[depth] = depth_map.get(depth, 0) + 1

    distribution_by_depth(node.left, depth + 1, depth_map)
    distribution_by_depth(node.right, depth + 1, depth_map)

    return depth_map

# example tree for testing

def build_sample_tree():
    django = CategoryNode(1, "Django", 18)
    flask = CategoryNode(2, "Flask", 12)
    java = CategoryNode(3, "Java", 30)
    uiux = CategoryNode(4, "UI/UX", 38)
    graphics = CategoryNode(5, "Graphics", 22)

    python = CategoryNode(6, "Python", 42, django, flask)
    programming = CategoryNode(7, "Programming", 85, python, java)
    design = CategoryNode(8, "Design", 65, uiux, graphics)
    technology = CategoryNode(9, "Technology", 150, programming, design)

    return technology


if __name__ == "__main__":
    print("===== Test Set for Edge Cases =====")


    # Edge Case 1: Empty tree

    print("\n--- Edge Case 1: Empty tree ---")
    root = None

    print("in_order_collect:", in_order_collect(root))                 # []
    print("in_order_accumulate_posts:", in_order_accumulate_posts(root))   # 0
    print("in_order_find_kth(1):", in_order_find_kth(1, root))       # None
    print("pre_order_export:\n", pre_order_export(root), sep="")     # ""
    print("pre_order_serialize:", pre_order_serialize(root))         # "#"
    print("pre_order_copy:", pre_order_copy(root))                   # None
    print("post_order_total_posts:", post_order_total_posts(root))   # 0
    print("post_order_average_depth:", post_order_average_depth(root))   # 0
    print("post_order_collect_leaves:", post_order_collect_leaves(root)) # []
    print("find_most_popular_category:", find_most_popular_category(root)) # None
    print("category_with_most_subcategories:", category_with_most_subcategories(root)) # None
    print("distribution_by_depth:", distribution_by_depth(root))     # {}


    # Edge Case 2: Single node tree

    print("\n--- Edge Case 2: Single node tree ---")
    root = CategoryNode(1, "Technology", 150)

    print("in_order_collect:", in_order_collect(root))               # ['Technology']
    print("in_order_accumulate_posts:", in_order_accumulate_posts(root)) # 150

    kth = in_order_find_kth(1, root)
    print("in_order_find_kth(1):", kth.category_name if kth else None)   # Technology

    print("pre_order_export:\n", pre_order_export(root), sep="")
    print("pre_order_serialize:", pre_order_serialize(root))

    copied = pre_order_copy(root)
    print("pre_order_copy root:", copied.category_name if copied else None)

    print("post_order_total_posts:", post_order_total_posts(root))   # 150
    print("post_order_average_depth:", post_order_average_depth(root))   # 0.0 or 0
    print("post_order_collect_leaves:", post_order_collect_leaves(root)) # ['Technology']

    popular = find_most_popular_category(root)
    print("find_most_popular_category:", popular.category_name if popular else None)

    most_children = category_with_most_subcategories(root)
    print("category_with_most_subcategories:", most_children.category_name if most_children else None)

    print("distribution_by_depth:", distribution_by_depth(root))     # {0: 1}


    # Edge Case 3: Left-skewed tree

    print("\n--- Edge Case 3: Left-skewed tree ---")
    root = CategoryNode(1, "A", 10,
            CategoryNode(2, "B", 20,
                CategoryNode(3, "C", 30,
                    CategoryNode(4, "D", 40))))

    print("in_order_collect:", in_order_collect(root))               # ['D', 'C', 'B', 'A']
    print("in_order_accumulate_posts:", in_order_accumulate_posts(root)) # 100
    print("post_order_total_posts:", post_order_total_posts(root))   # 100
    print("post_order_average_depth:", post_order_average_depth(root))   # 3.0
    print("post_order_collect_leaves:", post_order_collect_leaves(root)) # ['D']
    print("distribution_by_depth:", distribution_by_depth(root))     # {0:1,1:1,2:1,3:1}


    # Edge Case 4: Right-skewed tree

    print("\n--- Edge Case 4: Right-skewed tree ---")
    root = CategoryNode(1, "A", 10, None,
            CategoryNode(2, "B", 20, None,
                CategoryNode(3, "C", 30, None,
                    CategoryNode(4, "D", 40))))

    print("in_order_collect:", in_order_collect(root))               # ['A', 'B', 'C', 'D']
    print("in_order_accumulate_posts:", in_order_accumulate_posts(root)) # 100
    print("post_order_total_posts:", post_order_total_posts(root))   # 100
    print("post_order_average_depth:", post_order_average_depth(root))   # 3.0
    print("post_order_collect_leaves:", post_order_collect_leaves(root)) # ['D']
    print("distribution_by_depth:", distribution_by_depth(root))     # {0:1,1:1,2:1,3:1}


    # Edge Case 5: Invalid k in in_order_find_kth

    print("\n--- Edge Case 5: Invalid k ---")
    root = CategoryNode(1, "B", 20,
            CategoryNode(2, "A", 10),
            CategoryNode(3, "C", 30))

    print("in_order_collect:", in_order_collect(root))               # ['A', 'B', 'C']

    kth = in_order_find_kth(0, root)
    print("in_order_find_kth(0):", kth.category_name if kth else None)   # None

    kth = in_order_find_kth(4, root)
    print("in_order_find_kth(4):", kth.category_name if kth else None)   # None


    # Edge Case 6: Equal post counts

    print("\n--- Edge Case 6: Equal post counts ---")
    root = CategoryNode(1, "Root", 50,
            CategoryNode(2, "Left", 50),
            CategoryNode(3, "Right", 50))

    popular = find_most_popular_category(root)
    print("find_most_popular_category:", popular.category_name if popular else None)
    # Usually returns the first best node encountered, here likely "Root"


    # Edge Case 7: Full balanced tree

    print("\n--- Edge Case 7: Balanced tree ---")
    root = build_sample_tree()

    print("in_order_collect:", in_order_collect(root))
    print("in_order_accumulate_posts:", in_order_accumulate_posts(root))
    print("post_order_total_posts:", post_order_total_posts(root))
    print("post_order_average_depth:", post_order_average_depth(root))
    print("post_order_collect_leaves:", post_order_collect_leaves(root))

    popular = find_most_popular_category(root)
    print("find_most_popular_category:", f"{popular.category_name} ({popular.post_count})" if popular else None)

    most_children = category_with_most_subcategories(root)
    print("category_with_most_subcategories:",
          f"{most_children.category_name} ({count_direct_children(most_children)} children)" if most_children else None)

    print("distribution_by_depth:", distribution_by_depth(root))