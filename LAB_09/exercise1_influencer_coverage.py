from itertools import combinations


def is_valid_coverage(selected_users, graph):
    covered = set()

    for user in selected_users:
        covered.add(user)
        for neighbor in graph.get(user, []):
            covered.add(neighbor)

    for user in graph:
        if user not in covered:
            return False

    return True


def find_minimum_coverage(graph):
    users = list(graph.keys())
    n = len(users)

    if n == 0:
        return 0, []

    for size in range(1, n + 1):
        for subset in combinations(users, size):
            if is_valid_coverage(subset, graph):
                return size, list(subset)

    return n, users


def find_fast_coverage(graph):
    uncovered = set(graph.keys())
    selected_users = []

    if not graph:
        return 0, []

    while uncovered:
        best_user = None
        best_cover = set()

        for user in graph:
            current_cover = {user}
            for neighbor in graph[user]:
                current_cover.add(neighbor)

            current_cover = current_cover & uncovered

            if len(current_cover) > len(best_cover):
                best_user = user
                best_cover = current_cover

        selected_users.append(best_user)
        uncovered -= best_cover

    return len(selected_users), selected_users


def compare_coverage(graph):
    exact_size, exact_users = find_minimum_coverage(graph)
    greedy_size, greedy_users = find_fast_coverage(graph)

    print("Exact minimum coverage size:", exact_size)
    print("Exact selected users:", exact_users)
    print("Greedy coverage size:", greedy_size)
    print("Greedy selected users:", greedy_users)

    if greedy_size == exact_size:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy found a valid solution, but not always the minimum one.")


def print_graph(graph):
    if not graph:
        print("{}")
        return

    for user in graph:
        print(f"{user}: {graph[user]}")


def normalize_result(result):
    size, users = result
    return size, sorted(users)


