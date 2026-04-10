from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass
class User:
    user_id: int
    friends: List[int] = field(default_factory=list)


class SocialGraph:
    def __init__(self) -> None:
        self.users: Dict[int, User] = {}

    # Basic graph operations
    def add_user(self, user_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = User(user_id=user_id)

    def add_friendship(self, user1: int, user2: int) -> None:
        if user1 in self.users and user2 in self.users:
            if user2 not in self.users[user1].friends:
                self.users[user1].friends.append(user2)
            if user1 not in self.users[user2].friends:
                self.users[user2].friends.append(user1)

    def get_friends(self, user_id: int) -> List[int]:
        if user_id in self.users:
            return self.users[user_id].friends.copy()
        return []

    # Part A: bfs(start_user)
    def bfs(self, start_user: int) -> List[int]:
        visited: Set[int] = set()
        order: List[int] = []
        queue: deque[int] = deque()

        if start_user not in self.users:
            return order

        queue.append(start_user)
        visited.add(start_user)

        while queue:
            u = queue.popleft()
            order.append(u)

            for friend in self.get_friends(u):
                if friend not in visited:
                    queue.append(friend)
                    visited.add(friend)

        return order

    # Part B: bfs_with_distances(start_user)
    def bfs_with_distances(self, start_user: int) -> Dict[int, int]:
        visited: Set[int] = set()
        distance: Dict[int, int] = {}
        queue: deque[int] = deque()

        if start_user not in self.users:
            return distance

        queue.append(start_user)
        visited.add(start_user)
        distance[start_user] = 0

        while queue:
            u = queue.popleft()

            for friend in self.get_friends(u):
                if friend not in visited:
                    queue.append(friend)
                    visited.add(friend)
                    distance[friend] = distance[u] + 1

        return distance

    # Part C: shortest_path(start_user, target_user)
    def shortest_path(self, start_user: int, target_user: int) -> List[int]:
        visited: Set[int] = set()
        parent: Dict[int, int] = {}
        queue: deque[int] = deque()

        if start_user not in self.users or target_user not in self.users:
            return []

        queue.append(start_user)
        visited.add(start_user)

        while queue:
            u = queue.popleft()

            if u == target_user:
                break

            for friend in self.get_friends(u):
                if friend not in visited:
                    queue.append(friend)
                    visited.add(friend)
                    parent[friend] = u

        if target_user not in parent and target_user != start_user:
            return []

        path: List[int] = []
        current = target_user

        while current != start_user:
            path.append(current)
            current = parent[current]

        path.append(start_user)
        path.reverse()

        return path

    # Part D: degrees_of_separation(start_user, target_user)
    def degrees_of_separation(self, start_user: int, target_user: int) -> int:
        distance = self.bfs_with_distances(start_user)

        if target_user in distance:
            return distance[target_user]
        return -1

    # Part E: friends_within_k_hops(start_user, k)
    def friends_within_k_hops(self, start_user: int, k: int) -> Set[int]:
        distance = self.bfs_with_distances(start_user)
        result: Set[int] = set()

        for user in distance:
            if distance[user] <= k:
                result.add(user)

        return result


if __name__ == "__main__":
    graph = SocialGraph()

    # Add users
    for uid in [1, 2, 3, 4]:
        graph.add_user(uid)

    # Add friendships
    graph.add_friendship(1, 2)
    graph.add_friendship(2, 3)
    graph.add_friendship(3, 4)

    print("BFS(1):", graph.bfs(1))
    print("BFS with distances from 1:", graph.bfs_with_distances(1))
    print("Shortest Path 1->4:", graph.shortest_path(1, 4))
    print("Degrees of Separation 1->4:", graph.degrees_of_separation(1, 4))
    print("Friends within 2 hops from 1:", graph.friends_within_k_hops(1, 2))