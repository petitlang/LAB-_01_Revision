## File Structure:

```
/LAB _09/
├── exercise1_influencer_coverage.py
├── exercise2_
├── exercise3_
├── final_question.py

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

## Solution of exercise1_influencer_coverage


1. is_valid_coverage(selected_users, graph)

This function checks whether a given set of selected users can cover the whole graph.
A user is considered covered if:

- the user is selected, or
- the user is directly connected to at least one selected user

The algorithm first puts every selected user into a covered set.
Then it also adds all neighbors of each selected user.
At the end, it checks whether every node in the graph is inside the covered set.
If yes, it returns True. Otherwise, it returns False.

2. find_minimum_coverage(graph)

This function finds the exact minimum dominating set.
It tries all possible subsets of users, starting from the smallest size.
For each subset, it calls is_valid_coverage(...) to test whether that subset covers the whole graph.
The first valid subset found is the optimal solution, because subsets are checked from small to large.

This method gives the correct minimum answer, but it is only practical for small graphs because the number of subsets grows very quickly.

3. find_fast_coverage(graph)

This function finds an approximate solution using a greedy strategy.
Instead of trying all subsets, it repeatedly chooses the user that can cover the largest number of still-uncovered users.
After choosing that user, all users covered by it are removed from the uncovered set.
This process continues until all users are covered.

This method is much faster than brute force, especially for large graphs.
However, it does not always give the exact minimum solution.

4. compare_coverage(graph)

This function compares the exact solution and the greedy solution on the same graph.
It runs find_minimum_coverage(graph) and find_fast_coverage(graph), then prints:

- the size of each solution
- the selected users
- whether the greedy result matches the exact optimum

The purpose of this function is to show the difference between an exact algorithm and an approximate algorithm.
It is useful for small graphs where the exact answer can still be computed.

5. Test Set for Edge Cases in main()

The main() function is used to test the algorithms on special cases.
These edge cases help check whether the program works correctly in unusual or simple situations.

The test cases include:

- empty graph
- single node graph
- disconnected graph
- fully connected graph
- line graph
- star graph
- graph with several disconnected components
- graph used to compare exact and greedy solutions

For each case, the program prints:

- the graph
- the expected result
- the real result

This makes it easy to verify whether the functions behave correctly.

---



## Solution of exercise2_



---



## Solution of exercise3_



---

# Solution of Final Question


---



# Complexity analysis summary

## Complexity of exercise1_influencer_coverage


1. is_valid_coverage(selected_users, graph)

Time Complexity
 O(N + E)

Reason:
 The algorithm visits all selected users and their neighbors to mark covered nodes.
 After that, it scans all nodes once to check whether every user is covered.

Space Complexity
 O(N)

Reason:
 It uses a covered set that may store up to all nodes in the graph.

2. find_minimum_coverage(graph)

Time Complexity
 Worst case: O(2^N * (N + E))

Reason:
 The algorithm tries all possible subsets of users.
 For each subset, it calls is_valid_coverage(...), which costs O(N + E).
 Since the number of subsets is 2^N, the total worst-case complexity is exponential.

Space Complexity
 O(N)

Reason:
 It stores the current subset and some temporary data.
 The extra memory used is linear in the number of nodes, not counting the input graph.

3. find_fast_coverage(graph)

Time Complexity
 O(N * (N + E))

Reason:
 In the simple greedy version, the algorithm repeatedly checks all users to find the one that covers the most uncovered nodes.
 For each round, it may scan many nodes and edges again.
 This gives a polynomial running time.

Space Complexity
 O(N)

Reason:
 It uses an uncovered set, a selected_users list, and temporary cover sets.
 All of them are at most proportional to the number of nodes.

4. compare_coverage(graph)

Time Complexity
 O(2^N * (N + E))

Reason:
 This function runs both the exact algorithm and the greedy algorithm.
 Since find_minimum_coverage(...) is much slower than the greedy one, the total complexity is dominated by the exact search.

Space Complexity
 O(N)

Reason:
 It only stores the results returned by the two methods and some temporary variables.

Overall summary

is_valid_coverage(...)
 Time: O(N + E)
 Space: O(N)

find_minimum_coverage(...)
 Time: O(2^N * (N + E))
 Space: O(N)

find_fast_coverage(...)
 Time: O(N * (N + E))
 Space: O(N)

compare_coverage(...)
 Time: O(2^N * (N + E))
 Space: O(N)

Conclusion:
 The exact solution is correct but very expensive, so it is only suitable for small graphs.
 The greedy solution is much faster and more practical for large graphs, but it does not always guarantee the minimum result.


---

## Complexity of exercise2_



---

## Complexity of exercise3_


---



# Complexity of Final Question
