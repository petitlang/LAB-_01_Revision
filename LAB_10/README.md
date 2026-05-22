## File Structure:

```
/LAB _10/
├── exercise1_event_invitation.py
├── exercise2_viral_message_timing.py
├── exercise3_group_formation.py
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

## Solution of exercise1_event_invitation

1. is_valid_invitation(invited, graph)

This function checks if a given invited set is valid.

The graph is a conflict graph:

nodes = users
edges = conflicts

If two invited users have an edge between them, they cannot both be invited.

The function checks all pairs of invited users.

If one conflict edge exists, it returns False.
Otherwise, it returns True.

This function does not search for the best solution.
It only verifies one given invited set.

2. find_max_invitations_exact(graph)

This function finds the exact maximum invited set.

It uses backtracking with pruning.

For each user, there are two choices:

invite this user
do not invite this user

The algorithm keeps the best valid set found.

Pruning condition:

current_size + remaining_nodes <= best_size

If this condition is true, this branch cannot improve the best result.
So the algorithm stops exploring this branch.

This method gives the optimal solution, but it is exponential.
It is suitable only for small graphs.

3. can_add(user, current_set, graph)

This helper function checks if a user can be added to the current invited set.

It compares the candidate user with all users already in current_set.

If there is a conflict edge, it returns False.
Otherwise, it returns True.

4. find_max_invitations_greedy(graph)

This function is a fast heuristic method.

It repeatedly selects the node with the smallest degree in the remaining graph.

After selecting one user:

add this user to the invited list
remove this user from the remaining nodes
remove all its neighbors from the remaining nodes

This method is much faster than exact backtracking.

However, it does not always find the maximum independent set.

It gives a valid invited set, but not always the optimal one.


---

## Solution of exercise2_viral_message_timing

1. maximize_reach_exact(budget, costs, reaches)

This function solves the problem exactly by using dynamic programming.
It is based on the 0/1 knapsack problem.

Each user has two choices:
choose this user
or do not choose this user

The DP table stores the best reach we can get for each number of users and each budget value.
After filling the table, we backtrack from the last cell to find which users were selected.

This solution always finds the optimal maximum reach, but it needs more time and memory when the budget is large.


2. is_within_budget(selection, costs, budget)

This function checks if a selected list of users is valid.
It adds the costs of all selected users and compares the total cost with the budget.

If the total cost is less than or equal to the budget, the function returns True.
Otherwise, it returns False.

This function does not try to find the best solution.
It only verifies one given selection.


3. maximize_reach_greedy(budget, costs, reaches)

This function is a fast approximation method.
It calculates the reach/cost ratio for each user.

Then it sorts users by this ratio from highest to lowest.
After that, it selects users one by one if the remaining budget is enough.

This method is faster than exact DP, but it does not always find the optimal answer.


4. compare_exact_and_greedy(budget, costs, reaches)

This function runs both the exact DP solution and the greedy solution.
Then it prints their maximum reach and selected users.

It is useful for comparing the optimal solution and the fast approximation solution.
For small test cases, we can use it to show when greedy works and when greedy fails.

---

## Solution of exercise3_group_formation

1. count_cross_edges(groupA, groupB, graph)

This function counts the number of edges between two groups.

The graph is a friendship graph:

nodes = users
edges = friendships

A cross edge means:

one endpoint in groupA
one endpoint in groupB

The function scans the neighbors of each user in groupA.

If a neighbor is in groupB, we count one cross edge.

This function is used to evaluate the quality of a partition.

Smaller cross_edges means a better partition.

2. is_balanced(groupA, groupB, n)

This function checks the 40% balance constraint.

For n users:

min_size = 0.4 × n

A split is valid if:

|groupA| >= min_size
|groupB| >= min_size

If both conditions are true, the function returns True.
Otherwise, it returns False.

This helper function is used before accepting a move.

3. find_balanced_partition_greedy(graph)

This function tries to find a balanced partition with small cross edges.

First, it creates a random split that respects the 40% constraint.

Then it repeatedly tries to move one user from one group to the other.

A move is accepted only if:

balance constraint is still valid
new_cross_edges < current_cross_edges

The algorithm stops when no single move can improve the result.

This method is fast and simple.

However, it can get stuck in a local minimum.

So it may not always find the best possible partition.

4. find_balanced_partition_local_search(graph, iterations)

This function improves the greedy method.

It runs find_balanced_partition_greedy several times with different random initial splits.

For each run, it gets:

cross_edges, groupA, groupB

Then it keeps the best result.

More iterations usually give a better chance to find a smaller cut.

But the runtime also increases.

This method is still heuristic.
It does not guarantee the global optimum.

---

# Solution of Final Question


---

# Complexity analysis summary

## Complexity of exercise1_event_invitation

1. is_valid_invitation(invited, graph)

Time Complexity:

O(k²)

k is the number of invited users.

Reason:

We check all pairs of invited users.

Space Complexity:

O(1)

Reason:

We only use a few variables.

2. can_add(user, current_set, graph)

Time Complexity:

O(k)

k is the size of current_set.

Reason:

We compare the candidate user with all users already selected.

Space Complexity:

O(1)
3. find_max_invitations_exact(graph)

Time Complexity:

O(2^N × N)

N is the number of users.

Reason:

Each user has two choices:

invite / not invite

So there are up to:

2^N subsets

For each branch, checking whether a user can be added may take up to O(N).

Pruning reduces the practical runtime, but the worst case is still exponential.

Space Complexity:

O(N)

Reason:

The recursion depth is at most N.

The current set and best set can also contain up to N users.

4. find_max_invitations_greedy(graph)

Time Complexity:

O(N²)

Reason:

At each step, we search for the remaining node with the smallest degree.

In the simple implementation, this can scan many nodes and edges repeatedly.

Space Complexity:

O(N)

Reason:

We store:

remaining
invited

Overall summary:

The exact method is optimal but exponential.

The greedy method is faster and scalable, but not always optimal.



## Complexity of exercise2_viral_message_timing

1. maximize_reach_exact(budget, costs, reaches)

Time Complexity:
O(N * budget)

Reason:
There are N users.
For each user, we check all budget values from 0 to budget.
So the total number of DP states is N * budget.

Space Complexity:
O(N * budget)

Reason:
We use a 2D DP table with size (N + 1) * (budget + 1).
This table stores the best reach for each subproblem.


2. is_within_budget(selection, costs, budget)

Time Complexity:
O(K)

K is the number of selected users.

In the worst case, K can be N.
So the worst-case time complexity is:

O(N)

Reason:
We only scan the selected users once and add their costs.

Space Complexity:
O(1)

Reason:
We only use one variable total_cost.
No extra large data structure is needed.


3. maximize_reach_greedy(budget, costs, reaches)

Time Complexity:
O(N log N)

Reason:
First, we create a list of N users with their reach/cost ratio.
This takes O(N).

Then we sort the users by ratio.
Sorting takes O(N log N).

Finally, we scan all users once to select valid users.
This takes O(N).

So the total time complexity is:

O(N log N)

Space Complexity:
O(N)

Reason:
We store all users and their ratios in an items list.
The selected_users list can also store up to N users.


4. compare_exact_and_greedy(budget, costs, reaches)

Time Complexity:
O(N * budget + N log N)

Reason:
It runs the exact DP solution and the greedy solution.

Exact DP:
O(N * budget)

Greedy:
O(N log N)

So the total complexity is:

O(N * budget + N log N)

Usually, O(N * budget) is the main part.

Space Complexity:
O(N * budget)

Reason:
The exact DP solution uses a 2D DP table.
The greedy solution only uses O(N), so the DP table is the main memory cost.


Overall summary

The exact DP solution is optimal, but it is slower and uses more memory.
It is good when N and budget are not too large.

The greedy solution is faster and easier to use for large inputs.
However, it is only an approximation and may fail to find the optimal solution.

The budget checking function is simple and efficient.
It is useful for verifying whether a selected solution is valid.

---

## Complexity of exercise3_group_formation

1. count_cross_edges(groupA, groupB, graph)

Time Complexity:

O(E)

E is the number of edges.

Reason:

We scan friendship edges and count edges crossing between the two groups.

Space Complexity:

O(N)

Reason:

We convert groupB into a set for fast lookup.

2. is_balanced(groupA, groupB, n)

Time Complexity:

O(1)

Reason:

We only check group sizes.

Space Complexity:

O(1)
3. find_balanced_partition_greedy(graph)

Time Complexity:

O(I × N × E)

where:

I = number of improvement rounds
N = number of users
E = number of edges

Reason:

In each round, the algorithm tries to move users one by one.

For each possible move, it may count cross edges again.

So the simple version is:

I × N × E

Space Complexity:

O(N)

Reason:

We store:

groupA
groupB
newA
newB
4. find_balanced_partition_local_search(graph, iterations)

Time Complexity:

O(iterations × I × N × E)

Reason:

It runs the greedy algorithm multiple times.

Each run costs:

O(I × N × E)

So total runtime is:

iterations × greedy_time

Space Complexity:

O(N)

Reason:

We store the best partition and the current partition.

Overall summary:

The greedy method is fast but may stop at a local minimum.

The local search method improves the result by trying several random starts.

More iterations usually improve solution quality, but runtime increases linearly.


---

# Complexity of Final Question

The final question does not implement a new algorithm.

It compares the three exercises from the point of view of:

- problem classification
- decision vs optimization
- scalability
- approximation
- engineering choices
- edge cases

So the complexity mainly comes from the algorithms discussed in EX1, EX2 and EX3.

---

1. Classification

This part classifies each core problem.

Time Complexity:
O(1)

Reason:
We only compare known complexity classes:

P / NP / NP-Complete / NP-Hard

There is no computation over input data.

Space Complexity:
O(1)

---

2. Decision vs Optimization

This part transforms each optimization problem into a decision problem.

EX1:

Optimization:
maximize |invited|

Decision:
Does there exist an invited set with |invited| ≥ k?

EX2:

Optimization:
maximize sum(reach)

Decision:
Does there exist a selection with:

sum(reach) ≥ k
sum(cost) ≤ budget

EX3:

Optimization:
minimize cross_edges

Decision:
Does there exist a balanced partition with:

cross_edges ≤ k
|groupA| ≥ 0.4N
|groupB| ≥ 0.4N

Time Complexity:
O(1)

Reason:
This is theoretical transformation, not an algorithm running on data.

Space Complexity:
O(1)

---

3. Scalability

This part compares how the algorithms behave when N grows.

EX1 exact:

O(2^N × N)

Not scalable.

EX2 DP:

O(N × budget)

Scalable only when N and budget are small / medium.

EX3 greedy:

O(I × N × E)

Usable with heuristics, but not exact.

EX3 local search:

O(iterations × I × N × E)

More iterations → better quality but slower runtime.

---

4. Engineering Perspective

This part does not add new complexity.

It explains when approximation is acceptable.

Approximation is useful when:

N is very large
exact method is too slow
near-optimal solution is enough
runtime is more important than exact optimum

Time Complexity:
depends on chosen method

Example:

greedy → polynomial time
exact search → exponential time
DP → pseudo-polynomial time

---

5. Reflection

This part explains why some problems are hard.

Main reason:

search space grows very fast.

Typical cases:

subsets = 2^N
partitions ≈ 2^N
permutations = N!

So exact methods become impossible for large N.

No new algorithm is implemented in this section.

Time Complexity:
O(1)

Space Complexity:
O(1)

---

Overall summary

Final Question is mainly theoretical.

It summarizes the complexity of the three exercises:

EX1:
exact = O(2^N × N)
greedy = O(N²)

EX2:
exact DP = O(N × budget)
greedy = O(N log N)

EX3:
greedy = O(I × N × E)
local search = O(iterations × I × N × E)

The main conclusion:

Exact methods give optimal solutions but do not scale well.

Greedy / heuristic / local search methods scale better, but they do not always guarantee the global optimum.

---
