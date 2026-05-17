def is_valid_labeling(labeling, graph):
    """
    Check whether a given labeling is valid.

    For every edge (u, v), connected users must have different labels.

    Time Complexity: O(E)
    Space Complexity: O(1)
    """

    for u in graph:
        for v in graph[u]:

            # Check each undirected edge only once
            if u < v:
                if labeling[u] == labeling[v]:
                    return False

    return True


def is_safe(user, label, graph, labeling):
    """
    Check if one label can be assigned to the current user.

    The label is safe if no neighbor already has the same label.

    Time Complexity: O(degree(user))
    Space Complexity: O(1)
    """

    for neighbor in graph[user]:
        if labeling[neighbor] == label:
            return False

    return True


def backtrack(user, k, graph, labeling):
    """
    Recursively assign labels to users one by one.

    Time Complexity: O(k^N)
    Space Complexity: O(N)
    """

    n = len(graph)

    # All users are labeled
    if user == n:
        return True

    # Try each possible label
    for label in range(k):

        if is_safe(user, label, graph, labeling):

            labeling[user] = label

            if backtrack(user + 1, k, graph, labeling):
                return True

            # Backtrack
            labeling[user] = -1

    return False


def assign_labels(k, graph):
    """
    Try to label the graph using at most k labels.

    Return:
        (True, labeling) if possible
        (False, []) otherwise
    """

    n = len(graph)

    if n == 0:
        return True, []

    labeling = [-1] * n

    if backtrack(0, k, graph, labeling):
        return True, labeling

    return False, []


def find_min_labels(graph):
    """
    Find the minimum number of labels.

    Try k = 1, 2, 3, ..., n.
    The first successful k is the minimum number of labels.

    Time Complexity: exponential
    Space Complexity: O(N)
    """

    n = len(graph)

    if n == 0:
        return 0, []

    for k in range(1, n + 1):

        success, labeling = assign_labels(k, graph)

        if success:
            return k, labeling

    return n, []


def print_result(graph, expected_text):
    """
    Helper function for displaying test results.
    """

    print("Graph:")
    for node in graph:
        print(f"{node}: {graph[node]}")

    print("Expected:")
    print(expected_text)

    print("Real:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum_k =", minimum_k)
    print("labeling =", labeling)

    if labeling:
        print("valid =", is_valid_labeling(labeling, graph))
    else:
        print("valid =", True)

    print("-" * 50)


def run_tests():
    """
    Test Set for Edge Cases
    """

    print("===== Test Set for Edge Cases =====")

    # Edge Case 1 — Empty graph
    print("\n--- Edge Case 1: Empty graph ---")
    graph = {}
    labeling = []

    print("Graph:")
    print(graph)

    print("Expected:")
    print("is_valid_labeling(labeling, graph) = True")
    print("find_min_labels(graph) = (0, [])")

    print("Real:")
    print("is_valid_labeling(labeling, graph) =", is_valid_labeling(labeling, graph))
    print("find_min_labels(graph) =", find_min_labels(graph))
    print("-" * 50)


    # Edge Case 2 — One edge with k = 1
    print("\n--- Edge Case 2: One edge with k = 1 ---")
    graph = {
        0: [1],
        1: [0]
    }
    k = 1

    print("Graph:")
    for node in graph:
        print(f"{node}: {graph[node]}")

    print("Expected:")
    print("assign_labels(k, graph) = False")

    print("Real:")
    success, labeling = assign_labels(k, graph)
    print("assign_labels(k, graph) =", success)
    print("labeling =", labeling)
    print("-" * 50)


    # Edge Case 3 — Triangle graph
    print("\n--- Edge Case 3: Triangle graph ---")
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    print_result(
        graph,
        "find_min_labels(graph) = (3, [0, 1, 2])"
    )


    # Edge Case 4 — Square graph
    print("\n--- Edge Case 4: Square graph ---")
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    print_result(
        graph,
        "find_min_labels(graph) = (2, [0, 1, 0, 1])"
    )


    # Extra Test — Complete graph K4
    print("\n--- Extra Test: Complete graph K4 ---")
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }

    print_result(
        graph,
        "find_min_labels(graph) = (4, [0, 1, 2, 3])"
    )


    # Extra Test — One node
    print("\n--- Extra Test: One node ---")
    graph = {
        0: []
    }

    print_result(
        graph,
        "find_min_labels(graph) = (1, [0])"
    )


if __name__ == "__main__":
    run_tests()