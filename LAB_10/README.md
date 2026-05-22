## File Structure:

```
/LAB _10/
├── exercise1_
├── exercise2_viral_message_timing.py
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

## Solution of exercise1_



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

## Solution of exercise3_


---

# Solution of Final Question


---

# Complexity analysis summary

## Complexity of exercise1_



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

## Complexity of exercise3_


---

# Complexity of Final Question


---
