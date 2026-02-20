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
_
### Solution of exercise3_find_recommendation
This project implements a recommendation system based on user similarity and collaborative filtering.
The algorithm first calculates pairwise similarity between users using cosine similarity, then selects the top K users with the highest similarity (excluding existing friends).
Based on these similar users, the system recommends new interests by averaging these users' preferences for interests that the target user has not yet rated.

### Solution of exercise4_mutual_followers

#### Follow / Unfollow
These solutions update the adjacency matrix to represent a follow or unfollow action.
Setting matrix[follower][followee] to True indicates a follow relationship, while setting it to False removes it.
Both operations run in constant time.

#### Is_following
This solution checks whether a directed follow relationship exists between two users by directly accessing the adjacency matrix.
It returns a boolean value and runs in constant time.

#### Get_followers
This solution retrieves all users who follow a given user by scanning the corresponding column in the adjacency matrix.
Each row is checked to determine whether a follow relationship exists.

#### Get_following
This solution retrieves all users that a given user follows by scanning the corresponding row in the adjacency matrix.
Each column entry is checked for an existing follow relationship.

#### Mutual_follows
This solution detects mutual follow relationships by examining pairs of users and checking whether both directed edges exist between them.
Only unique pairs are returned to avoid duplicates.

#### Influence_score
This solution computes a user’s influence score as the sum of their followers and followings divided by the total number of users.
It reflects both popularity and activity within the network.

---

## Complexity analysis summary

### Complexity of exercise2_mutual_friends

For the mutual friends detection problem, the algorithm represents each user’s friend list as a hash-based set.
The **intersection and difference** operations iterate over one set and perform constant-time membership checks in the other set, resulting in a **time complexity of O(min(m, n)) on average**, where m and n are the sizes of the two friend sets.
The **union** operation iterates over both sets once, leading to a **time complexity of O(m + n)**.

The **mutual friend coefficient (Jaccard similarity)** is computed using the sizes of the intersection and union, and therefore has the same overall time complexity.
In terms of space complexity, all operations require **additional space proportional to the size of the result sets**, leading to **a space complexity of O(m + n)** in the worst case.

### Complexity of exercise3_find_recommendation
The time complexity of cosine similarity calculation is O(U × I).
Selecting the K most similar users has a time complexity of O(U log U).
The filtering step iterates through all interests and the selected K users, with a time complexity of O(K × I).
Each similarity calculation iterates through all interest dimensions, resulting in an overall time complexity of O(U² × I).


### Complexity of exercise4_mutual_followers

The social network is represented using an adjacency matrix of size **N × N**, where *N* is the number of users.
The **Follow**, **Unfollow**, and **Is_following** operations access a single matrix cell and therefore run in **O(1)** time.

The **Get_followers** and **Get_following** functions scan an entire column or row of the matrix, resulting in a **time complexity of O(N)** for each call.
The **Mutual_follows** detection checks all unique user pairs, leading to a **time complexity of O(N²)** in the worst case.

The **Influence_score** computation scans both one row and one column of the matrix and therefore runs in **O(N)** time.
In terms of space complexity, the adjacency matrix requires **O(N²)** space, which limits the scalability of this approach to small or medium-sized networks.
