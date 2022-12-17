import pytest

from data_structures import Node
from utils import create_GenericTree, parametrize_solution_cls


class Solution:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def maxDepth(self, root: Node) -> int:
        level_nodes = [root] if root else []
        depth = 0
        while level_nodes:
            next_level_nodes = []
            for node in level_nodes:
                next_level_nodes.extend(node.children)
            level_nodes = next_level_nodes
            depth += 1
        return depth


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxDepth",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None, 5, 6])
    assert solution(root) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_GenericTree(
        [
            1,
            None,
            2,
            3,
            4,
            5,
            None,
            None,
            6,
            7,
            None,
            8,
            None,
            9,
            10,
            None,
            None,
            11,
            None,
            12,
            None,
            13,
            None,
            None,
            14,
        ]
    )
    assert solution(root) == 5


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_GenericTree([1])
    assert solution(root) == 1
