def maximize_reach(budget, costs, influences):
    n = len(costs)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = costs[i - 1]
        influence = influences[i - 1]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if cost <= b:
                candidate = dp[i - 1][b - cost] + influence
                if candidate > dp[i][b]:
                    dp[i][b] = candidate

    selected_users = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_users.append(i - 1)
            b -= costs[i - 1]

    selected_users.reverse()
    return dp[n][budget], selected_users


def is_within_budget(selection, costs, budget):
    total_cost = 0

    for user in selection:
        total_cost += costs[user]

    return total_cost <= budget


def fast_alternative_strategy(budget, costs, influences):
    n = len(costs)
    items = []

    for i in range(n):
        ratio = influences[i] / costs[i]
        items.append((ratio, i))

    items.sort(reverse=True)

    selected_users = []
    total_influence = 0
    used_budget = 0

    for ratio, index in items:
        if used_budget + costs[index] <= budget:
            selected_users.append(index)
            used_budget += costs[index]
            total_influence += influences[index]

    return total_influence, selected_users


def compare_strategies(budget, costs, influences):
    exact_influence, exact_users = maximize_reach(budget, costs, influences)
    greedy_influence, greedy_users = fast_alternative_strategy(budget, costs, influences)

    print("Exact maximum influence:", exact_influence)
    print("Exact selected users:", exact_users)
    print("Greedy influence:", greedy_influence)
    print("Greedy selected users:", greedy_users)

    if greedy_influence == exact_influence:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy found a valid but non-optimal solution.")


def total_cost(selection, costs):
    s = 0
    for user in selection:
        s += costs[user]
    return s


def main():
    print("===== Test Set for Edge Cases =====")

    # Edge Case 1: Empty input
    print("\n--- Edge Case 1: Empty input ---")
    budget1 = 10
    costs1 = []
    influences1 = []

    real1_exact = maximize_reach(budget1, costs1, influences1)
    real1_greedy = fast_alternative_strategy(budget1, costs1, influences1)

    print("Expected:")
    print("maximize_reach = (0, [])")
    print("fast_alternative_strategy = (0, [])")
    print("is_within_budget([]) = True")

    print("Real:")
    print("maximize_reach =", real1_exact)
    print("fast_alternative_strategy =", real1_greedy)
    print("is_within_budget([]) =", is_within_budget([], costs1, budget1))

    # Edge Case 2: Budget = 0
    print("\n--- Edge Case 2: Budget = 0 ---")
    budget2 = 0
    costs2 = [3, 4, 5]
    influences2 = [30, 40, 50]

    real2_exact = maximize_reach(budget2, costs2, influences2)
    real2_greedy = fast_alternative_strategy(budget2, costs2, influences2)

    print("Expected:")
    print("maximize_reach = (0, [])")
    print("fast_alternative_strategy = (0, [])")
    print("No user can be selected")

    print("Real:")
    print("maximize_reach =", real2_exact)
    print("fast_alternative_strategy =", real2_greedy)

    # Edge Case 3: All costs bigger than budget
    print("\n--- Edge Case 3: All costs bigger than budget ---")
    budget3 = 2
    costs3 = [5, 6, 7]
    influences3 = [10, 20, 30]

    real3_exact = maximize_reach(budget3, costs3, influences3)
    real3_greedy = fast_alternative_strategy(budget3, costs3, influences3)

    print("Expected:")
    print("maximize_reach = (0, [])")
    print("fast_alternative_strategy = (0, [])")

    print("Real:")
    print("maximize_reach =", real3_exact)
    print("fast_alternative_strategy =", real3_greedy)

    # Edge Case 4: Single user fits exactly
    print("\n--- Edge Case 4: Single user fits exactly ---")
    budget4 = 5
    costs4 = [5]
    influences4 = [100]

    real4_exact = maximize_reach(budget4, costs4, influences4)
    real4_greedy = fast_alternative_strategy(budget4, costs4, influences4)

    print("Expected:")
    print("maximize_reach = (100, [0])")
    print("fast_alternative_strategy = (100, [0])")

    print("Real:")
    print("maximize_reach =", real4_exact)
    print("fast_alternative_strategy =", real4_greedy)

    # Edge Case 5: Single user does not fit
    print("\n--- Edge Case 5: Single user does not fit ---")
    budget5 = 4
    costs5 = [5]
    influences5 = [100]

    real5_exact = maximize_reach(budget5, costs5, influences5)
    real5_greedy = fast_alternative_strategy(budget5, costs5, influences5)

    print("Expected:")
    print("maximize_reach = (0, [])")
    print("fast_alternative_strategy = (0, [])")

    print("Real:")
    print("maximize_reach =", real5_exact)
    print("fast_alternative_strategy =", real5_greedy)

    # Edge Case 6: Multiple optimal selections possible
    print("\n--- Edge Case 6: Multiple optimal selections possible ---")
    budget6 = 4
    costs6 = [2, 2, 4]
    influences6 = [3, 3, 6]

    real6_exact = maximize_reach(budget6, costs6, influences6)
    real6_greedy = fast_alternative_strategy(budget6, costs6, influences6)

    print("Expected:")
    print("Best influence = 6")
    print("Possible exact selections: [2] or [0, 1]")

    print("Real:")
    print("maximize_reach =", real6_exact)
    print("fast_alternative_strategy =", real6_greedy)

    # Edge Case 7: Greedy fails but DP succeeds
    print("\n--- Edge Case 7: Greedy fails but DP succeeds ---")
    budget7 = 50
    costs7 = [10, 20, 30]
    influences7 = [60, 100, 120]

    real7_exact = maximize_reach(budget7, costs7, influences7)
    real7_greedy = fast_alternative_strategy(budget7, costs7, influences7)

    print("Expected:")
    print("maximize_reach = (220, [1, 2])")
    print("fast_alternative_strategy = (160, [0, 1])")

    print("Real:")
    print("maximize_reach =", real7_exact)
    print("fast_alternative_strategy =", real7_greedy)

    # Edge Case 8: Check budget validation helper
    print("\n--- Edge Case 8: Budget validation helper ---")
    budget8 = 15
    costs8 = [4, 6, 8]

    real8_a = is_within_budget([0, 1], costs8, budget8)
    real8_b = is_within_budget([1, 2], costs8, budget8)

    print("Expected:")
    print("is_within_budget([0, 1]) = True")
    print("is_within_budget([1, 2]) = True")

    print("Real:")
    print("is_within_budget([0, 1]) =", real8_a)
    print("is_within_budget([1, 2]) =", real8_b)

    # Edge Case 9: Exact and greedy give same answer
    print("\n--- Edge Case 9: Exact and greedy give same answer ---")
    budget9 = 10
    costs9 = [2, 3, 5]
    influences9 = [20, 30, 50]

    real9_exact = maximize_reach(budget9, costs9, influences9)
    real9_greedy = fast_alternative_strategy(budget9, costs9, influences9)

    print("Expected:")
    print("Both methods should reach influence 100 with users [0, 1, 2]")

    print("Real:")
    print("maximize_reach =", real9_exact)
    print("fast_alternative_strategy =", real9_greedy)

    print("\n===== Extra Comparison Output =====")
    compare_strategies(budget7, costs7, influences7)


if __name__ == "__main__":
    main()