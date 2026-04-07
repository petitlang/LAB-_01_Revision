from collections import defaultdict


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].neighbors.append(node2)
            self.nodes[node2].neighbors.append(node1)


# DFS Recursive
def dfs_recursive(graph, start_user):
    visited = set()
    result = []

    def helper(node_id):
        visited.add(node_id)
        result.append(node_id)

        for neighbor in graph.nodes[node_id].neighbors:
            if neighbor not in visited:
                helper(neighbor)

    if start_user in graph.nodes:
        helper(start_user)

    return result


# DFS Iterative
def dfs_iterative(graph, start_user):
    visited = set()
    result = []
    stack = []

    if start_user not in graph.nodes:
        return result

    stack.append(start_user)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # reverse to keep order similar to recursive
            for neighbor in reversed(graph.nodes[node].neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# Connected Components
def find_connected_components(graph):
    visited = set()
    components = []

    def dfs(node_id, component):
        visited.add(node_id)
        component.append(node_id)

        for neighbor in graph.nodes[node_id].neighbors:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node_id in graph.nodes:
        if node_id not in visited:
            component = []
            dfs(node_id, component)
            components.append(component)

    return components


# Is Connected
def is_connected(graph):
    if len(graph.nodes) == 0:
        return True

    components = find_connected_components(graph)
    return len(components) == 1


# Has Path
def has_path(graph, start_user, target_user):
    visited = set()
    stack = [start_user]

    if start_user not in graph.nodes or target_user not in graph.nodes:
        return False

    while stack:
        node = stack.pop()

        if node == target_user:
            return True

        if node not in visited:
            visited.add(node)

            for neighbor in graph.nodes[node].neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    return False


# Find Path
def find_path(graph, start_user, target_user):
    visited = set()
    stack = [start_user]
    parent = {}

    if start_user not in graph.nodes or target_user not in graph.nodes:
        return []

    parent[start_user] = None

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == target_user:
                # reconstruct path
                path = []
                while node is not None:
                    path.insert(0, node)
                    node = parent[node]
                return path

            for neighbor in graph.nodes[node].neighbors:
                if neighbor not in visited and neighbor not in parent:
                    parent[neighbor] = node
                    stack.append(neighbor)

    return []


# Component Sizes
def get_connected_components_sizes(graph):
    components = find_connected_components(graph)
    return [len(c) for c in components]


# Largest Component
def find_largest_component(graph):
    components = find_connected_components(graph)
    largest = []

    for c in components:
        if len(c) > len(largest):
            largest = c

    return largest


# Isolated Users
def find_isolated_users(graph):
    isolated = []

    for node_id in graph.nodes:
        if len(graph.nodes[node_id].neighbors) == 0:
            isolated.append(node_id)

    return isolated


if __name__ == "__main__":
    print("===== Test Set for Edge Cases =====")

    #  Edge Case 1: Empty graph 
    print("\n--- Edge Case 1: Empty graph ---")
    g1 = Graph()

    print("DFS Recursive:", dfs_recursive(g1, 1))
    print("DFS Iterative:", dfs_iterative(g1, 1))
    print("Connected Components:", find_connected_components(g1))
    print("Is Connected:", is_connected(g1))
    print("Has Path 1->2:", has_path(g1, 1, 2))
    print("Find Path 1->2:", find_path(g1, 1, 2))
    print("Component Sizes:", get_connected_components_sizes(g1))
    print("Largest Component:", find_largest_component(g1))
    print("Isolated Users:", find_isolated_users(g1))


    #  Edge Case 2: Single node 
    print("\n--- Edge Case 2: Single node ---")
    g2 = Graph()
    g2.add_node(1)

    print("DFS Recursive:", dfs_recursive(g2, 1))
    print("DFS Iterative:", dfs_iterative(g2, 1))
    print("Connected Components:", find_connected_components(g2))
    print("Is Connected:", is_connected(g2))
    print("Has Path 1->1:", has_path(g2, 1, 1))
    print("Find Path 1->1:", find_path(g2, 1, 1))
    print("Component Sizes:", get_connected_components_sizes(g2))
    print("Largest Component:", find_largest_component(g2))
    print("Isolated Users:", find_isolated_users(g2))


    #  Edge Case 3: Two disconnected nodes 
    print("\n--- Edge Case 3: Two disconnected nodes ---")
    g3 = Graph()
    g3.add_node(1)
    g3.add_node(2)

    print("Connected Components:", find_connected_components(g3))
    print("Is Connected:", is_connected(g3))
    print("Has Path 1->2:", has_path(g3, 1, 2))
    print("Isolated Users:", find_isolated_users(g3))


    #  Edge Case 4: Fully connected graph 
    print("\n--- Edge Case 4: Fully connected graph ---")
    g4 = Graph()
    for i in range(1, 5):
        g4.add_node(i)

    g4.add_edge(1, 2)
    g4.add_edge(1, 3)
    g4.add_edge(1, 4)
    g4.add_edge(2, 3)
    g4.add_edge(2, 4)
    g4.add_edge(3, 4)

    print("Connected Components:", find_connected_components(g4))
    print("Is Connected:", is_connected(g4))
    print("Largest Component:", find_largest_component(g4))


    #  Edge Case 5: Graph with cycle 
    print("\n--- Edge Case 5: Graph with cycle ---")
    g5 = Graph()
    for i in range(1, 5):
        g5.add_node(i)

    g5.add_edge(1, 2)
    g5.add_edge(2, 3)
    g5.add_edge(3, 1)  # cycle
    g5.add_edge(3, 4)

    print("DFS Recursive:", dfs_recursive(g5, 1))
    print("Has Path 1->4:", has_path(g5, 1, 4))
    print("Find Path 1->4:", find_path(g5, 1, 4))


    #  Edge Case 6: Multiple components 
    print("\n--- Edge Case 6: Multiple components ---")
    g6 = Graph()
    for i in range(1, 7):
        g6.add_node(i)

    g6.add_edge(1, 2)
    g6.add_edge(2, 3)
    g6.add_edge(4, 5)

    print("Connected Components:", find_connected_components(g6))
    print("Component Sizes:", get_connected_components_sizes(g6))
    print("Largest Component:", find_largest_component(g6))


    #  Edge Case 7: Isolated users 
    print("\n--- Edge Case 7: Isolated users ---")
    g7 = Graph()
    for i in range(1, 5):
        g7.add_node(i)

    g7.add_edge(1, 2)

    print("Isolated Users:", find_isolated_users(g7))