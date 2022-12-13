from typing import List

import pytest

from data_structures import Node
from utils import create_GenericTree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def preorder(self, root: Node) -> List[int]:
        ans = []

        def dfs(node):
            ans.append(node.val)
            for c in node.children:
                dfs(c)

        if root:
            dfs(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "preorder",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None, 5, 6])
    assert solution(root) == [1, 3, 5, 6, 2, 4]


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
    assert solution(root) == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_GenericTree([1])
    assert solution(root) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None])
    assert solution(root) == [1, 3, 2, 4]
