from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class User:
    user_id: int
    friends: List[int] = field(default_factory=list)


class SocialGraph:
    def __init__(self, max_user_id: int = 100) -> None:
        """
        max_user_id:
            Used to initialize the adjacency matrix.
            Assumes user IDs are integers in [0, max_user_id].
        """
        self.users: Dict[int, User] = {}
        self.matrix: List[List[int]] = [
            [0 for _ in range(max_user_id + 1)]
            for _ in range(max_user_id + 1)
        ]

    # 2. add_user
    def add_user(self, user_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = User(user_id=user_id)

    # 3. add_friendship(u, v)
    def add_friendship(self, user1: int, user2: int) -> None:
        if user1 in self.users and user2 in self.users:
            if user2 not in self.users[user1].friends:
                self.users[user1].friends.append(user2)
            if user1 not in self.users[user2].friends:
                self.users[user2].friends.append(user1)

            self.matrix[user1][user2] = 1
            self.matrix[user2][user1] = 1

    # 4. remove_friendship
    def remove_friendship(self, user1: int, user2: int) -> None:
        if user1 in self.users and user2 in self.users:
            if user2 in self.users[user1].friends:
                self.users[user1].friends.remove(user2)
            if user1 in self.users[user2].friends:
                self.users[user2].friends.remove(user1)

            self.matrix[user1][user2] = 0
            self.matrix[user2][user1] = 0

    # 5. are_friends
    def are_friends(self, user1: int, user2: int) -> bool:
        if user1 not in self.users or user2 not in self.users:
            return False
        return self.matrix[user1][user2] == 1

    # 6. get_friends
    def get_friends(self, user_id: int) -> List[int]:
        if user_id in self.users:
            return self.users[user_id].friends.copy()
        return []

    # 7. get_degree(u)
    def get_degree(self, user_id: int) -> int:
        if user_id in self.users:
            return len(self.users[user_id].friends)
        return 0

    # 8. get_num_users
    def get_num_users(self) -> int:
        return len(self.users)

    # 9. get_num_edges
    def get_num_edges(self) -> int:
        total = 0
        for user_id in self.users:
            total += len(self.users[user_id].friends)
        return total // 2

    # 10. is_complete_graph()
    def is_complete_graph(self) -> bool:
        n = len(self.users)
        for user_id in self.users:
            if self.get_degree(user_id) != n - 1:
                return False
        return True

    # 11. graph_density()
    def graph_density(self) -> float:
        v = self.get_num_users()
        e = self.get_num_edges()

        if v <= 1:
            return 0.0

        return (2 * e) / (v * (v - 1))

    # 12. degree_distribution
    def degree_distribution(self) -> Dict[int, int]:
        distribution: Dict[int, int] = {}

        for user_id in self.users:
            degree = self.get_degree(user_id)
            if degree not in distribution:
                distribution[degree] = 0
            distribution[degree] += 1

        return distribution

    # 13. matrix_to_list()
    def matrix_to_list(self) -> None:
        for user1 in self.users:
            self.users[user1].friends = []

            for user2 in self.users:
                if self.matrix[user1][user2] == 1:
                    self.users[user1].friends.append(user2)

    # 14. list_to_matrix
    def list_to_matrix(self) -> None:
        for user1 in self.users:
            for user2 in self.users:
                self.matrix[user1][user2] = 0

        for user1 in self.users:
            for user2 in self.users[user1].friends:
                self.matrix[user1][user2] = 1


if __name__ == "__main__":
    graph = SocialGraph(max_user_id=10)

    # Add users
    for uid in [1, 2, 3, 4]:
        graph.add_user(uid)

    # Add friendships
    graph.add_friendship(1, 2)
    graph.add_friendship(2, 3)

    print("Friends of 2:", graph.get_friends(2))
    print("Are 1 and 2 friends?", graph.are_friends(1, 2))
    print("Are 1 and 3 friends?", graph.are_friends(1, 3))
    print("Degree of 2:", graph.get_degree(2))
    print("Number of users:", graph.get_num_users())
    print("Number of edges:", graph.get_num_edges())
    print("Is complete graph?", graph.is_complete_graph())
    print("Graph density:", graph.graph_density())
    print("Degree distribution:", graph.degree_distribution())

    graph.remove_friendship(1, 2)
    print("After removing (1,2), are 1 and 2 friends?", graph.are_friends(1, 2))