def make_undirected_graph(nodes, edges):
    graph = {node: set() for node in nodes}

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    return graph


def is_valid_invitation(invited, graph):
    """
    Check if no conflict exists between any two invited users.
    Time Complexity: O(k^2)
    """
    invited = list(invited)

    for i in range(len(invited)):
        u = invited[i]

        for j in range(i + 1, len(invited)):
            v = invited[j]

            if v in graph.get(u, set()):
                return False

    return True


def can_add(user, current_set, graph):
    """
    Check if user has no conflict with current_set.
    """
    for selected_user in current_set:
        if selected_user in graph.get(user, set()):
            return False

    return True


def find_max_invitations_exact(graph):
    """
    Exact solution using backtracking with pruning.
    Return: (max_size, best_set)
    """
    users = list(graph.keys())
    best_set = []

    def backtrack(index, current_set):
        nonlocal best_set

        # pruning
        if len(current_set) + (len(users) - index) <= len(best_set):
            return

        # end case
        if index == len(users):
            if len(current_set) > len(best_set):
                best_set = current_set.copy()
            return

        u = users[index]

        # choose u
        if can_add(u, current_set, graph):
            current_set.append(u)
            backtrack(index + 1, current_set)
            current_set.pop()

        # do not choose u
        backtrack(index + 1, current_set)

    backtrack(0, [])

    return len(best_set), best_set


def find_max_invitations_greedy(graph):
    """
    Greedy heuristic:
    choose the node with the smallest degree in remaining graph.
    Return: (size, invited)
    """
    remaining = set(graph.keys())
    invited = []

    while remaining:
        min_degree = float("inf")
        chosen_user = None

        for u in remaining:
            degree = 0

            for v in graph.get(u, set()):
                if v in remaining:
                    degree += 1

            if degree < min_degree:
                min_degree = degree
                chosen_user = u

        invited.append(chosen_user)

        remaining.remove(chosen_user)

        for neighbor in graph.get(chosen_user, set()):
            remaining.discard(neighbor)

    return len(invited), invited


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":

    print("===== Exercise 1 Tests =====")

    # Test 1: Empty graph
    graph_empty = make_undirected_graph(
        nodes=[1, 2, 3, 4],
        edges=[]
    )

    print("\nTest 1: Empty graph")
    print("Exact:", find_max_invitations_exact(graph_empty))
    print("Greedy:", find_max_invitations_greedy(graph_empty))

    # Test 2: Fully connected graph
    graph_full = make_undirected_graph(
        nodes=[1, 2, 3, 4],
        edges=[
            (1, 2), (1, 3), (1, 4),
            (2, 3), (2, 4),
            (3, 4)
        ]
    )

    print("\nTest 2: Fully connected graph")
    print("Exact:", find_max_invitations_exact(graph_full))
    print("Greedy:", find_max_invitations_greedy(graph_full))

    # Test 3: Single user
    graph_single = make_undirected_graph(
        nodes=[1],
        edges=[]
    )

    print("\nTest 3: Single user")
    print("Exact:", find_max_invitations_exact(graph_single))
    print("Greedy:", find_max_invitations_greedy(graph_single))

    # Test 4: Simple path graph
    graph_path = make_undirected_graph(
        nodes=[1, 2, 3, 4],
        edges=[(1, 2), (2, 3), (3, 4)]
    )

    print("\nTest 4: Simple path graph")
    print("is_valid_invitation([1, 3]):", is_valid_invitation([1, 3], graph_path))
    print("is_valid_invitation([1, 2]):", is_valid_invitation([1, 2], graph_path))
    print("Exact:", find_max_invitations_exact(graph_path))
    print("Greedy:", find_max_invitations_greedy(graph_path))