def main():
    print("===== Test Set for Edge Cases =====")

    # Edge Case 1: Empty graph
    print("\n--- Edge Case 1: Empty graph ---")
    graph1 = {}
    print("Graph:")
    print_graph(graph1)

    real1_valid = is_valid_coverage([], graph1)
    real1_exact = find_minimum_coverage(graph1)
    real1_greedy = find_fast_coverage(graph1)

    print("Expected:")
    print("is_valid_coverage([]) = True")
    print("find_minimum_coverage = (0, [])")
    print("find_fast_coverage = (0, [])")

    print("Real:")
    print("is_valid_coverage([]) =", real1_valid)
    print("find_minimum_coverage =", real1_exact)
    print("find_fast_coverage =", real1_greedy)

    # Edge Case 2: Single node graph
    print("\n--- Edge Case 2: Single node graph ---")
    graph2 = {
        1: []
    }
    print("Graph:")
    print_graph(graph2)

    real2_valid_empty = is_valid_coverage([], graph2)
    real2_valid_one = is_valid_coverage([1], graph2)
    real2_exact = find_minimum_coverage(graph2)
    real2_greedy = find_fast_coverage(graph2)

    print("Expected:")
    print("is_valid_coverage([]) = False")
    print("is_valid_coverage([1]) = True")
    print("find_minimum_coverage = (1, [1])")
    print("find_fast_coverage = (1, [1])")

    print("Real:")
    print("is_valid_coverage([]) =", real2_valid_empty)
    print("is_valid_coverage([1]) =", real2_valid_one)
    print("find_minimum_coverage =", real2_exact)
    print("find_fast_coverage =", real2_greedy)

    # Edge Case 3: Two disconnected nodes
    print("\n--- Edge Case 3: Two disconnected nodes ---")
    graph3 = {
        1: [],
        2: []
    }
    print("Graph:")
    print_graph(graph3)

    real3_valid_one = is_valid_coverage([1], graph3)
    real3_valid_both = is_valid_coverage([1, 2], graph3)
    real3_exact = find_minimum_coverage(graph3)
    real3_greedy = find_fast_coverage(graph3)

    print("Expected:")
    print("is_valid_coverage([1]) = False")
    print("is_valid_coverage([1, 2]) = True")
    print("find_minimum_coverage = (2, [1, 2])")
    print("find_fast_coverage size = 2")

    print("Real:")
    print("is_valid_coverage([1]) =", real3_valid_one)
    print("is_valid_coverage([1, 2]) =", real3_valid_both)
    print("find_minimum_coverage =", real3_exact)
    print("find_fast_coverage =", real3_greedy)

    # Edge Case 4: Fully connected graph
    print("\n--- Edge Case 4: Fully connected graph ---")
    graph4 = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [1, 2, 3]
    }
    print("Graph:")
    print_graph(graph4)

    real4_valid = is_valid_coverage([1], graph4)
    real4_exact = find_minimum_coverage(graph4)
    real4_greedy = find_fast_coverage(graph4)

    print("Expected:")
    print("is_valid_coverage([1]) = True")
    print("find_minimum_coverage size = 1")
    print("find_fast_coverage size = 1")

    print("Real:")
    print("is_valid_coverage([1]) =", real4_valid)
    print("find_minimum_coverage =", real4_exact)
    print("find_fast_coverage =", real4_greedy)

    # Edge Case 5: Line graph
    print("\n--- Edge Case 5: Line graph ---")
    graph5 = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4]
    }
    print("Graph:")
    print_graph(graph5)

    real5_valid_24 = is_valid_coverage([2, 4], graph5)
    real5_valid_3 = is_valid_coverage([3], graph5)
    real5_exact = find_minimum_coverage(graph5)
    real5_greedy = find_fast_coverage(graph5)

    print("Expected:")
    print("is_valid_coverage([2, 4]) = True")
    print("is_valid_coverage([3]) = False")
    print("find_minimum_coverage = (2, [1, 4]) or (2, [2, 4])")
    print("find_fast_coverage size = 2")

    print("Real:")
    print("is_valid_coverage([2, 4]) =", real5_valid_24)
    print("is_valid_coverage([3]) =", real5_valid_3)
    print("find_minimum_coverage =", real5_exact)
    print("find_fast_coverage =", real5_greedy)

    # Edge Case 6: Star graph
    print("\n--- Edge Case 6: Star graph ---")
    graph6 = {
        1: [2, 3, 4, 5],
        2: [1],
        3: [1],
        4: [1],
        5: [1]
    }
    print("Graph:")
    print_graph(graph6)

    real6_valid_1 = is_valid_coverage([1], graph6)
    real6_valid_2 = is_valid_coverage([2], graph6)
    real6_exact = find_minimum_coverage(graph6)
    real6_greedy = find_fast_coverage(graph6)

    print("Expected:")
    print("is_valid_coverage([1]) = True")
    print("is_valid_coverage([2]) = False")
    print("find_minimum_coverage = (1, [1])")
    print("find_fast_coverage = (1, [1])")

    print("Real:")
    print("is_valid_coverage([1]) =", real6_valid_1)
    print("is_valid_coverage([2]) =", real6_valid_2)
    print("find_minimum_coverage =", real6_exact)
    print("find_fast_coverage =", real6_greedy)

    # Edge Case 7: Disconnected components
    print("\n--- Edge Case 7: Disconnected components ---")
    graph7 = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    print("Graph:")
    print_graph(graph7)

    real7_valid = is_valid_coverage([1, 3, 5], graph7)
    real7_exact = find_minimum_coverage(graph7)
    real7_greedy = find_fast_coverage(graph7)

    print("Expected:")
    print("is_valid_coverage([1, 3, 5]) = True")
    print("find_minimum_coverage size = 3")
    print("find_fast_coverage size = 3")

    print("Real:")
    print("is_valid_coverage([1, 3, 5]) =", real7_valid)
    print("find_minimum_coverage =", real7_exact)
    print("find_fast_coverage =", real7_greedy)

    # Edge Case 8: Small graph for exact vs greedy comparison
    print("\n--- Edge Case 8: Exact vs Greedy comparison ---")
    graph8 = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }
    print("Graph:")
    print_graph(graph8)

    real8_exact = find_minimum_coverage(graph8)
    real8_greedy = find_fast_coverage(graph8)

    print("Expected:")
    print("find_minimum_coverage size = 2")
    print("find_fast_coverage size >= 2")
    print("Both results should be valid coverage")

    print("Real:")
    print("find_minimum_coverage =", real8_exact)
    print("find_fast_coverage =", real8_greedy)
    print("exact result valid =", is_valid_coverage(real8_exact[1], graph8))
    print("greedy result valid =", is_valid_coverage(real8_greedy[1], graph8))

    print("\n===== Extra Comparison Output =====")
    compare_coverage(graph8)


if __name__ == "__main__":
    main()