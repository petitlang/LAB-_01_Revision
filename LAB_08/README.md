## File Structure:

```
/LAB _08/
├── exercise1_binary_search_trees.py
├── exercise2_binary_heap.py
├── exercise3_A_Trie for Autocomplete.py
├── exercise3_B_Segment Tree,py
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

## Solution of exercise2_binary_heap

This solution uses a Binary Heap to maintain trending posts in a social network.
The heap is implemented as a max-heap, so the post with the highest number of likes is always stored at the root.

Each heap element is a Post containing the number of likes, the post_id, and a timestamp.
The push operation inserts a new post at the end of the heap and then restores the heap order by moving it upward.
The pop_max operation removes the root, replaces it with the last element, and restores the heap order by moving it downward.

The peek_max operation returns the root without removing it.
The get_top_k operation returns the k most liked posts by using a copy of the heap, so the original heap is not modified.
The update_likes operation finds a post by post_id, updates its number of likes, and then reheapifies the structure by moving the updated post upward or downward depending on the new value.

The heap also provides simple analytics.
size returns the number of posts, is_valid_heap checks whether the max-heap property is satisfied, get_height returns the heap height, and get_level_order returns the heap as level-order traversal.

The simulate_trending_feed procedure initializes the heap with 100 posts, performs 10,000 like updates, and displays the top 5 posts every 1,000 updates.
This models the behavior of a real-time trending feed in a social network.

---

## Solution of exercise3_prefix_range_trees

### Part A – Trie for Autocomplete

This part uses a Trie to store usernames and support fast autocomplete queries.
Each Trie node contains a dictionary of children, a boolean field indicating whether the node is the end of a username, and the corresponding user_id.

The insert operation adds a username character by character into the Trie.
The search operation checks whether a complete username exists and returns its user_id if found.
The starts_with operation checks whether at least one stored username begins with a given prefix.

The autocomplete operation first follows the prefix in the Trie.
If the prefix exists, it explores the subtree below that prefix node and collects usernames until reaching the maximum number of results.
This makes the Trie suitable for search-as-you-type systems.

The Trie also provides simple analytics.
count_words returns the total number of stored usernames, get_height returns the length of the longest stored username, and get_total_nodes counts the total number of Trie nodes.
The delete operation removes a username and also removes unnecessary nodes that are no longer used by any other username.

Overall, the Trie is efficient for prefix-based search and autocomplete, which is difficult to achieve directly with a simple hash map.

### Part B – Segment Tree for Activity Range Queries

This part uses a Segment Tree to process activity values over time.
The structure stores an activity array, where each value represents the number of posts for one day.
Each segment tree node stores the interval boundaries together with the sum, maximum value, and minimum value of that interval.

The build operation constructs the segment tree from the initial activity array by recursively dividing the range into two halves.
The query operation returns the total number of posts between two days.
The get_range_max operation returns the maximum activity value in a day interval, and get_range_min returns the minimum activity value in the interval.

The segment tree also provides simple analytics.
get_tree_size returns the number of nodes in the structure, get_height returns the tree height, and get_leaf_values returns the original activity array.

The simulate_activity procedure generates 30 days of activity values and computes the 7-day rolling totals for the last week.
This shows how the segment tree can be used for social network activity monitoring and range analysis.

Overall, the Segment Tree is well adapted for range queries because it can answer them efficiently without scanning the whole array every time.

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

1. push(post_id, likes, timestamp)
Time:O(log n)
Space:O(1)
2. pop_max()
Time:O(log n)
Space:O(1)
3. peek_max()
Time:O(1)
Space:O(1)
4. get_top_k(k)
Time:O(k log n)
Space:O(n)
5. update_likes(post_id, new_likes, timestamp)
Time:O(n) in this simple implementation
Space:O(1)
6. size()
Time:O(1)
Space:O(1)
7. is_valid_heap()
Time:O(n)
Space:O(1)
8. get_height()
Time:O(1)
Space:O(1)
9. get_level_order()
Time:O(n)
Space:O(n)
10. simulate_trending_feed()
Time:Dominated by repeated updates and queries
Space:O(n)

Overall:
- The max-heap is efficient for maintaining trending posts because the most liked post is always at the root.
Insertion and deletion of the maximum value both take O(log n), while reading the maximum takes O(1).
It is more efficient than sorting all posts every time, especially when only the top few results are required.

---

## Complexity of exercise3_prefix_range_trees

### Part A – Trie for Autocomplete

1. insert(username, user_id)
Let m be the length of the username.
Time:O(m)
Space:O(m) in the worst case
2. search(username)
Time:O(m)
Space:O(1)
3. starts_with(prefix)
Time:O(m)
Space:O(1)
4. autocomplete(prefix, max_results)
Let p be the prefix length and k the number of returned results.
Time:O(p + k)
Space:O(k + h)
5. delete(username)
Time:O(m)
Space:O(m) in the recursive version
6. count_words()
Time:O(n)
Space:O(h)
7. get_height()
Time:O(n)
Space:O(h)
8. get_total_nodes()
Time:O(n)
Space:O(h)

Overall for Part A:
- The Trie is efficient for exact search and especially for prefix search.
Unlike a hash map, it naturally supports autocomplete and search-as-you-type operations.
Its main cost is memory usage, because many nodes may be created when many usernames are stored.

### Part B – Segment Tree for Activity Range Queries

1. build(activity_array)
Time:O(n)
Space:O(n)
query(l, r)
2. Time:O(log n)
Space:O(log n)
3. get_range_max(l, r)
Time:O(log n)
Space:O(log n)
4. get_range_min(l, r)
Time:O(log n)
Space:O(log n)
5. get_tree_size()
Time:O(1)
Space:O(1)
6. get_height()
Time:O(1)
Space:O(1)
7. get_leaf_values()
Time:O(n)
Space:O(n)
8. simulate_activity()
Time:O(n) for building + O(log n) per query
Space:O(n)

Overall for Part B:
- The Segment Tree is efficient for range queries because it avoids scanning the entire array for each request.
Compared with a prefix sum array, it is better when updates or different range queries happen frequently.
It is therefore well suited for activity monitoring over time.