from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Graph
    Time Complexity: O(V)
    Space Complexity: O(V)
    V = the number of vertice in graph
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        keys = set(rooms[0])
        while len(keys) > 0 and len(visited) < len(rooms):
            new_keys = set()
            for new_room in keys:
                visited.add(new_room)
                for new_key in rooms[new_room]:
                    if new_key not in visited:
                        new_keys.add(new_key)
            keys = new_keys
        return len(visited) == len(rooms)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "canVisitAllRooms",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(rooms=[[1], [2], [3], []])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(rooms=[[1, 3], [3, 0, 1], [2], [0]])
