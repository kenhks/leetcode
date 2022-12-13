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

    def postorder(self, root: Node) -> List[int]:
        ans = []

        def dfs(node):
            for c in node.children:
                dfs(c)
            ans.append(node.val)

        if root:
            dfs(root)
        return ans


class Solution2:
    """
    DFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def postorder(self, root: Node) -> List[int]:
        ans = []
        if root:
            stack = [root]
            while stack:
                parent_node = stack.pop()
                ans.append(parent_node.val)
                for node in parent_node.children:
                    stack.append(node)
        return ans[::-1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "postorder",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None, 5, 6])
    assert solution(root) == [5, 6, 3, 2, 4, 1]


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
    assert solution(root) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_GenericTree([1])
    assert solution(root) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_GenericTree([1, None, 3, 2, 4, None])
    assert solution(root) == [3, 2, 4, 1]
