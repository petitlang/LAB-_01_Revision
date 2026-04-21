## File Structure:

```
/LAB _07/
├── exercise1_binary_search_trees.py
├── exercise2_binary_heap.py
├── exercise3_prefix_range_trees.py
└── README.md
```

---

## Team members and assigned exercises

Team: T14

Mouzheng LI: 1 & 3
Yuefan LIU: 2 & 3

Collaborate : 3 & Final Question

---

## Dependencies and Language version

Please use **python 3.11 or higher version**.

Please use **JDK 17 or a higher version**.

---

# Brief description of each solution

## Solution of exercise1_binary_search_trees

This solution uses a Binary Search Tree (BST) to store user profiles by user_id.
Each node contains the user_id, name, friends list, and links to the left and right child.

The insert operation adds a new user into the correct position based on user_id.
The find operation searches for a user by comparing the target id with the current node and moving left or right.
The inorder traversal visits the tree in sorted order, so it returns all user_ids from small to large.

The delete operation removes a user from the BST.
It handles the three classical cases: deleting a leaf node, deleting a node with one child, and deleting a node with two children.
For the third case, it replaces the node with the minimum node from the right subtree.

The suggest_friends operation is based on the friend-of-friend idea.
It first finds the target user, then checks the friends of each direct friend.
It excludes the user and existing direct friends, counts how many times each candidate appears, and returns the top suggestions with the highest frequency.

The BST also provides simple analytics.
get_height computes the height of the tree, is_balanced checks whether the tree is balanced, and get_leaf_count counts the number of leaf nodes.

---

## Solution of exercise2_


---

## Solution of exercise3_


---

# Complexity analysis summary

## Complexity of exercise1_binary_search_trees


1. insert(user_id, name, friends_list)
Time:
- Average case: O(log n)
- Worst case: O(n)
Space:
- O(h)

2. find(user_id)
Time:
- Average case: O(log n)
- Worst case: O(n)
Space:
- O(h)

3. inorder_traversal()
Time:
- O(n)
Space:
- O(h)

4. find_min()
Time:
- O(h)
Space:
- O(1)

5. delete(user_id)
Time:
- Average case: O(log n)
- Worst case: O(n)
Space:
- O(h)

6. suggest_friends(user_id, max_suggestions)
Let F be the number of direct friends,
M be the total number of friend-of-friend checks,
and s be the number of candidate suggestions.

Time:
- Average case: O(F log n + M + s log s)
- Worst case: O(Fn + M + s log s)
Space:
- O(s)

7. get_height()
Time:
- O(n)
Space:
- O(h)

8. is_balanced()
Time:
- O(n^2) in this simple implementation
Space:
- O(h)

9. get_leaf_count()
Time:
- O(n)
Space:
- O(h)

Overall:
The BST is efficient when it stays balanced, because search, insert, and delete are usually O(log n).
But if the tree becomes skewed, these operations can degrade to O(n).
This also makes suggest_friends slower because it depends on repeated find operations.

---

## Complexity of exercise2_


---

## Complexity of exercise3_


