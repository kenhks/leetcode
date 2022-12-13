from typing import List

import pytest

from data_structures import Node
from utils import create_GenericTree, parametrize_solution_cls


class Solution:
    """
    BFS, Iterative
    Time Complexity: O(h)
    Space Complexity: O(n)
    """

    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        result = [[root]]
        while len(result[-1]) > 0:
            next_level = []
            for node in result[-1]:
                if node.children:
                    next_level.extend(node.children)
            result.append(next_level)
        return [[j.val for j in i] for i in result[:-1]]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "levelOrder",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None, 5, 6])
    assert solution(root) == [[1], [3, 2, 4], [5, 6]]


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
    assert solution(root) == [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_GenericTree([1])
    assert solution(root) == [[1]]
