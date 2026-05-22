import random
import math


def make_undirected_graph(nodes, edges):
    graph = {node: set() for node in nodes}

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    return graph


def count_cross_edges(groupA, groupB, graph):
    """
    Count edges between groupA and groupB.
    Time Complexity: O(E)
    """
    setB = set(groupB)
    cross_edges = 0

    for u in groupA:
        for v in graph.get(u, set()):
            if v in setB:
                cross_edges += 1

    return cross_edges


def is_balanced(groupA, groupB, n):
    """
    Check 40% balance constraint.
    """
    min_size = math.ceil(0.4 * n)

    return len(groupA) >= min_size and len(groupB) >= min_size


def create_random_balanced_split(nodes):
    """
    Create random split respecting 40% constraint.
    """
    nodes = list(nodes)
    n = len(nodes)

    min_size = math.ceil(0.4 * n)

    if n < 2:
        raise ValueError("No valid balanced two-group split.")

    if min_size > n - min_size:
        raise ValueError("No valid balanced split with 40% constraint.")

    random.shuffle(nodes)

    sizeA = random.randint(min_size, n - min_size)

    groupA = set(nodes[:sizeA])
    groupB = set(nodes[sizeA:])

    return groupA, groupB


def find_balanced_partition_greedy(graph):
    """
    Greedy local search.

    Start with a random balanced split.
    Move one user if:
    - balance is still valid
    - cross_edges decreases

    Return: (cross_edges, groupA, groupB)
    """
    nodes = list(graph.keys())
    n = len(nodes)

    if n < 2:
        return None, set(nodes), set()

    groupA, groupB = create_random_balanced_split(nodes)

    best_cross = count_cross_edges(groupA, groupB, graph)
    improved = True

    while improved:
        improved = False

        for u in nodes:

            if u in groupA:
                newA = set(groupA)
                newB = set(groupB)

                newA.remove(u)
                newB.add(u)

            else:
                newA = set(groupA)
                newB = set(groupB)

                newB.remove(u)
                newA.add(u)

            if is_balanced(newA, newB, n):
                new_cross = count_cross_edges(newA, newB, graph)

                if new_cross < best_cross:
                    groupA = newA
                    groupB = newB
                    best_cross = new_cross
                    improved = True

    return best_cross, groupA, groupB


def find_balanced_partition_local_search(graph, iterations):
    """
    Run greedy multiple times with different random starts.
    Return best result.
    """
    best_cross = float("inf")
    best_groupA = set()
    best_groupB = set()

    for _ in range(iterations):
        result = find_balanced_partition_greedy(graph)

        if result[0] is None:
            return result

        cross_edges, groupA, groupB = result

        if cross_edges < best_cross:
            best_cross = cross_edges
            best_groupA = groupA
            best_groupB = groupB

    return best_cross, best_groupA, best_groupB


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":

    print("===== Exercise 3 Tests =====")

    # Test 1: Empty graph
    graph_empty = make_undirected_graph(
        nodes=[1, 2, 3, 4],
        edges=[]
    )

    print("\nTest 1: Empty graph")
    print("Local Search:", find_balanced_partition_local_search(graph_empty, iterations=10))

    # Test 2: Fully connected graph
    nodes_full = [1, 2, 3, 4, 5]
    edges_full = []

    for i in range(len(nodes_full)):
        for j in range(i + 1, len(nodes_full)):
            edges_full.append((nodes_full[i], nodes_full[j]))

    graph_full = make_undirected_graph(
        nodes=nodes_full,
        edges=edges_full
    )

    print("\nTest 2: Fully connected graph")
    print("Local Search:", find_balanced_partition_local_search(graph_full, iterations=10))

    # Test 3: Single user
    graph_single = make_undirected_graph(
        nodes=[1],
        edges=[]
    )

    print("\nTest 3: Single user")
    print("Greedy:", find_balanced_partition_greedy(graph_single))

    # Test 4: Balanced simple path graph
    graph_path = make_undirected_graph(
        nodes=[1, 2, 3, 4],
        edges=[(1, 2), (2, 3), (3, 4)]
    )

    groupA = {1, 2}
    groupB = {3, 4}

    print("\nTest 4: Simple path graph")
    print("count_cross_edges:", count_cross_edges(groupA, groupB, graph_path))
    print("is_balanced:", is_balanced(groupA, groupB, len(graph_path)))
    print("Local Search:", find_balanced_partition_local_search(graph_path, iterations=10))

    # Test 5: Unbalanced split check
    groupA = {1, 2, 3}
    groupB = {4, 5, 6, 7, 8, 9, 10}

    print("\nTest 5: Unbalanced split check")
    print("is_balanced:", is_balanced(groupA, groupB, 10))

    # Test 6: Valid balanced split check
    groupA = {1, 2, 3, 4}
    groupB = {5, 6, 7, 8, 9, 10}

    print("\nTest 6: Valid balanced split check")
    print("is_balanced:", is_balanced(groupA, groupB, 10))