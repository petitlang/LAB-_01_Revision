## File Structure:
~~~
/LAB _02/
├── exercise1_message_analysis.java
├── exercise2_mutual_friends.py
├── exercise3_find_recommendation.py
├── exercise4_mutual_followers.py
└── README.md (Team members and assigned exercises, Brief description of each solution, Complexity analysis summary)
~~~

---

## Team members and assigned exercises
Team: T14

Mouzheng LI: 1

Yuefan LIU: 2

Xinyue LI: 3

Collaborate : 4 & Final Question

---

## Dependencies and Language version
Please use **python 3.11 or higher version**.

Please use **JDK 17 or a higher version**.

---

#  Brief description of each solution

## Solution of exercise1_recursive_comment_thread_traversal

**display_thread**

This function recursively prints a comment and all of its replies. The `level` parameter controls the indentation so that nested replies appear visually structured. For each comment, the function prints the comment information and then recursively calls itself for every reply in the `replies` list.


**count_total_comments**

This function recursively counts the total number of comments in a thread. It starts with a count of one for the current comment and then adds the number of comments from each reply by calling the same function recursively. This ensures that all nested comments are included.


**total_likes**

This function recursively computes the total number of likes in a comment thread. It begins with the likes of the current comment and then adds the likes from all replies by recursively processing each child comment.


**find_deepest_reply**

This function recursively finds the maximum nesting depth of the comment thread. For each reply, it calculates the depth of its subtree and keeps track of the largest depth encountered. The final result is the maximum depth plus one for the current comment level.


**search_by_user**

This function recursively searches the entire comment thread for comments written by a specific user. If the current comment belongs to the target user, it is added to the result list. The function then continues searching through all replies and combines the results.


**contains_keyword**

This function recursively checks whether any comment in the thread contains a given keyword. It first checks the content of the current comment. If the keyword is not found, the function continues searching through all replies and returns true as soon as a match is found.


**delete_comment**

This function recursively deletes a comment from the thread and performs cascade deletion on all of its replies. If the current comment matches the target `comment_id`, the function returns null to remove that node. Otherwise, it processes all replies and rebuilds the replies list without the deleted subtree.

---

## Solution of exercise2_


_
## Solution of exercise3_



---

# Complexity analysis summary

## Complexity of exercise1_recursive_comment_thread_traversal


**display_thread**

- **Time Complexity:** O(n)  
  Each comment in the thread is visited exactly once during the traversal.

- **Space Complexity:** O(d)  
  The recursion stack depends on the maximum depth `d` of the comment thread.


**count_total_comments**

- **Time Complexity:** O(n)  
  The function recursively visits every comment once to count them.

- **Space Complexity:** O(d)  
  The recursion stack grows according to the maximum nesting depth of the thread.


**total_likes**

- **Time Complexity:** O(n)  
  Each comment is processed once to sum all likes.

- **Space Complexity:** O(d)  
  Memory usage depends on the recursion depth of the thread.


**find_deepest_reply**

- **Time Complexity:** O(n)  
  The function must visit every comment to determine the maximum depth.

- **Space Complexity:** O(d)  
  The recursion stack stores calls up to the deepest nesting level.


**search_by_user**

- **Time Complexity:** O(n)  
  Every comment is checked to see whether the user ID matches.

- **Space Complexity:** O(d + k)  
  `d` is the recursion depth and `k` is the number of comments returned in the result list.


**contains_keyword**

- **Time Complexity:** O(n)  
  In the worst case, the algorithm checks all comments in the thread.

- **Space Complexity:** O(d)  
  The recursion stack depends on the maximum nesting depth.


**delete_comment**

- **Time Complexity:** O(n)  
  The algorithm may need to traverse the entire thread to find and remove the target comment.

- **Space Complexity:** O(d)  
  The recursion depth corresponds to the maximum nesting level of the thread.

---

## Complexity of exercise2_



---

## Complexity of exercise3_


