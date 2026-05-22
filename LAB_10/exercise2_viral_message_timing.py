from typing import List, Tuple


def maximize_reach_exact(budget: int, costs: List[int], reaches: List[int]) -> Tuple[int, List[int]]:
    """
    Exact solution using dynamic programming for 0/1 knapsack.

    Return:
        (max_reach, selected_users_list)
    """

    n = len(costs)

    # dp[i][b] means:
    # using first i users, with budget b, the maximum reach we can get
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        user_cost = costs[i - 1]
        user_reach = reaches[i - 1]

        for b in range(budget + 1):
            # Case 1: do not choose this user
            dp[i][b] = dp[i - 1][b]

            # Case 2: choose this user if budget is enough
            if user_cost <= b:
                choose_value = dp[i - 1][b - user_cost] + user_reach

                if choose_value > dp[i][b]:
                    dp[i][b] = choose_value

    max_reach = dp[n][budget]

    # Backtrack to find selected users
    selected_users = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_users.append(i - 1)
            b -= costs[i - 1]

    selected_users.reverse()

    return max_reach, selected_users


def is_within_budget(selection: List[int], costs: List[int], budget: int) -> bool:
    """
    Check if the total cost of selected users is within budget.
    """

    total_cost = 0

    for user in selection:
        total_cost += costs[user]

    return total_cost <= budget


def maximize_reach_greedy(budget: int, costs: List[int], reaches: List[int]) -> Tuple[int, List[int]]:
    """
    Greedy approximation by reach/cost ratio.
    Pick users with highest ratio first.

    Return:
        (total_reach, selected_users)
    """

    n = len(costs)
    items = []

    for i in range(n):
        # Assume costs are positive integers
        ratio = reaches[i] / costs[i]
        items.append((i, costs[i], reaches[i], ratio))

    # Sort by ratio from high to low
    items.sort(key=lambda x: x[3], reverse=True)

    remaining_budget = budget
    total_reach = 0
    selected_users = []

    for user_id, user_cost, user_reach, ratio in items:
        if user_cost <= remaining_budget:
            selected_users.append(user_id)
            remaining_budget -= user_cost
            total_reach += user_reach

    return total_reach, selected_users


def compare_exact_and_greedy(budget: int, costs: List[int], reaches: List[int]) -> None:
    """
    Compare exact DP solution and greedy solution.
    """

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    print("Exact maximum reach:", exact_reach)
    print("Exact selected users:", exact_users)
    print("Greedy reach:", greedy_reach)
    print("Greedy selected users:", greedy_users)

    if exact_reach == greedy_reach:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy is faster, but it did not find the optimal solution.")


def print_test_result(test_name, expected, real):
    print("\n---", test_name, "---")
    print("Expected Result:")
    print(expected)
    print("Real Result:")
    print(real)


def main():
    print("===== Test Set for Edge Cases =====")

    # Edge Case 1: Empty user list
    # No users can be selected, so max reach should be 0.
    budget = 10
    costs = []
    reaches = []

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 0,
        "exact_users": [],
        "greedy_reach": 0,
        "greedy_users": []
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 1: Empty user list", expected, real)


    # Edge Case 2: Budget is 0
    # No user can be selected because budget is 0.
    budget = 0
    costs = [2, 3, 4]
    reaches = [10, 20, 30]

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 0,
        "exact_users": [],
        "greedy_reach": 0,
        "greedy_users": []
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 2: Budget is 0", expected, real)


    # Edge Case 3: All users are too expensive
    # Every cost is larger than the budget, so no user can be selected.
    budget = 5
    costs = [6, 7, 8]
    reaches = [10, 20, 30]

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 0,
        "exact_users": [],
        "greedy_reach": 0,
        "greedy_users": []
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 3: All users are too expensive", expected, real)


    # Edge Case 4: Budget can select all users
    # Total cost = 2 + 3 + 4 = 9, budget = 10.
    # Exact selects all users.
    # Greedy also selects all users, but the order is based on ratio.
    budget = 10
    costs = [2, 3, 4]
    reaches = [10, 20, 30]

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 60,
        "exact_users": [0, 1, 2],
        "greedy_reach": 60,
        "greedy_users": [2, 1, 0]
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 4: Budget can select all users", expected, real)


    # Edge Case 5: Check is_within_budget
    # Selected users are 0 and 2.
    # Total cost = 3 + 5 = 8, budget = 10.
    budget = 10
    costs = [3, 4, 5]
    selection = [0, 2]

    expected = True
    real = is_within_budget(selection, costs, budget)

    print_test_result("Edge Case 5: is_within_budget returns True", expected, real)


    # Edge Case 6: Check is_within_budget returns False
    # Selected users are 0, 1 and 2.
    # Total cost = 3 + 4 + 5 = 12, budget = 10.
    budget = 10
    costs = [3, 4, 5]
    selection = [0, 1, 2]

    expected = False
    real = is_within_budget(selection, costs, budget)

    print_test_result("Edge Case 6: is_within_budget returns False", expected, real)


    # Edge Case 7: Greedy fails to find optimal solution
    # Greedy chooses user 0 first because it has high ratio.
    # But the optimal solution is user 1 + user 2.
    budget = 10
    costs = [6, 5, 5]
    reaches = [12, 10, 10]

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 20,
        "exact_users": [1, 2],
        "greedy_reach": 12,
        "greedy_users": [0]
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 7: Greedy fails to find optimal solution", expected, real)


    # Edge Case 8: Normal case where exact and greedy are different
    # Exact chooses user 1 and user 3.
    # Greedy chooses user 1 and user 0 because of ratio order.
    budget = 8
    costs = [2, 3, 4, 5]
    reaches = [6, 10, 12, 15]

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    expected = {
        "exact_reach": 25,
        "exact_users": [1, 3],
        "greedy_reach": 16,
        "greedy_users": [1, 0]
    }

    real = {
        "exact_reach": exact_reach,
        "exact_users": exact_users,
        "greedy_reach": greedy_reach,
        "greedy_users": greedy_users
    }

    print_test_result("Edge Case 8: Normal case where exact and greedy are different", expected, real)


    print("\n===== Extra Comparison Output =====")
    budget = 10
    costs = [6, 5, 5]
    reaches = [12, 10, 10]
    compare_exact_and_greedy(budget, costs, reaches)


if __name__ == "__main__":
    main()