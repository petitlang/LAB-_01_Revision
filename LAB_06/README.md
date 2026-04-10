## File Structure:
~~~
/LAB _05/
├── exercise1_
├── exercise2_
├── exercise3_
└── README.md
~~~

---

## Team members and assigned exercises
Team: T14

Mouzheng LI: 2 & 1  
Yuefan LIU: 3 & 1  

Collaborate : 1 & Final Question  

---

## Dependencies and Language version
Please use **python 3.11 or higher version**.  

Please use **JDK 17 or a higher version**.  

---

# Brief description of each solution

## Solution of exercise1_Social Graph.py

This solution implements a social network using graph data structures.

We represent the graph using:
- Adjacency List (dictionary of users)
- Adjacency Matrix (2D array)

Main functionalities include:
- Add and remove users and friendships
- Check if two users are friends
- Compute degree of a user
- Compute number of users and edges
- Check if the graph is complete
- Compute graph density
- Convert between matrix and list representations

The adjacency list is used for efficient storage, while the matrix allows fast edge lookup.

---

## Solution of exercise2_DFS_social_network_analysis.py

This solution implements DFS-based algorithms for social network analysis.

We represent the graph using an adjacency list (dictionary of nodes and neighbors).

Main functionalities include:

- DFS traversal (recursive and iterative)
- Find connected components
- Check if the graph is connected
- Check if a path exists between two users
- Find a path between two users
- Compute sizes of connected components
- Find the largest component
- Detect isolated users

DFS is used because it explores all nodes in depth and is suitable for:
- exploring components
- connectivity checking
- path existence

Both recursive and iterative DFS are implemented.
The iterative version avoids recursion depth problems.

---

## Solution of exercise3_BFS for Shortest Path Analysis.py

This solution implements BFS-based algorithms for analyzing social networks.

Part A:
We use BFS to traverse the graph and return the visiting order.

Part B:
We extend BFS to compute the shortest distance from a starting user to all other users.

Part C:
We compute the shortest path between two users using BFS and parent tracking.

Part D:
We compute the degrees of separation, which is the length of the shortest path.

Part E:
We find all users reachable within k hops from a starting user.

BFS is used because it guarantees the shortest path in an unweighted graph and explores nodes level by level.

---

# Complexity analysis summary

## Complexity of exercise1_Social Graph.py

Adjacency Matrix:
- Time complexity (are_friends): O(1)
- Space complexity: O(V²)

Adjacency List:
- Time complexity (are_friends): O(deg(u))
- Space complexity: O(V + E)

Conclusion:
Adjacency list is more space-efficient and suitable for large social networks.

---

## Complexity of exercise2_DFS_social_network_analysis.py

DFS (Adjacency List):
- Time complexity: O(V + E)
- Space complexity: O(V)

Explanation:
DFS visits each node once and explores each edge once.

Recursive DFS:
- May cause stack overflow for very large graphs

Iterative DFS:
- Uses explicit stack
- Avoids recursion problem

Conclusion:
DFS is efficient for connectivity and component analysis.

---

## Complexity of exercise3_BFS for Shortest Path Analysis.py

BFS:
- Time complexity: O(V + E)
- Space complexity: O(V)

Applications:
- Shortest path (optimal in unweighted graph)
- Degrees of separation
- k-hop neighbors

Conclusion:
BFS is the best choice for distance and shortest path problems.