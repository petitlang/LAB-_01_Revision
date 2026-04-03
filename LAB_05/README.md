## File Structure:
~~~
/LAB _05/
├── exercise1_
├── exercise2_tree_traversals.py
├── exercise3_Generalized_Trees_and_Representations.py
└── README.md (Team members and assigned exercises, Brief description of each solution, Complexity analysis summary)
~~~

---

## Team members and assigned exercises
Team: T14

Mouzheng LI: 2

Yuefan LIU: 1

Xinyue LI: 3

Collaborate : 4 & Final Question

---

## Dependencies and Language version
Please use **python 3.11 or higher version**.

Please use **JDK 17 or a higher version**.

---

#  Brief description of each solution

## Solution of exercise1_



---

## Solution of exercise2__tree_traversals

This solution implements a set of tree traversal algorithms on a binary tree structure representing categories.

First, in-order traversal is used to collect category names in sorted order and to accumulate post counts. It is also used to find the k-th category by first generating an ordered list.

Second, pre-order traversal is applied to export the tree structure, create a deep copy of the tree, and serialize it into a string format. This traversal processes the parent node before its children, which is suitable for preserving hierarchy.

Third, post-order traversal is used for aggregation tasks, such as computing the total number of posts, calculating the average depth of leaf nodes, and collecting all leaf categories. Since post-order processes children before the parent, it is appropriate for combining results from subtrees.

Additional analytics functions are implemented to identify the most popular category based on post count and the category with the most direct subcategories. Another function computes the distribution of nodes by depth.

Overall, the solution demonstrates how different traversal strategies can be used depending on whether the task requires structural processing or aggregation of data.

_
## Solution of exercise3_Generalized_Trees_and_Representations

This project implements a generalized tree (N-ary tree) structure and its operations, including conversions, traversals, and metrics computation.
Two conversion methods are implemented. The conversion from a binary tree to a generalized tree interprets the left pointer of the binary tree as the first child node and the right pointer as the next sibling node. The conversion from a generalized tree to a binary tree uses the "first child node / next sibling node" representation, where the left pointer points to the first child node and the right pointer points to the next sibling node. This ensures that both representations maintain the same hierarchical relationship.

Multiple traversal algorithms are provided, including preorder traversal, postorder traversal, and level-order traversal (breadth-first search). Furthermore, the implementation calculates key tree metrics such as tree height, total number of nodes, number of leaf nodes, maximum fan-out degree, and average branch factor.

The implementation also handles special cases such as empty trees, single-node trees, deep (chain-like) structures, and wide or unbalanced trees, ensuring correctness and robustness in different scenarios.



---

# Complexity analysis summary

## Complexity of exercise1_



---

## Complexity of exercise2_tree_traversals

1. in_order_collect(node)
Time: O(n), since each node is visited once.
Space: O(h) for recursion + O(n) for the result list.

2. in_order_accumulate_posts(node)
Time: O(n), each node is processed once.
Space: O(h) due to recursion.

3. in_order_find_kth(k, node)
Time: O(n), because it first performs a full in-order traversal.
Space: O(n) for storing nodes + O(h) recursion.

4. pre_order_export(node)
Time: O(n), each node is visited once.
Space: O(h) recursion + O(n) for the output string.

5. pre_order_copy(node)
Time: O(n), each node is copied once.
Space: O(h) recursion + O(n) for the new tree.

6. pre_order_serialize(node)
Time: O(n), each node contributes once to the string.
Space: O(h) recursion + O(n) for the serialized output.

7. post_order_total_posts(node)
Time: O(n), all nodes are visited once.
Space: O(h) due to recursion.

8. post_order_average_depth(node)
Time: O(n), each node is visited once to compute leaf statistics.
Space: O(h) due to recursion.

9. post_order_collect_leaves(node)
Time: O(n), all nodes are visited once.
Space: O(h) recursion + O(l) for storing leaf nodes, where l ≤ n.

10. find_most_popular_category(node)
Time: O(n), each node is checked once.
Space: O(h) recursion.

11. category_with_most_subcategories(node)
Time: O(n), each node is visited once.
Space: O(h) recursion.

12. distribution_by_depth(node)
Time: O(n), each node is visited once.
Space: O(h) recursion + O(n) for the depth map.

Overall, all algorithms have linear time complexity O(n), with space complexity depending on tree height and whether additional storage is required.






---

## Complexity of exercise3_Generalized_Trees_and_Representations
All traversal algorithms (pre-order, post-order, and level-order) visit each node exactly once, so their time complexity is O(n), where n is the number of nodes. The space complexity is O(h) for recursive traversals and O(w) for level-order traversal.

The conversion between binary and generalized trees also processes each node once, resulting in a time complexity of O(n). The space complexity is O(n) due to the creation of new nodes in the target representation.

For tree metrics, each function performs a full traversal of the tree, leading to a time complexity of O(n) and a space complexity of O(h).





