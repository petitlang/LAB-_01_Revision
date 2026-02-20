## File Structure:
~~~
/LAB _02/
├── exercise1_
├── exercise2_mutual_friends.py
├── exercise3_find_recommendation.py
├── exercise4_mutual_followers.py
└── README.md (Team members and assigned exercises, Brief description of each solution, Complexity analysis summary)
~~~

---

## Team members and assigned exercises
Team: T14

Yuefan LIU: 1

Mouzheng LI: 2

Xinyue LI: 3

Collaborate : 4 & Final Question

---

## Dependencies and Language version
Please use **python 3.11 or higher version**

---

##  Brief description of each solution

### Solution of exercise2_mutual_friends

This project implements basic set operations including intersection, difference, and union using Python sets.
The intersection and difference functions iterate through one set and perform constant-time membership checks in the other set.
The union function constructs a new set containing all unique elements from both input sets to avoid modifying the original data.
Based on these operations, the mutual friend coefficient is computed using the Jaccard similarity, defined as the ratio between the size of the intersection and the size of the union.
Special edge cases, such as empty sets and unbalanced set sizes, are handled to ensure correctness and robustness.

---

## Complexity analysis summary

### Complexity of exercise2_mutual_friends

For the mutual friends detection problem, the algorithm represents each user’s friend list as a hash-based set.
The **intersection and difference** operations iterate over one set and perform constant-time membership checks in the other set, resulting in a **time complexity of O(min(m, n)) on average**, where m and n are the sizes of the two friend sets.
The **union** operation iterates over both sets once, leading to a **time complexity of O(m + n)**.

The **mutual friend coefficient (Jaccard similarity)** is computed using the sizes of the intersection and union, and therefore has the same overall time complexity.
In terms of space complexity, all operations require **additional space proportional to the size of the result sets**, leading to **a space complexity of O(m + n)** in the worst case.